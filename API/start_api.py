from flask import Flask
from flask_restful import Api
from endpoints import *


app = Flask(__name__)
api = Api(app)

api.add_resource(Main.Main, '/')
api.add_resource(Player.Player, '/player/')



if __name__ == '__main__': 
    app.run(port=8000, host='127.0.0.1')