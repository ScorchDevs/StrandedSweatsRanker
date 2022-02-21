import database_interface as db
from flask_restful import Resource
from static.CONSTANTS import *
from flask import request
from endpoints.v1.Auth import checkAdminLogin

class Weights(Resource):
    def get(self):
        return {"data": db.selectQuery("SELECT * FROM Weights ORDER BY VERSION DESC LIMIT 1")}

class WeightsTop(Resource):
    def get(self, name):
        try:
            return {"data": db.selectQuery("SELECT uuid, profileid, %s FROM stats ORDER BY %s DESC" % (name, name))}
        except:
            return {"message": CATEGORY_NOT_FOUND}

class Weight(Resource):
    def get(self, version):
        return {"data": db.selectQuery("SELECT * FROM Weights WHERE version = ? ORDER BY version DESC LIMIT 1", params=(version,))}

    def put(self, version):
        body = request.get_json()
        try:
            admin_logged_in, error = checkAdminLogin(body["authorization"])
        except Exception as e:
            print(e)
            admin_logged_in, error = False, NO_BODY_GIVEN_ERROR
        if not admin_logged_in: return {"message": "Something went wrong: " + error}, 400

        data = body['data']
        data['version'] = version

        try:
            db.executeManyQuery("REPLACE INTO weights VALUES (:version, :farming_weight, :farming_max, :mining_weight, :mining_max, :combat_weight, :combat_max, :foraging_weight, :foraging_max, :fishing_weight, :fishing_max, :enchanting_weight, :enchanting_max, :alchemy_weight, :alchemy_max, :taming_weight, :taming_max, :zombie_weight, :zombie_max, :spider_weight, :spider_max, :wolf_weight, :wolf_max, :enderman_weight, :enderman_max, :minions_weight, :minions_max, :collections_weight, :collections_max)", params=(body['data'],))
            return {"message": "weight version %s created!" % version}
        except:
            return {"message": "Something went wrong..."}
        