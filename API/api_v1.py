from flask import Flask
from flask_restful import Api
from endpoints.v1 import *
from flask import send_from_directory
import os

app = Flask(__name__)
api = Api(app)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

api.add_resource(Main.Main, '/')
api.add_resource(Main.Mainv1, '/v1/')
api.add_resource(Auth.SignUpForAPI, '/v1/auth/signup')
api.add_resource(Auth.AllowUsername, '/v1/auth/allow/<username>')

api.add_resource(Player.Players, '/v1/players/')
api.add_resource(Player.Player, '/v1/players/<uuid>')

api.add_resource(Player.PlayerWeight, '/v1/weights/<uuid>')
api.add_resource(Weights.Weight, '/v1/weights/version/<version>')
api.add_resource(Weights.Weights, '/v1/weights/')
api.add_resource(Weights.WeightsTop, '/v1/weights/top/<name>')


if __name__ == '__main__': 
    app.run(port=20000, host='0.0.0.0')