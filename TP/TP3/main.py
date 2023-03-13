from pymongo import MongoClient
from bson.objectid import ObjectId
from pprint import pprint

def main():
    c=MongoClient("mongo2.iem", port=27017, username="vv224843", password="vv224843", authSource="vv224843", authMechanism="SCRAM-SHA-1")
    db=c.vv224843   

    #Quelle est la moyenne des notes de l'étudiant Boris Karloff ? (en utilisant un « aggregate » puis sans l’utiliser)     
    
    # db.etudiants.aggregate([
    #     {
    #         $match:{nom :'Boris Karloff'},
    #     },
    #     {
    #         "$unwind": "$UE"
    #     },
    #     {
    #         $group:{
    #             _id:"$nom",
    #             note:{$avg:"$UE.note"},
    #         }
    #     }
    # ])
    
    pipeline = [
        {"$match":{"nom" :'Boris Karloff'}},
        {"$unwind": "$UE"},
        {"$group":{"_id":"$nom","note":{"$avg":"$UE.note"}}}
    ]
    results = db.etudiants.aggregate(pipeline)

    for result in results:
        print(result)

    # Quelle est la note maximale obtenue par un étudiant de la collection ? (en utilisant un « aggregate » puis sans l’utiliser)
    
    # db.etudiants.aggregate([
    #     {
    #         "$unwind": "$UE"
    #     },
    #     {
    #         $group:{
    #             _id:"$nom",
    #             note:{$avg:"$UE.note"},
    #         }
    #     },
    #     {
    #         $group:{
    #             _id:"Note max",
    #             note:{$max:"$note"}
    #         }
    #     }
    # ])

    pipeline = [
        {"$unwind": "$UE"},
        {"$group":{"_id":"$nom","note":{"$avg":"$UE.note"}}},
        {"$group":{"_id":"Note max","note":{"$max":"$note"}}}
    ]
    results = db.etudiants.aggregate(pipeline)

    for result in results:
        print(result)

    # Calculer le pourcentage d'étudiants admis (dont la moyenne est supérieure ou égale à 10) (sans « aggregate »)

    nbEtudiantAdmis = 0
    for etudiant in db.etudiants.find():
        nbNote = 0
        sum = 0
        for UE in etudiant["UE"] :
            nbNote+=1
            sum+=UE["note"]
        moy = sum / nbNote
        if moy >= 10 :
            nbEtudiantAdmis+=1
    print(nbEtudiantAdmis)

    # Quel est l'étudiant qui a validé le plus de crédits ECTS ? Afficher son nom et le nombre de crédits validés (sans « aggregate »)

    maxUE = 0
    for etudiant in db.etudiants.find():
        nbUE = 0
        for UE in etudiant["UE"] :
            if UE["note"] >= 10 :
                nbUE+=1
        if nbUE > maxUE :
            maxUE = nbUE
    print(maxUE)

    # Afficher les titres des cours qui n'ont pas de prérequis, sans doublon (en utilisant un « aggregate »)

    # db.etudiants.aggregate([
    #      {
    #          "$unwind": "$UE"
    #      },
    #      {
    #          $group:{
    #              _id:"$UE.id",
    #          }
    #      }
    #  ])

    pipeline = [
        {"$unwind": "$UE"},
        {"$group":{"_id":"$UE.id"}},
    ]
    results = db.etudiants.aggregate(pipeline)

    for result in results:
        print(result)

    # Quel est le nombre de prérequis que doit avoir suivis l'étudiant Marcel Campion ? (en utilisant un « aggregate »)

# db.etudiants.aggregate([
#          {
#              "$unwind": "$UE"
#          },
#          {
#              "$unwind": {
#                  path: "$UE.prerequis",
#                  preserveNullAndEmptyArrays: true
#               }
#          },
#          {
#              $group:{
#                  _id:"$UE.id",
#                  prerequis : {$add:[{$sum: 1},-1]}
#              }
#          }
#      ])
if __name__ == "__main__":
    main()