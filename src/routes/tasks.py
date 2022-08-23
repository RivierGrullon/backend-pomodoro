from flask import Flask, jsonify, request, Response
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager
from flask_cors import CORS, cross_origin
from bson import json_util
from app import app
from app import mongo

@cross_origin
@app.route('/createtask', methods=['POST'])
@jwt_required(optional=False)
def create_task():
    username = get_jwt_identity()
    if username:
        if mongo.db.users.find_one({ "username": username }):
            id = request.json['id']
            title = request.json['title']
            pomodorosCount = request.json['pomodorosCount']
            completed = request.json['completed']
        else:
            response = jsonify({ "error":"the provided user does not exist" })
            response.status_code=401
            return response

        if username  and id and title and pomodorosCount and completed:
            try:
                mongo.db.tasks.insert_one({
                    'id' : id,
                    'username': username,
                    'title' : title,
                    'pomodorosCount' : pomodorosCount,
                    'completed' : completed,
                    })
                response = jsonify({"msg": "task created successfully"})
                response.status_code=200
                return response
            except:
                response = jsonify({"error": "an error occurred"})
                response.status_code=401
                return response
        else:
            response = jsonify({"error": "data could not be captured"})
            response.status_code=401
            return response
    else:
        response = jsonify({"error": "user not found"})
        response.status_code=401
        return response

@cross_origin
@app.route('/gettask', methods=['GET'])
@jwt_required(optional=False)
def get_task():
    username = get_jwt_identity()
    if username:
        tasks = mongo.db.tasks.find({'username': username})
        response = json_util.dumps(tasks)
        return Response(response, mimetype='application/json')
    else:
        response = jsonify({"error": "user not found"})
        response.status_code=401
        return response

@cross_origin
@app.route('/deletetask', methods=['DELETE'])
@jwt_required(optional=False)
def delete_task():
    username = get_jwt_identity()
    if username:
        id = request.json['id']
        try:
            mongo.db.tasks.delete_one({'id': id})
            response = jsonify({'messsage': ' task ' + id + ' was delete'})
            response.status_code=200
            return response
        except:
            response = jsonify({'messsage': ' task ' + id + ' not found'})
            response.status_code=401
            return response
    else:
        response = jsonify({"error": "user not found"})
        response.status_code=401
        return response

@cross_origin
@app.route('/updatetask', methods=['PUT'])
@jwt_required(optional=False)
def update_task():
    username = get_jwt_identity()
    if username:
        if mongo.db.users.find_one({ "username": username }):
            id = request.json['id']
            title = request.json['title']
            pomodorosCount = request.json['pomodorosCount']
            completed = request.json['completed']
        else:
            response = jsonify({ "error":"the user to update does not exist" })
            response.status_code=401
            return response

        if id and username and title and pomodorosCount and completed:
            try:
                mongo.db.tasks.update_one({'id': id}, {'$set':{
                    'title' : title,
                    'pomodorosCount' : pomodorosCount,
                    'completed' : completed,
                    }})
                response = jsonify({"msg": "the task was updated"})
                response.status_code=200
                return response
            except:
                response = jsonify({"error": "an error occurred"})
                response.status_code=401
                return response
        else:
            response = jsonify({"error": "data could not be captured"})
            response.status_code=401
            return response
    else:
        response = jsonify({"error": "user not found"})
        response.status_code=401
        return response
