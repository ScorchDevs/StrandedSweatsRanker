import database_interface as db
from flask_restful import Resource

class Weights(Resource):
    def get(self):
        return {"data": db.selectQuery("SELECT * FROM Weights ORDER BY VERSION DESC LIMIT 1")}

class Weight(Resource):
    def get(self, version):
        return {"data": db.selectQuery("SELECT * FROM Weights WHERE version = ? ORDER BY version DESC LIMIT 1", params=(version,))}
        