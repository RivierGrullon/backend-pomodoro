from flask import Flask, request, jsonify, Response, session, redirect, url_for
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson import json_util
from bson.objectid import ObjectId
from functools import wraps
from flask_cors import CORS, cross_origin
import uuid


app = Flask(__name__)

app.secret_key = "key_super_secret"

#cross origin
CORS(app)

#database
app.config['MONGO_URI']='mongodb://127.0.0.1:27017/pomodorodb'
mongo = PyMongo(app)


#routes

@cross_origin
@app.route('/')
def home():
   return "<p>Home</p>"

@cross_origin
@app.route("/dashboard/")
def dashboard():
    return "<p>Dashboard</p>"

@cross_origin
@app.errorhandler(404)
def not_found(error=None):
    message = jsonify({
    'message': 'Resource Not Found: ' + request.url,
    'status': '404'
    })
    message.status_code=404
    return message

from user import routes


if __name__=="__main__":
	app.run(debug=True)
