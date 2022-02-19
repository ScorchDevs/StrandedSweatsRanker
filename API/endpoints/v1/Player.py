from unittest import skip
import database_interface as db
from flask_restful import Resource
from flask import request
from endpoints.v1.Weights import Weights
from static.CONSTANTS import *

class Players(Resource):
    def get(self):
        try:
            return {"data": db.selectQuery("SELECT * FROM players INNER JOIN profiles ON (players.uuid = profiles.uuid)")}
        except Exception as e:
            return {"data": []}, 400

class Player(Resource):
    def get(self, uuid):
        try:
            return {"data": getPlayerStatsFromDatabase(uuid)}, 200
        except:
            return {"message": USER_NOT_FOUND}, 400

class PlayerWeight(Resource):
    def get(self, uuid):
        try:
            return {"data": getPlayerWeightsFromDatabase(uuid)}
        except Exception as e:
            print(e)
            return {"message": USER_NOT_FOUND}, 400


def getPlayerStatsFromDatabase(UUID: str):
    return db.selectQuery("SELECT * FROM stats INNER JOIN profiles p ON (p.profileid = stats.profileid) WHERE p.uuid = ?", params=(UUID, ))


def getPlayerWeightsFromDatabase(UUID: str):
    weights = db.selectQuery("SELECT * FROM weights")[0]
    player_values = getPlayerStatsFromDatabase(UUID)
    out = []
    for player_value in player_values:
        player_weights = {}
        total = 0
        skip_keys = ["uuid", "profileid", "collecttime", "username"]
        for key in player_value:
            if key in skip_keys: continue
            player_weights['profileid'] = player_value['profileid']
            weight = weights[key + "_weight"]
            max_value = weights[key + "_max"]
            value = player_value[key]
            player_weights[key] = (value/max_value) * weight
            total += player_weights[key]
        player_weights["total_weight"] = total
        out.append(player_weights)
    return out