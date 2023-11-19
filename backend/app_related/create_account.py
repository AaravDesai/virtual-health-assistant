from db import db
from flask import jsonify

def create_account_api(params):
    users_collection = db["users"]
    username = params.get("username")
    password = params.get("password")
    
    new_user = {
        "username":username,
        "password":password,
        "data":{
            "gender":"",
            "height":"",
            "weight":0,
            "age":0,
            "fitnessGoal":"",
            "experience":"",
            "dietaryRestriction":"",
            "includeSupplements":True,
            "numDays":0,
            "needsAction":True 
        }
    }
    
    users_collection.insert_one(new_user)
    
    return jsonify({"message":'Hello, Signup!'})