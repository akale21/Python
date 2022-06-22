"""When finding documents in a collection, you can filter the result by using a query object."""

import pymongo

connectionString = "mongodb+srv://Shubh:<password>@cluster0.tt98tdj.mongodb.net/test"

myclient = pymongo.MongoClient(connectionString)

mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# # Find document(s) with the address "Park Lane 38"
# myquery = { "address": "Park Lane 38" }
#
# mydoc = mycol.find(myquery)
#
# for x in mydoc:
#   print(x)

# # Find documents where the address starts with the letter "S" or higher
# myquery = { "address": { "$gt": "S" } }
#
# mydoc = mycol.find(myquery)
#
# for x in mydoc:
#   print(x)

# Find documents where the address starts with the letter "S":
myquery = { "address": { "$regex": "^S" } }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)