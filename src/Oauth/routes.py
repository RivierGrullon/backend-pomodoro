'''
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from authlib.integrations.flask_client import OAuth
from __main__ import app
#from app import mongo, jwt


oauth = OAuth(app)
github = oauth.register('github', {...})

@app.route('/github_login')
def github_login():
    redirect_uri = url_for('authorize', _external=True)
    return github.authorize_redirect(redirect_uri)

@app.route('/github_authorize')
def github_authorize():
    token = github.authorize_access_token()
    # you can save the token into database
    profile = github.get('/user', token=token)
    return jsonify(profile)
'''