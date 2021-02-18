import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["testtables"]
mycol = mydb["students"]
myquery = { "rollno": "195" }
newvalues = { "$set": { "rollno": "165" } }
=mycol.update_many(myquery, newvalues)

