from pymongo import MongoClient
from bson.objectid import ObjectId
from pprint import pprint

def main():
    c=MongoClient("mongo2.iem", port=27017, username="vv224843", password="vv224843", authSource="vv224843", authMechanism="SCRAM-SHA-1")
    db=c.vv224843  

    """
    productObject = {
        "_id": ObjectId("4c4b1476238d3b4dd5003981"),
        "slug": "wheel-barrow-9092",
        "sku": "9092", 
        "name": "Extra Large Wheel Barrow", 
        "description": "Heavy duty wheel barrow...",
        "details": {
            "weight": 47, 
            "weight_units": "lbs", 
            "model_num": 4039283402, 
            "manufacturer": "Acme",
            "color": "Green",
        },
        "total reviews": 4, 
        "average_review": 4.5, 
        "pricing": { 
            "retail": 5897, 
            "sale": 4897
        }, 
        "price_history": [{ 
            "retail": 5297, 
            "sale": 4297, 
            "start": "2010-05-01T00:00:00.000-0700",
            "end": "2010-05-08T00:00:00.000-0700"
        },
        { 
            "retail": 5297,
            "sale": 5297,
            "sale": 4297, 
            "start": "2010-05-01T00:00:00.000-0700",
            "end": "2010-05-08T00:00:00.000-0700"
        }],
        "category_ids": [
            ObjectId("6a5b1476238d3b4dd5000048"), 
            ObjectId("6a5b1476238d3b4dd5000049"),
        ],
        "main_cat_id": ObjectId("6a5b1476238d3b4dd5000048"), 
        "tags":["tools", "gardening", "soil"],
    }
    db.products.insert_one(productObject)
    
    categorieObject = {
        "_id": ObjectId( "6a5b1476238d3b4dd5000048" ),
        "slug": "gardening-tools",
        "ancestors": [{
            "name": "Home",
            "_id": ObjectId( "8b87fb1476238d3b4dd50003" ),
            "slug": "home"
        },
        {
            "name": "Outdoors",
            "_id": ObjectId( "9a9fb1476238d3b4dd500001" ),
            "slug": "outdoors"
        }],
        "parent_id": ObjectId( "9a9fb1476238d3b4dd500001" ),
        "name": "Gardening Tools",
        "description": "Gardening gadgets galore!"
    }
    db.categories.insert_one(categorieObject)

    userObject = {
        "_id": ObjectId( "4c4b1476238d3b4dd5000001" ),
        "username": "kbanker",
        "email": "kylebanker@gmail.com",
        "first_name": "Kyle",
        "last_name": "Banker",
        "hashed_password": "bd1cfa194c3a603e7186780824b04419",
        "addresses": [{
            "name": "home",
            "street": "588 5th Street",
            "city": "Brooklyn",
            "state": "NY",
            "zip": 11215
        },
        {
            "name": "work",
            "street": "1 E. 23rd Street",
            "city": "New York",
            "state": "NY",
            "zip": 10010
        }
        ],
            "payment_methods": [{
            "name": "VISA",
            "last_four": 2127,
            "crypted_number": "43f6ba1dfda6b8106dc7",
            "expiration_date": "2016-05-01T00:00:00.000-0700"
        }]
    }
    db.users.insert_one(userObject)

    reviewObject = {
        "_id": ObjectId( "4c4b1476238d3b4dd5000041" ),
        "product_id": ObjectId( "4c4b1476238d3b4dd5003981" ),
        "date": "2010-06-07T00:00:00.000-0700",
        "title": "Amazing",
        "text": "Has a squeaky wheel, but still a darn good wheel barrow.",
        "rating": 4,
        "user_id": ObjectId( "4c4b1476238d3b4dd5000001" ),
        "username": "dgreenthumb",
        "helpful_votes": 3,
        "voter_ids": [
            ObjectId( "4c4b1476238d3b4dd5000041" ),
            ObjectId( "7a4f0376238d3b4dd5000003" ),
            ObjectId( "92c21476238d3b4dd5000032" )
        ]
    }
    db.reviews.insert_one(reviewObject)

    orderObject = {
        "_id": ObjectId( "6a5b1476238d3b4dd5000048" ),
        "user_id": ObjectId( "4c4b1476238d3b4dd5000001" ),
        "purchase_data": "2014-08-01T00:00:00.000-0700",
        "state": "CART",
        "line_items": [
        {
            "_id": ObjectId( "4c4b1476238d3b4dd5003981" ),
            "sku": "9092",
            "name": "Extra Large Wheel Barrow",
            "quantity": 1,
            "pricing": {
                "retail": 5897,
                "sale": 4897
            }
        },
        {
            "_id": ObjectId( "4c4b1476238d3b4dd5003982" ),
            "sku": "10027",
            "name": "Rubberized Work Glove, Black",
            "quantity": 1,
            "pricing": {
                "retail": 1499,
                "sale": 1299
            }
        }
        ],
        "shipping_address": {
            "street": "588 5th Street",
            "city": "Brooklyn",
            "state": "NY",
            "zip": 11215
        },
        "sub_total": 6196,
        "tax": 600
    }
    db.orders.insert_one(orderObject)
    
    """
    results = db.products.find({"category_ids":ObjectId("6a5b1476238d3b4dd5000048")})
    for result in results:
        print(result)

    """    
    pipeline = [
        {"$match":{"year" :{$gte:2011}}},
        {"$group":{"_id":"$type","note":{"$avg":"$UE.note"}}}
    ]
    results = db.etudiants.aggregate(pipeline)
    """
    
if __name__ == "__main__":
    main()