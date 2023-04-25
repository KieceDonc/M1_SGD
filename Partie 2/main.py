from pymongo import MongoClient
from bson.objectid import ObjectId
from pprint import pprint

def main():
    c=MongoClient("mongo2.iem", port=27017, username="vv224843", password="vv224843", authSource="vv224843", authMechanism="SCRAM-SHA-1")
    db=c.vv224843  

    # ------------------------------------------------------------------------------
    films = {} # hashmap pour les films, clée = id d'un film, valeur = titre d'un film
    for result in db.films.find({}):
        films[result["_id"]] = result["titre"]

    # ------------------------------------------------------------------------------
    print("Liste de films dans la catégorie Science-fiction :")
    for result in db.films.find({"categorie": "Science-fiction"}):
        print("\t"+films[result["_id"]])
    print("\n\n")

    # ------------------------------------------------------------------------------
    print("Nombre total d'entrées pour chaque film  :")
    pipeline = [
        {"$unwind": "$diffusions"},
        {"$group": {"_id": "$diffusions.filmID", "total_entrees": {"$sum": "$diffusions.entrees"}}}
    ]
    for result in db.diffusions.aggregate(pipeline):
        print("\t"+str(result["total_entrees"])+" entrées pour "+films[result["_id"]])
    print("\n\n")

    # ------------------------------------------------------------------------------
    print("Nombre de commentaires pour chaque film ")
    pipeline = [
        {"$group": {"_id": "$filmID", "nombre_commentaires": {"$sum": 1}}}
    ]
    for result in db.commentaires.aggregate(pipeline):
        print("\t"+str(result["nombre_commentaires"])+" commentaires pour "+films[result["_id"]])
    print("\n\n")

    # ------------------------------------------------------------------------------
    print("Films les plus populaires (ceux avec le plus grand nombre d'entrées) ")
    pipeline = [
        {"$unwind": "$diffusions"},
        {"$group": {"_id": "$diffusions.filmID", "total_entrees": {"$sum": "$diffusions.entrees"}}},
        {"$sort": {"total_entrees": -1}},
        {"$limit": 10}
    ]
    index = 1;
    for result in db.diffusions.aggregate(pipeline):
        print("\t"+str(index)+". "+films[result["_id"]])
        index+=1
    print("\n\n")

    # ------------------------------------------------------------------------------
    print("Moyenne des notes pour chaque film")
    pipeline = [
        {"$group": {"_id": "$filmID", "moyenne_notes": {"$avg": "$note"}}}
    ]
    for result in db.notes.aggregate(pipeline):
        print("\t"+str(result["moyenne_notes"])+"/5 pour "+films[result["_id"]])
    print("\n\n")
    
    # ------------------------------------------------------------------------------
    print("Tous les films qui ont été projetés au moins une fois dans chaque cinéma ")
    pipeline = [
        {"$unwind": "$diffusions"},
        {"$group": {"_id": {"cinema": "$cinema", "filmID": "$diffusions.filmID"}}},
        {"$group": {"_id": "$_id.filmID", "count": {"$sum": 1}}},
        {"$match": {"count": {"$eq": 3}}}
    ]
    for result in db.diffusions.aggregate(pipeline):
        print("\t"+films[result["_id"]])
    print("\n\n")

    # ------------------------------------------------------------------------------
    print("Nombre total d'entrées pour chaque cinéma")
    pipeline = [
        {"$unwind": "$diffusions"},
        {"$group": {"_id": "$cinema", "total_entrees": {"$sum": "$diffusions.entrees"}}}
    ]
    for result in db.diffusions.aggregate(pipeline):
        print("\t"+str(result["total_entrees"])+" pour "+result["_id"])
    print("\n\n")

    # ------------------------------------------------------------------------------
    print("Utilisateurs ayant commenté au moins 5 films différents")
    pipeline = [
        {"$group": {"_id": "$utilisateurID", "nombre_films": {"$addToSet": "$filmID"}}},
        {"$project": {
            "utilisateurID": "$_id",
            "nombre_films": 1,
            "nb_films_different": {"$size": "$nombre_films"}
        }},
        {"$match": {"$expr": {"$gte": ["$nb_films_different", 5]}}}
    ]
    for result in db.diffusions.aggregate(pipeline):
        print("\t"+str(result["total_entrees"])+" pour "+result["_id"])
    print("\n\n")
if __name__ == "__main__":
    main()