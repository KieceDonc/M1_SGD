# Exercice 1

## Créer une collection

```shell
db.ventes.insertOne({
     id_auteur:'154',
     nom: 'Gosciny',
     livres:[
        {
            islm:'2154889522',
            titre:'Asterix et Cléopatre',
            Ventes:[
                {
                    id_vente:'10',
                    date:'02/06/2017',
                }
            ],
        }
     ],
   }
)
```

## Voir les collections

```shell
show collections
```

## Voir les valeurs d'une collection

```shell
db.ventes.find()
```

## Trouver une valeur dans la collection

```shell
db.ventes.find({id_auteur:'154'})
```

```shell
db.ventes.find({
   livres:{
      $elemMatch:{
         Ventes:{
            $elemMatch:{
                id_vente:'10'
            }
         }
      }
   }
})
```

```shell
db.ventes.find({'livres.Ventes.id_vente':'10'})
```

```shell
db.ventes.find({'livres.Ventes.id_vente':'10', 'livres.Ventes.date':'02/06/2017',})
```

# Exercice 2

## Création de la collection étudiant

```shell
db.etudiants.insertOne({
 '_id': '6546',
 'nom': 'Marcel Campion',
 'UE': [{'id': 'info1a', 'titre': 'Java', 'note': 06},
 {'id': 'info1b', 'titre': 'Web', 'note': 15},
 {'id': 'info4c', 'titre': 'Fondements de l\'informatique', 'note': 04}
 ]
})
```

```shell
db.etudiants.insertOne({
 '_id': '3215',
 'nom': 'Boris Karloff',
 'UE': [{'id': 'info2a', 'titre': 'Programmation orientée objet', 'note': 17},
 {'id': 'info2b', 'titre': 'Interfaces visuelles', 'note': 06},
 {'id': 'info1b', 'titre': 'Web', 'note': 12}
 ]
})
```

## Update sur une valeur

```shell
db.etudiants.update({'_id':'3215'},{$set:{'nom':'Boris Karlof'}})
```

## Update sur plusieurs valeurs

```shell
db.etudiants.updateMany({'nom':'Boris'},{$set:{'nom':'Boris Karlof'}})
```

## Delete

```shell
db.etudiants.remove({'_id':'3215'})
```

# Exercice 3

## Drop une collection

```shell
db.etudiants.drop({})
```

## Création d'une collection

```shell
db.etudiants.insertOne({
    'nom':'for4ever',
    'prenom':'michel',
    'adresse':{
        'numero_rue':'82',
        'rue':'Bd de Clichy',
        'ville':'Paris',
        'code':75018,
    },
    cours:[{
        'code':69,
        'titre': 'Cours de salsa',
        'description' : 'Cours de salsa très dur et pas chère',
        'credit':69420,
        'code postal' : 43,        
    }]
})
```
