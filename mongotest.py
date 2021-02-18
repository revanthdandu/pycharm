import pymongo
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['testtables']
mycol = mydb["students"]
mydict = { "name": "kumar", "rollno": "192" ,"contact":"8790588214", "age" :"19" , "email" : "revanthdandu99@gmail.com" }
x = mycol.insert_one(mydict)
print(x)
