# import du module psycopg2
from psycopg2 import connect, DatabaseError, InterfaceError

# connexion à une base MySql [dbpersonnes]
# l'identité de l'utilisateur est (admpersonnes,nobody)
USER = "admpersonnes"
PWD = "nobody"
HOST = "localhost"
DATABASE = "dbpersonnes"

# c'est parti
connexion = None
try:
    print("Connexion au SGBD MySQL en cours...")
    # connexion
    connexion = connect(host=HOST, user=USER, password=PWD, database=DATABASE)
    # suivi
    print(
        f"Connexion MySQL réussie à la base database={DATABASE}, host={HOST} sous l'identité user={USER}, passwd={PWD}")
except (InterfaceError, DatabaseError) as erreur:
    # on affiche l'erreur
    print(f"L'erreur suivante s'est produite : {erreur}")
finally:
    # on ferme la connexion si elle a été ouverte
    if connexion:
        connexion.close()
