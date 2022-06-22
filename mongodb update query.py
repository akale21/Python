"""You can update a record, or document as it is called in MongoDB, by using the update_one() method.
To update all documents that meets the criteria of the query, use the update_many() method."""

import pymongo

connectionString = "mongodb+srv://Shubh:<password>@cluster0.tt98tdj.mongodb.net/test"

myclient = pymongo.MongoClient(connectionString)

mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# # Change the address from "Valley 345" to "Canyon 123":
# myquery = { "address": "Park Lane 38" }
# newvalues = { "$set": { "address": "Canyon 123" } }
#
# mycol.update_one(myquery, newvalues)
#
# #print "customers" after the update:
# for x in mycol.find():
#   print(x)

# Update all documents where the address starts with the letter "S":
myquery = { "address": { "$regex": "^S" } }
newvalues = { "$set": { "name": "Minnie" } }

x = mycol.update_many(myquery, newvalues)

print(x.modified_count, "documents updated.")