from flask import request
from flask_jwt_extended import create_access_token
from flask_restful import Resource 
from flask_bcrypt import generate_password_hash, check_password_hash
import database_interface as db
from static.CONSTANTS import *

class SignUpForAPI(Resource):
    def post(self):
        body = request.get_json()
        if not body: return {"message": NO_BODY_GIVEN_ERROR}, 400
        if "username" not in body: return {"message": NO_USERNAME_GIVEN_ERROR}, 400
        if "email" not in body: return {"message": NO_EMAIL_GIVEN_ERROR}, 400
        if "password" not in body: return {"message": NO_PASSWORD_GIVEN_ERROR}, 400
        
        username = body['username']
        email = body['email']
        password = generate_password_hash(body['password']).decode('utf8')

        try:
            db.executeQuery("INSERT INTO api_users VALUES (?, ?, ?, 0, 0)", params=(email, username, password))
        except Exception as e:
            return {"message": USER_ALREADY_EXISTS}
        return {'message': ACCOUNT_CREATED}, 200

def checkPassword(given_password, hashed_password):
    try:
        return check_password_hash(hashed_password, given_password)
    except Exception as e:
        return False

def retrievePwdHashForUser(username):
    try:
        return db.selectQuery("SELECT password FROM api_users WHERE username LIKE ?", params=(username,))[0]['password']
    except:
        return {"password": ""}



class AllowUsername(Resource):
    def post(self, username):
        body = request.get_json()
        admin_logged_in, error = checkAdminLogin(body)
        if not admin_logged_in: return {"message": "Something went wrong: " + error}, 400
        try:
            db.executeQuery("UPDATE api_users SET allowed_to_use_api = 1 WHERE username = ?", params=(username,))
            return {"message": USER_ALLOWED_ADDED}
        except:
            return {"message": UNEXPECTED_ERROR}


def checkAdminLogin(login: dict):
    logged_in, error = checkUserCombinationCorrect(login)
    if not logged_in: return False, error
    try:
        return db.selectQuery("SELECT is_admin FROM api_users WHERE username LIKE ?", params=(login['username'],))[0]['is_admin'], ''
    except:
        return 0

def checkUserCombinationCorrect(login: dict): # Should look like: {"username": "name", "password": "HasHEd PAssWord"}
    if not login: return False, NO_BODY_GIVEN_ERROR
    if "username" not in login: return False, NO_USERNAME_GIVEN_ERROR
    if "password" not in login: return False, NO_EMAIL_GIVEN_ERROR
    hashed_password = retrievePwdHashForUser(login["username"])
    password_correct = checkPassword(login['password'], hashed_password)
    if not password_correct: return False, USERNAME_PASSWORD_COMBINATION_INCORRECT
    return True, ""