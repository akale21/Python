"""To delete one document, we use the delete_one() method.
To delete more than one document, use the delete_many() method."""

import pymongo

connectionString = "mongodb+srv://Shubh:<password>@cluster0.tt98tdj.mongodb.net/test"

myclient = pymongo.MongoClient(connectionString)
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# # Delete the document with the address "Mountain 21":
# myquery = { "address": "Mountain 21" }
# mycol.delete_one(myquery)

# # Delete all documents were the address starts with the letter S:
# myquery = { "address": {"$regex": "^S"} }
#
# x = mycol.delete_many(myquery)
#
# print(x.deleted_count, " documents deleted.")

# Delete all documents in a collection
x = mycol.delete_many({})
print(x.deleted_count, " documents deleted.")