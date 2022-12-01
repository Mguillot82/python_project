# imports
from psycopg2 import connect, DatabaseError, InterfaceError

# l'identité de l'utilisateur
ID = "admpersonnes"
PWD = "nobody"
# la machine hôte du sgbd
HOST = "localhost"
# identité de la base
BASE = "dbpersonnes"

# liste de personnes (nom,prenom,age)
personnes = []
for i in range(5):
    personnes.append((i, f"n0{i}", f"p0{i}", i + 10))
personnes.append((40, "d'Aboot", "Y'éna", 18))
# autre liste de personnes
autresPersonnes = []
for i in range(5):
    autresPersonnes.append((i + 100, f"n1{i}", f"p1{i}", i + 20))
autresPersonnes.append((200, "d'Aboot", "F'ilhem", 34))

# accès au SGBD
connexion = None
try:
    # connexion
    connexion = connect(host=HOST, user=ID, password=PWD, database=BASE)
    # curseur
    curseur = connexion.cursor()
    # suppression des enregistrement existants
    curseur.execute("delete from personnes")
    # insertions personne par personne avec une requête préparée
    for personne in personnes:
        curseur.execute("insert into personnes(id,nom,prenom,age) values(%s,%s,%s,%s)", personne)
    # insertion en bloc d'une liste de personnes
    curseur.executemany("insert into personnes(id,nom,prenom,age) values(%s, %s,%s,%s)", autresPersonnes)
    # validation de la transaction
    connexion.commit()
except (DatabaseError, InterfaceError) as erreur:
    # affichage erreur
    print(f"L'erreur suivante s'est produite : {erreur}")
    # annulation transaction
    if connexion:
        connexion.rollback()
finally:
    # fermeture connexion
    if connexion:
        connexion.close()
