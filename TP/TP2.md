# Exercice 1

```shell
db.users_tp2.find().limit(5).pretty()
```

```shell
db.users_tp2.renameCollection("users")
```

# Exercice 2

```shell
mongoimport -u vv224843 -p vv224843 --db vv224843 --collection dblp --file dblp_sgd.json --jsonArray --host mongo2.iem
```

# Exercice 3 

```shell
mongoimport -u vv224843 -p vv224843 --db vv224843 --collection restaurant --file restaurant_sgd.json --host mongo2.iem
```

### Afficher les restaurants proposant de la cuisine brésilienne (« Brazilian ») dans le quartier de Brooklyn dont le code postal n'est ni 11230 ni 11234.

```shell
db.restaurant.find({$and:[{"cuisine":"Brazilian"},{"borough":"Brooklyn"}]})
```

```shell
db.restaurant.find({"cuisine":"Brazilian","borough":"Brooklyn","address.zipcode":{$ne:11230}})
```

```shell
db.restaurant.find({"cuisine":"Brazilian","borough":"Brooklyn","address.zipcode":{$nin:[11230,11234]}})
```

### Combien de restaurants du Bronx n'ont que des notes inférieures à 13 ?

```shell
db.restaurant.find({"borough":"Bronx", "grades.score":{$not: {$gte: 13}}}).count()
```

### Afficher les trois restaurants du Queens qui ont un avis A avec la note 12 ainsi qu'un avis C avec la note 59.


```shell
db.restaurant.find({
    "borough":"Queens", 
    $and:[
        {"grades.grade":"A", "grades.score":12},
        {"grades.grade":"C", "grades.score":59}
    ]
})
```

### Afficher uniquement les noms des restaurants du Bronx dont la latitude est inférieure à 73.94 ou bien dont la longitude est supérieure à 40.62.