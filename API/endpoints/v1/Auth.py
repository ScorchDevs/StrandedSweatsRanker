from flask_jwt_extended import create_access_token
from flask import request
from flask_jwt_extended import create_access_token
from flask_restful import Resource 
from flask_bcrypt import generate_password_hash, check_password_hash
import database_interface as db

class SignUpForAPI(Resource):
    def post(self):
        body = request.get_json()
        print(body)
        if not body: return {"message": "Missing parameters!"}, 400
        if "username" not in body: return {"message": "Missing username!"}, 400
        if "email" not in body: return {"message": "Missing email!"}, 400
        if "password" not in body: return {"message": "Missing password!"}, 400
        
        username = body['username']
        email = body['email']
        password = generate_password_hash(body['password']).decode('utf8')

        try:
            db.executeQuery("INSERT INTO api_users VALUES (?, ?, ?)", params=(email, username, password))
        except Exception as e:
            return {"message": 'Account already exists with that email or username!'}
        return {'message': 'Account succesfully created!'}, 200

# def checkPassword(given_password, hashed_password):
#     return check_password_hash(given_password, hashed_password)
