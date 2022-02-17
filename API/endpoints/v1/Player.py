from unittest import skip
import database_interface as db
from flask_restful import Resource
from flask import request

from endpoints.v1.Weights import Weights

class Players(Resource):
    def get(self):
        try:
            return {"data": db.selectQuery("SELECT players.UUID, players.username, profiles.profileID FROM players LEFT JOIN profiles ON (Players.UUID = profiles.UUID)")}
        except Exception as e:
            print(e)
            return {"data": []}

class Player(Resource):
    def get(self, uuid):
        try:
            return {"data": getPlayerStatsFromDatabase(uuid)}
        except:
            return {"data": {}}

class PlayerWeight(Resource):
    def get(self, uuid):
        # try:
            return {"data": getPlayerWeightsFromDatabase(uuid)}
        # except:
        #     return {"data": {}}


def getPlayerStatsFromDatabase(UUID: str):
    return db.selectQuery("SELECT * FROM stats LEFT JOIN players p ON (p.UUID = stats.UUID) WHERE p.UUID = ?", params=(UUID, ))[0]


def getPlayerWeightsFromDatabase(UUID: str):
    weights = db.selectQuery("SELECT * FROM weights")[0]
    player_values = getPlayerStatsFromDatabase(UUID)

    player_weights = {}
    total = 0
    skip_keys = ["UUID", "profileID", "collectTime", "username"]
    for key in player_values:
        if key in skip_keys: continue
        weight = weights[key]
        max_value = weights[key + "_max"]
        value = player_values[key]
        player_weights[key] = (value/max_value) * weight
        total += player_weights[key]
    player_weights["total_weight"] = total
    return player_weights