from db import db
import sys
from bson import ObjectId
from flask import jsonify, make_response

def fetch_data_api(cookie):
    users_collection = db["users"]
    
    
    user = users_collection.find_one({"_id": ObjectId(cookie)})
    print(user)
    
    if user:
        res = make_response(user["data"])
    else:
        res = make_response({"message":'Failed'})
    
    return res