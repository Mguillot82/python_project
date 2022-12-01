from mysql.connector import DatabaseError, InterfaceError
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor

def afficher_infos(curseur: MySQLCursor):
    print(type(curseur))

    if curseur.description:
        titre = ""
        for i in range(len(curseur.description)):
            titre += curseur.description[i][0] + ", "

        print(titre[0:len(titre)-1])
        print("*" * (len(titre) -1))
        ligne = curseur.fetchone()
        while ligne:
            print(ligne)
            ligne = curseur.fetchone()

            print("*" * (len(titre) -1))
        else:
            # le curseur n'a pas de champs description - il a exécuté un ordre SQL de mise à jour
            print(f"nombre de lignes modifiées : {curseur.rowcount}")
        
def execute_list_of_commands(connexion: MySQLConnection, sql_commands: list,
                             suivi: bool = False, arret: bool = True, with_transaction: bool = True):

    # utilise la connexion ouverte connexion
    # exécute sur cette connexion les commandes SQL à l'extérieur à raison d'une par ligne
    # ce fichier est un fichier de commandes SQL à exécuter à raison d'une par ligne
    # si suivi = True alors chaque exécution d'un ordre SQL fait l'objet d'un affichage indiquant sa réussite ou son échec
    # si arret = True, la fonction s'arrête sur la 1ère erreur rencontrée sinon elle exécute toutes les commandes sql
    # si with_transaction = True alors toute erreur annule l'ensemble des ordres SQL exécutés auparavant
    # si with_transaction = False alors une erreur n'a aucun impact sur les ordres SQL exécutés auparavant
    # la fonction rend une liste erreur1, erreur2

    # initialisations
    curseur = None
    connexion.autocommit = not with_transaction
    erreurs = []
    try:
        curseur = connexion.cursor()
        # exécution des commandes sql
        for command in sql_commands:
            command = command.strip()
            # commande vide ou commentaire ?
            if command == '' or command[0] == "#":
                continue
            error = None
            try:
                curseur.execute(command)
            except (InterfaceError, DatabaseError) as erreur:
                error = erreur
            if error:
                msg = f"{command} : Erreur ({error})"
                erreurs.append(msg)
                if suivi:
                    print(msg)

                if with_transaction or arret:
                    return erreurs
            else:
                if suivi:
                    print(f"[{command}] : Exécution réussie")
                afficher_infos(curseur)
        return erreurs
    finally:
        if curseur:
            curseur.close()
        if with_transaction:
            if erreurs:
                # annulation
                connexion.rollback()
            else:
                # validation
                connexion.commit()

def execute_file_of_commands(connexion: MySQLConnection, sql_filename: str,
                             suivi: bool = False, arret: bool=True, with_transaction: bool=True):

    # utilise la connexion ouverte connexion
    # exécute sur cette connexion les commandes SQL à l'extérieur à raison d'une par ligne
    # ce fichier est un fichier de commandes SQL à exécuter à raison d'une par ligne
    # si suivi = True alors chaque exécution d'un ordre SQL fait l'objet d'un affichage indiquant sa réussite ou son échec
    # si arret = True, la fonction s'arrête sur la 1ère erreur rencontrée sinon elle exécute toutes les commandes sql
    # si with_transaction = True alors toute erreur annule l'ensemble des ordres SQL exécutés auparavant
    # si with_transaction = False alors une erreur n'a aucun impact sur les ordres SQL exécutés auparavant
    # la fonction rend une liste erreur1, erreur2

    # exploitation du fichier sql
    try:
        file = open(sql_filename, "r")
        return execute_list_of_commands(connexion, file.readlines(), suivi, arret, with_transaction)
    except BaseException as erreur:
        return [f"Le fichier {sql_filename} n'a pu être exploité : {erreur}"]