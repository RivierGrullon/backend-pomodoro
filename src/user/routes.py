from flask import Flask, jsonify, request, session, redirect, Response, url_for
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS, cross_origin
from bson import json_util
from __main__ import app
from app import mongo, jwt

@cross_origin
@app.route('/getuser/', methods=['GET'])
@jwt_required(optional=False)
def get_user():
    username = get_jwt_identity()
    if username:
        user = mongo.db.users.find_one({'username': username})
        response = json_util.dumps(user)
        return Response(response, mimetype='application/json')
    else:
        response = jsonify({"error": "user not found"})
        response.status_code=401
        return response

@cross_origin
@app.route('/createuser', methods=['POST'])
@jwt_required(optional=True)
def create_user():
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    if email and username and password :
        #check minimum password length
        if len(password) < 7:
            response = jsonify({ "error":"Password must be at least 7 characters." })
            response.status_code=403
            return response
        #hash the password
        hashed_password = generate_password_hash(password)
        #if email exist
        if mongo.db.users.find_one({ "email": email }):
            response = jsonify({ "error":"Email address already in use" })
            response.status_code=403
            return response
        #if username exist
        if mongo.db.users.find_one({ "username": username }):
            response = jsonify({ "error":"username already in use" })
            response.status_code=403
            return response
        mongo.db.users.insert_one({
            'email' : email,
            'username' : username,
            'password' : hashed_password
            })
        response = jsonify({"msg": "user created successfully"})
        response.status_code=200
        return response
    else:
        response = jsonify({"error": "data could not be captured"})
        response.status_code=401
        return response

@cross_origin
@app.route('/updatepassword', methods=['PUT'])
@jwt_required(optional=False)
def update_password():
    username = get_jwt_identity()
    password = request.json['password']
    if username and password :
         #check minimum password length
        if len(password) < 7:
            response = jsonify({ "error":"Password must be at least 7 characters." })
            response.status_code=403
            return response
        #hash the password
        hashed_password = generate_password_hash(password)
        #search for usrname
        if mongo.db.users.find_one({ "username": username }):
            mongo.db.users.update_one({'username': username}, {'$set':{
                'password': hashed_password,
            }})
            response = jsonify({'messsage': ' user: ' + username + ' has updated the password'})
            response.status_code=200
            return response
    else:
        response = jsonify({"error": "data could not be captured"})
        response.status_code=401
        return response