from flask import Flask, jsonify, request, session, redirect, Response, url_for
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS, cross_origin
from bson import json_util
from __main__ import app
from app import mongo, jwt
import uuid

@cross_origin
@app.route('/getusers', methods=['GET'])
@jwt_required(optional=False)
def get_users():
    users = mongo.db.users.find()
    response = json_util.dumps(users)
    return Response(response, mimetype='application/json')

@cross_origin
@app.route('/getuser/<id>', methods=['GET'])
@jwt_required(optional=False)
def get_user(id):
    user = mongo.db.users.find_one({'id': id})
    response = json_util.dumps(user)
    return Response(response, mimetype='application/json')

@cross_origin
@app.route('/deleteuser/<id>', methods=['DELETE'])
@jwt_required(optional=False)
def delete_user(id):
    try:
        mongo.db.users.delete_one({'id': id})
    except:
        return jsonify({'messsage': ' user ' + id + ' not found'})
    return jsonify({'messsage': ' user ' + id + ' was delete'})

@cross_origin
@app.route('/createuser', methods=['POST'])
@jwt_required(optional=True)
def create_user():
    id = uuid.uuid4().hex
    name = request.json['name']
    email = request.json['email']
    username = request.json['username']
    password = request.json['password']
    if name  and email and username and password :
        #check minimum password length
        if len(password) < 7:
            response = jsonify({ "error":"Password must be at least 7 characters." })
            return response
        #hash the password
        hashed_password = generate_password_hash(password)
        #if email exist
        if mongo.db.users.find_one({ "email": email }):
            response = jsonify({ "error":"Email address already in use" })
            return response
        #if username exist
        if mongo.db.users.find_one({ "username": username }):
            response = jsonify({ "error":"username already in use" })
            return response

        mongo.db.users.insert_one({
            'id': id,
            'name' : name,
            'email' : email,
            'username' : username,
            'password' : hashed_password
            })
        response = jsonify({"msg": "user created successfully"})
        return response
    else:
        response = jsonify({"error": "data could not be captured"})
        return response

@cross_origin
@app.route('/updateuser/<id>', methods=['PUT'])
@jwt_required(optional=False)
def update_user(id):
    name = request.json['name']
    email = request.json['email']
    username = request.json['username']
    password = request.json['password']

    if name  and email and username and password :
         #check minimum password length
        if len(password) < 7:
            response = jsonify({ "error":"Password must be at least 7 characters." })
            return response
        #hash the password
        hashed_password = generate_password_hash(password)
        #if email exist
        if mongo.db.users.find_one({ "email": email }):
            response = jsonify({ "error":"Email address already in use" })
            return response
        #if username exist
        if mongo.db.users.find_one({ "username": username }):
            response = jsonify({ "error":"username already in use" })
            return response
        mongo.db.users.update_one({'id': id}, {'$set':{
            'name': name,
            'email': email,
            'username': username,
            'password': hashed_password,
        }})
        response = jsonify({'messsage': ' user ' + id + ' was updated'})
        return response
    else:
        response = jsonify({"error": "data could not be captured"})
        return response