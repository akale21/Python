"""To insert a record, or document as it is called in MongoDB,
into a collection,we use the insert_one() method."""

import pymongo

connectionString = "mongodb+srv://Shubh:<password>@cluster0.tt98tdj.mongodb.net/test"

myclient = pymongo.MongoClient(connectionString)

mydb = myclient["mydatabase"]
mycol = mydb["customers"]

#if we insert only one document so use this

# mydict = {"name": "Shubham", "address": "Highway 38"}
# x = mycol.insert_one(mydict)
# print(x.inserted_id)

# if we insert more tha one document so use this
mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"}
]
x = mycol.insert_many(mylist)
print(x.inserted_ids)