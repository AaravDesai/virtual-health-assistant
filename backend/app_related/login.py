from db import db
import sys
from flask import jsonify, make_response

def login_api(params):
    users_collection = db["users"]
    username = params.get("username")
    password = params.get("password")
    
    user = users_collection.find_one({"username":username,"password":password})
    
    if user:
        cookie = str(user['_id'])
        res = make_response({"message":'Hello, Login!',"cookie":cookie})
        res.set_cookie('auth',cookie,domain='localhost', path='/',samesite='None')
    else:
        res = make_response({"message":'Failed'})
    
    return res