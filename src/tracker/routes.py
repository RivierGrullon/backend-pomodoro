from flask import Flask, jsonify, request, Response
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager
from flask_cors import CORS, cross_origin
from datetime import datetime
from bson import json_util
from __main__ import app
from app import mongo

@cross_origin
@app.route('/createpomodoro', methods=['POST'])
@jwt_required(optional=False)
def create_pomodoro():
    username = get_jwt_identity()
    if username:
        if mongo.db.users.find_one({ "username": username }):
            date_time = datetime.now()
            title = request.json['title']
            description = request.json['description']
            total_pomo = request.json['total_pomo']
            type_pomo = request.json['type_pomo']
        else:
            response = jsonify({ "error":"the provided user does not exist" })
            response.status_code=401
            return response

        if username  and date_time and title and description and total_pomo and type_pomo:

            if int(total_pomo)> 0:
                mongo.db.pomodoro.insert_one({
                    'username': username,
                    'date_time' : date_time,
                    'title' : title,
                    'description' : description,
                    'type_pomo': type_pomo,
                    'total_pomo' : total_pomo
                    })
                response = jsonify({"msg": "pomodoro created successfully"})
                response.status_code=200
                return response
            else:
                response = jsonify({ "error":"must save at least 1 full pomodoro." })
                response.status_code=403
                return response
        else:
            response = jsonify({"error": "data could not be captured"})
            response.status_code=401
            return response
    else:
        response = jsonify({"error": "user not found"})
        response.status_code=401
        return response
#'''
#@cross_origin
#@app.route('/gettracker', methods=['GET'])
#@jwt_required(optional=False)
#def get_tracker():
#    tracker =  mongo.db.pomodoro.aggregate( [
#   {
#     "$lookup":
#       {
#         "from": "users",
#         "localField": "username",
#         "foreignField": "username",
#         "as": "users and pomodoros"
#       }
#  }
#] )
#    response = json_util.dumps(tracker)
#    return Response(response, mimetype='application/json')
#
#'''
@cross_origin
@app.route('/getpomodoro', methods=['GET'])
@jwt_required(optional=False)
def get_pomodoro():
    username = get_jwt_identity()
    if username:
        pomo = mongo.db.pomodoro.find({'username': username})
        response = json_util.dumps(pomo)
        return Response(response, mimetype='application/json')
    else:
        response = jsonify({"error": "user not found"})
        response.status_code=401
        return response