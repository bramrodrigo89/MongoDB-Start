import pymongo
import os
import env

# MONGODB_URI = os.getenv("MONGO_URI")
MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
        
conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

new_doc = { 'first':'douglas', 'last':'adams', 'dob':'11/03/1952', 'hair_color':'grey', 'occupation':'writer', 'nationality':'english' }
new_docs = [{ 'first':'terry', 'last':'pratchett', 'dob':'28/04/1984', 'gender':'m','hair_color':'not much', 'occupation':'writer', 'nationality':'english' }, { 'first':'george', 'last':'rr martin', 'dob':'20/09/1948', 'gender':'m', 'hair_color':'white', 'occupation':'writer', 'nationality':'american' }]

# To insert only one document
# coll.insert_one(new_doc)

# To insert more than one document
# coll.insert_many(new_docs)

# To find specific data
# documents = coll.find({'first':'douglas'})

# To find all data without filters:
# documents = coll.find()

# To delete specific data
# coll.remove({'first':'douglas'})
# documents = coll.find()

# To update data in the database
# coll.update_one({'first':'douglas', 'last':'adams'},{'$set':{'gender':'x'}})

# To update many docus at the same time
# coll.update_many({'nationality':'american'},{'$set':{'hair_color':'maroon'}})
# documents = coll.find({'nationality':'american'})

documents = coll.find()

for doc in documents:
    print(doc)