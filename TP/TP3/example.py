from pymongo import MongoClient
from bson.objectid import ObjectId
from pprint import pprint

def main():
    c=MongoClient("mongo2.iem", port=27017, username="vv224843", password="vv224843", authSource="vv224843", authMechanism="SCRAM-SHA-1")
    db=c.vv224843   
    print(db.personnes.find_one({"nom" : "Durand"}))
    
    collection = db.ventes
    print(collection.find_one())

    col = db.restaurant
    for doc in col.find(): print(doc)

if __name__ == "__main__":
    main()