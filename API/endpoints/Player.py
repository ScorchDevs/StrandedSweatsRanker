import database_interface as db
from flask_restful import Resource
from flask import request

class Player(Resource):
    def get(self):
        return {"data": db.selectQuery("SELECT * FROM Players")}