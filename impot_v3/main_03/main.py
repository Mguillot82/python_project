# modules
import config

config = config.configure()

# le syspath est configuré, on peut faire les imports

from impot_v3.shared_03.impots_module_02 import calcul_impot, record_results_in_json_file, get_taxpayers_data, \
    get_admindata

# fichiers des contribuables
taxpayers_filename = config['taxpayersFilename']
# fichier des résultats
results_filename = config['resultsFilename']
# fichier des données de l'administration fiscale
admindata_filename = config['admindataFilename']

# code
try:

    # lecture des données de l'administration fiscale
    admindata = get_admindata(admindata_filename)
    # lecture des données des contribuables
    tax_payers = get_taxpayers_data(taxpayers_filename)
    # liste des résultats
    results = []

    # on calcule l'impôt des contribuables
    for tax_payer in tax_payers:

        # le calcul de l'impôt renvoie un dictionnaire de clés
        # ['marie','enfants','salaire','impôt','surcôte','décôte','réduction','taux']

        result = calcul_impot(admindata, tax_payer['marie'], tax_payer['enfants'], tax_payer['salaire'])
        # le dictionnaire est ajouté à la liste des résultats
        results.append(result)
    # on enregistre les résultats
    record_results_in_json_file(results_filename, results)
except BaseException as erreur:
    # il peut y avoir différentes erreurs : absence de fichiers, contenu de fichiers incorrect
    # on affiche l'erreur et on quitte l'application
    print(f"l'erreur suivante s'est produite : {erreur}]\n")
finally:
    print("Travail terminé...")
