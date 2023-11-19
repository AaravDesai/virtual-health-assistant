from db import db
import sys
from bson import ObjectId
from flask import jsonify, make_response

def update_data_api(args):
    users_collection = db["users"]
    
    cookie = ObjectId(args["cookie"])
    del args["cookie"]
    args["needsAction"] = False
    print(args,cookie,file=sys.stderr)
    
    users_collection.update_one({"_id": cookie},{"$set":{"data":args}})
        
    return make_response({"message":'Success'})