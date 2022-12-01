# on récupère la configuration de l'application
import config_04

config = config_04.configure()

# le syspath est configuré - on peut faire les imports
import sys
from pgres_module import execute_file_of_commands
from psycopg2 import connect, DatabaseError, InterfaceError

# ---------------------------------------------- main
# vérification de la syntaxe de l'appel
# argv[0] true / false
args = sys.argv
erreur = len(args) != 2
if not erreur:
    with_transaction = args[1].lower()
    erreur = with_transaction != "true" and with_transaction != "false"
# erreur ?
if erreur:
    print(f"syntaxe : {args[0]} true / false")
    sys.exit()

# calcul d'un texte
with_transaction = with_transaction == "true"
if with_transaction:
    texte = "avec transaction"
else:
    texte = "sans transaction"

# logs écran
print("--------------------------------------------------------------------")
print(f"Exécution du fichier SQL {config['commands_filename']} {texte}")
print("--------------------------------------------------------------------")

# exécution des ordres SQL du fichier
connexion = None
try:
    # connexion à la bd
    connexion = connect(host=config['host'], user=config['user'], password=config['password'],
                        database=config['database'])
    # exécution du fichier des commandes SQL
    erreurs = execute_file_of_commands(connexion, config["commands_filename"], suivi=True, arrêt=False,
                                       with_transaction=with_transaction)
except (InterfaceError, DatabaseError) as erreur:
    # affichage de l'erreur
    print(f"L'erreur fatale suivante s'est produite : {erreur}")
    # on s'arrête
    sys.exit()
finally:
    # fermeture de la connexion si elle a été ouverte
    if connexion:
        connexion.close()

# affichage nombre d'erreurs
print("--------------------------------------------------------------------")
print(f"Exécution terminée")
print("--------------------------------------------------------------------")
print(f"Il y a eu {len(erreurs)} erreur(s)")
# affichage des erreurs
for erreur in erreurs:
    print(erreur)
