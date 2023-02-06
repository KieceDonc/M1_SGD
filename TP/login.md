# Accès au serveur mongo2

    ssh vv224843@mongo2

# Connexion à la base de données

    mongo –u vv224843 –p vv224843 --authenticationDatabase vv224843 -host mongo2.iem

# puis

    use vv224843 → pour fixer la base de travail

mongoimport –u vv224843 –p vv224843 --db vv224843 --collection users_tp2 --file users_sgd.json --host mongo2.iem