import pymongo
import sys

connection_string = "mongodb+srv://yohcho:X2n4xmkB4XDs8DQ2@cluster0.inogbac.mongodb.net/"
db = pymongo.MongoClient(connection_string)["VHA"]

print(db,file=sys.stderr)