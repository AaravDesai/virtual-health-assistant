from db import db
import sys
from bson import ObjectId
from flask import jsonify, make_response

def fetch_data_api(cookie, isHome):
    users_collection = db["users"]
    user = users_collection.find_one({"_id": ObjectId(cookie)})
    user["data"]["username"] = user["username"]
    
    if user:
        if isHome:
            user["data"]["diet_plan"] = user["diet_plan"]
            user["data"]["workout_plan"] = user["workout_plan"]
        res = make_response(user["data"])
    else:
        res = make_response({"message":'Failed'})
    
    return res