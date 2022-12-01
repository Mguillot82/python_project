import config

config = config.configure()

# imports
from ImpotsError import ImpotsError

# on récupère les couches de l'application (elles sont déjà instanciées)
dao = config["dao"]
metier = config["metier"]

try:
    # récupération des tranches de l'impôt
    admindata = dao.get_admindata()
    # lecture des données des contribuables
    taxpayers = dao.get_taxpayers_data()["taxpayers"]
    # des contribuables ?
    if not taxpayers:
        raise ImpotsError(51, f"Pas de contribuables valides dans le fichier {config['taxpayersFilename']}")
    # calcul de l'impot des contribuables
    for taxpayer in taxpayers:
        # taxpayer est à la fois un paramètre d'entrée et de sortie
        # taxpayer va être modifié
        metier.calculate_tax(taxpayer,admindata)
    # ecriture des résultats dans un fichier texte
    dao.write_taxpayers_results(taxpayers)
except ImpotsError as erreur:
    # affichage de l'erreur
    print(f"L'erreur suivante s'est produite : {erreur}")
finally:
    # terminé
    print("Travail terminé...")