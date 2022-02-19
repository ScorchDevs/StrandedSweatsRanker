import database_interface as db
from flask_restful import Resource
from static.CONSTANTS import *

class Main(Resource):
    def get(self):
        return {"status": API_READY}, 200