from flask import Flask, jsonify, request
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager, unset_jwt_cookies
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS, cross_origin
from __main__ import app
from app import mongo, jwt

@cross_origin
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    users = mongo.db.users
    login_user = users.find_one({'username' : username})
    if login_user:
        if check_password_hash(login_user['password'], password):
            access_token = create_access_token(identity=username)
            response = jsonify(access_token=access_token)
            return response
        response = jsonify({'messsage': 'Invalid username/password combination'})
        return response
    response = jsonify({'messsage': 'User not found'})
    return response

@cross_origin
@app.route("/logout", methods=["POST"])
@jwt_required(optional=False)
def logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response