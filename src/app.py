from flask import Flask
from dotenv import load_dotenv
from flask import request, jsonify, Response
from flask_pymongo import PyMongo, pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager
from flask_cors import CORS, cross_origin
from datetime import timedelta
import os


app = Flask(__name__)

#dotenv
load_dotenv()

# Setup Flask-JWT-Extended
ACCESS_EXPIRES = timedelta(hours=4)
app.config["JWT_SECRET_KEY"] = os.getenv('CONFIG_SECRET_KEY')
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = ACCESS_EXPIRES
jwt = JWTManager(app)

# Cross Origin
CORS(app)

# Setup Database
client = pymongo.MongoClient(os.getenv('CONFIG_SECRET_DATABASE'), server_api=ServerApi('1'))
mongo = client.test



# Routes
@cross_origin
@app.route('/')
@jwt_required(optional=True)
def home():
    current_identity = get_jwt_identity()
    if current_identity:
        response = jsonify(logged_in_as=current_identity)
        response.status_code=200
        return response
    else:
        response = jsonify(logged_in_as="anonymous user")
        response.status_code=200
        return response

@cross_origin
@app.route("/dashboard/")
@jwt_required(optional=False)
def dashboard():
    current_user = get_jwt_identity()
    response = jsonify(logged_in_as=current_user)
    response.status_code=200
    return response

from routes import user, auth, tasks, Oauth


if __name__=="__main__":
    app.run(debug=False, port=int(os.environ.get("PORT", 5000)), host='0.0.0.0')
