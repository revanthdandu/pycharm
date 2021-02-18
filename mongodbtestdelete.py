import pymongo
connection= pymongo.MongoClient('mongodb://localhost:27017/')
database = connection['testtables']
collection = database['students']
myquery = {"name" : "kumar"}
collection.delete_one(myquery)
