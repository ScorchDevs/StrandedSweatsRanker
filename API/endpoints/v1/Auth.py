from flask_jwt_extended import create_access_token
from flask import request
from flask_jwt_extended import create_access_token
from flask_restful import Resource 
from flask_bcrypt import generate_password_hash, check_password_hash
import database_interface as db

class SignUpForAPI(Resource):
    def post(self):
        body = request.get_json()
        if not body: return {"message": "Missing parameters!"}, 400
        if "username" not in body: return {"message": "Missing username!"}, 400
        if "email" not in body: return {"message": "Missing email!"}, 400
        if "password" not in body: return {"message": "Missing password!"}, 400
        
        username = body['username']
        email = body['email']
        password = generate_password_hash(body['password']).decode('utf8')

        try:
            db.executeQuery("INSERT INTO api_users VALUES (?, ?, ?, 0, 0)", params=(email, username, password))
        except Exception as e:
            return {"message": 'Account already exists with that email or username!'}
        return {'message': 'Account succesfully created!'}, 200

def checkPassword(given_password, hashed_password):
    try:
        return check_password_hash(hashed_password, given_password)
    except:
        return False
def retrievePwdHashForUser(username):
    try:
        return db.selectQuery("SELECT password FROM api_users WHERE username LIKE ? AND is_admin = 1", params=(username,))[0]
    except:
        return {"password": ""}



class AllowUsername(Resource):
    def post(self, username):
        body = request.get_json()
        if not body: return {"message": "Missing parameters!"}, 400
        if "username" not in body: return {"message": "Missing username!"}, 400
        if "password" not in body: return {"message": "Missing password!"}, 400
        admin_pwd_hash = retrievePwdHashForUser(body['username'])["password"]

        if not admin_pwd_hash: return {"message": "You are not an administrator!"}
        admin_logged_in = checkPassword(body['password'], admin_pwd_hash)
        if not admin_logged_in: return {"message": "Password incorrect!"}

        db.executeQuery("UPDATE api_users SET allowed_to_use_api = 1 WHERE username = ?", params=(username,))
        return {"message": "User successfully added to allow list!"}