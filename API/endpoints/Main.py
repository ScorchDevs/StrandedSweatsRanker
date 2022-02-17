import database_interface as db
from flask_restful import Resource

class Main(Resource):
    def get(self):
        return {"data": db.selectQuery("SELECT * FROM Weights ORDER BY VERSION DESC LIMIT 1")}