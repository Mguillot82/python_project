# imports
import sys

from psycopg2 import DatabaseError, InterfaceError, connect
from psycopg2.extensions import connection


# ---------------------------------------------------------------------------------
def execute_sql(connexion: connection, update: str):
    # exécute une requête de mise à jour sur la connexion
    curseur = None
    try:
        # on demande un curseur
        curseur = connexion.cursor()
        # exécute la requête update sur la connexion
        curseur.execute(update)
    finally:
        # fermeture du curseur s'il a été obtenu
        if curseur:
            curseur.close()


# ---------------------------------------------- main
# identifiants de la connexion
# l'identité de l'utilisateur
ID = "admpersonnes"
PWD = "nobody"
# la machine hôte du sgbd
HOST = "localhost"
# identité de la base
DATABASE = "dbpersonnes"

# on y va étape par étape
try:
    # connexion
    connexion = connect(host=HOST, user=ID, password=PWD, database=DATABASE)
    # mode AUTOCOMMIT
    connexion.autocommit = True
except (InterfaceError, DatabaseError) as erreur:
    # on affiche l'erreur
    print(f"L'erreur suivante s'est produite : {erreur}")
    # on quitte
    sys.exit()

# suppression de la table personnes si elle existe
# si elle n'existe pas une erreur se produira - on l'ignore
requête = "drop table personnes"
try:
    execute_sql(connexion, requête)
except (InterfaceError, DatabaseError):
    pass

# création de la table personnes
requête = "create table personnes (id int PRIMARY KEY, prenom varchar(30) NOT NULL, nom varchar(30) NOT NULL, age integer NOT NULL, " \
          "unique(nom,prenom)) "
try:
    # exécution requête
    execute_sql(connexion, requête)
    # affichage
    print(f"{requête} : requête réussie")
except (InterfaceError, DatabaseError) as erreur:
    # on affiche l'erreur
    print(f"L'erreur suivante s'est produite : {erreur}")
finally:
    # on se déconnecte
    connexion.close()
