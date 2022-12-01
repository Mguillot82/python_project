# import du module psycopg2
from psycopg2 import DatabaseError, InterfaceError, connect


# ---------------------------------------------------------------------------------
def connexion(host: str, database: str, login: str, pwd: str):
    # connecte puis déconnecte (login,pwd) de la base [database] du serveur [host]
    # lance l'exception DatabaseError si problème
    connexion = None
    try:
        # connexion
        connexion = connect(host=host, user=login, password=pwd, database=database)
        print(
            f"Connexion réussie à la base database={database}, host={host} sous l'identité user={login}, passwd={pwd}")
    finally:
        # on ferme la connexion si elle a été ouverte
        if connexion:
            connexion.close()
            print("Déconnexion réussie\n")


# ---------------------------------------------- main
# identifiants de la connexion
USER = "admpersonnes"
PASSWD = "nobody"
HOST = "localhost"
DATABASE = "dbpersonnes"

# connexion d'un utilisateur existant
try:
    connexion(host=HOST, login=USER, pwd=PASSWD, database=DATABASE)
except (InterfaceError, DatabaseError) as erreur:
    # on affiche l'erreur
    print(erreur)

# connexion d'un utilisateur inexistant
try:
    connexion(host=HOST, login="xx", pwd="yy", database=DATABASE)
except (InterfaceError, DatabaseError) as erreur:
    # on affiche l'erreur
    print(f"Erreur de connexion à la base [{DATABASE}] par l'utilisateur [xx/yy]")
