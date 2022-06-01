from flask import Flask, request, jsonify, Response
from flask_pymongo import PyMongo
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager
from flask_cors import CORS, cross_origin
from datetime import timedelta


app = Flask(__name__)

# Setup Flask-JWT-Extended
ACCESS_EXPIRES = timedelta(hours=4)
app.config["JWT_SECRET_KEY"] = "ghdbytD57Kyga5873OKHSDF957"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = ACCESS_EXPIRES
jwt = JWTManager(app)

# Cross Origin
CORS(app)

# Setup Database
app.config['MONGO_URI']='mongodb://127.0.0.1:27017/pomodorodb'
mongo = PyMongo(app)

# Routes
@cross_origin
@app.route('/')
@app.route('/home')
@jwt_required(optional=True)
def home():
    current_identity = get_jwt_identity()
    if current_identity:
        response = jsonify(logged_in_as=current_identity)
        return response
    else:
        response = jsonify(logged_in_as="anonymous user")
        return response

@cross_origin
@app.route("/dashboard/")
@jwt_required(optional=False)
def dashboard():
    current_user = get_jwt_identity()
    response = jsonify(logged_in_as=current_user)
    return response


from user import routes
from auth import routes


if __name__=="__main__":
	app.run(debug=True)
