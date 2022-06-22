"""To select data from a collection in MongoDB, we can use the find_one() method.
  To select data from a table in MongoDB, we can also use the find() method."""

import pymongo

connectionString = "mongodb+srv://Shubh:<password>@cluster0.tt98tdj.mongodb.net/test"

myclient = pymongo.MongoClient(connectionString)

mydb = myclient["mydatabase"]
mycol = mydb["customers"]

#for find only one document
# x = mycol.find_one() #we use filter inside brackets
# print(x)
#for find all document
for x in mycol.find():
  print(x)