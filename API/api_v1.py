from flask import Flask
from flask_restful import Api
from endpoints.v1 import *


app = Flask(__name__)
api = Api(app)

api.add_resource(Main.Main, '/v1/')
api.add_resource(Weights.Weight, '/v1/weights/version/<version>')
api.add_resource(Weights.Weights, '/v1/weights/')
api.add_resource(Player.Players, '/v1/players/')
api.add_resource(Player.Player, '/v1/players/<uuid>/stats')
api.add_resource(Player.PlayerWeight, '/v1/players/<uuid>/weights')



if __name__ == '__main__': 
    app.run(port=8000, host='127.0.0.1')