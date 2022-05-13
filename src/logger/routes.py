from flask import Flask, jsonify, request, session, redirect, Response, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS, cross_origin
from bson import json_util
from __main__ import app
from app import mongo
import uuid


@cross_origin
@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({
        'username' : request.json['username']
        })
    if login_user:
        if check_password_hash(login_user['password'], request.json['password']):
            session['username'] = login_user['username']
            session['id'] = login_user['id']
            return redirect(url_for('dashboard'))
    response = jsonify({'messsage': 'Invalid username/password combination'})
    return response

@cross_origin
@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect(url_for('home'))