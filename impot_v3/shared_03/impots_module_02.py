import codecs
import json
import math

# revenu_imposable = salaireAnnuel - abattement
# l'abattement a un min et un max
# ---------------------------------------------
# from impot_v3.main_03.main import admindata


def get_revenu_imposable(admin_data: dict, salaire: int) -> int:
    # abattement de 10% du salaire
    abattement = 0.1 * salaire
    # cet abattement ne peut dépasser ABATTEMENT_DIXPOURCENT_MAX
    if abattement > admin_data['ABATTEMENT_DIXPOURCENT_MAX']:
        abattement = admin_data['ABATTEMENT_DIXPOURCENT_MAX']

    # l'abattement ne peut être inférieur à ABATTEMENT_DIXPOURCENT_MIN
    if abattement < admin_data['ABATTEMENT_DIXPOURCENT_MIN']:
        abattement = admin_data['ABATTEMENT_DIXPOURCENT_MIN']

    # revenu imposable
    revenu_imposable = salaire - abattement
    # résultat
    return math.floor(revenu_imposable)

# calcule une réduction éventuelle
def get_reduction(admin_data: dict, marie: str, salaire: int, enfants: int, impots: int) -> int:
    # le plafond des revenus pour avoir droit à la réduction de 20%
    plafond_revenus_pour_reduction = admin_data['PLAFOND_REVENUS_COUPLE_POUR_REDUCTION'] if marie == "oui" else \
        admin_data['PLAFOND_REVENUS_CELIBATAIRE_POUR_REDUCTION']
    plafond_revenus_pour_reduction += enfants * admin_data['VALEUR_REDUC_DEMI_PART']
    if enfants  > 2:
        plafond_revenus_pour_reduction += (enfants - 2) * admin_data['VALEUR_REDUC_DEMI_PART']

    # revenu imposable
    revenu_imposable = get_revenu_imposable(admin_data,salaire )
    # reduction
    reduction = 0
    if revenu_imposable < plafond_revenus_pour_reduction:
        # reduction de 20%
        reduction = 0.2 * impots

    # resultat
    return math.ceil(reduction)

# Calcule une décôte éventuelle
def get_decote(admin_data: dict, marie: str, salaire: int, impots: int) -> int:
    # au départ, une décôte nulle
    decote = 0
    # montant maximal d'impôt pour avoir la décôte
    plafond_impot_pour_decote = admin_data['PLAFOND_IMPOT_COUPLE_POUR_DECOTE'] if marie == "oui" else \
        admin_data['PLAFOND_IMPOT_CELIBATAIRE_POUR_DECOTE']
    if impots < plafond_impot_pour_decote:
        # montant maximal de la décôte
        plafond_decote = admin_data['PLAFOND_DECOTE_COUPLE'] if marie == "oui" else admin_data['PLAFOND_DECOTE_CELIBATAIRE']
        # decote théorique
        decote = plafond_decote - 0.75 * impots
        # la décôte ne peut dépasser le montant de l'impôt
        if decote > impots:
            decote = impots

        # pas de décôte < 0
        if decote < 0:
            decote = 0

        # resultat
    return math.ceil(decote)

# calcul de l'impôt
def calcul_impot(admin_data: dict, marie: str, enfants: int, salaire: int) -> dict :
    # marié : oui, non
    # enfants : nombre d'enfants
    # salaire : salaire annuel
    # limites, coeffr, coeffn : les tableaux des données permettant le calcul de l'impôt
    #
    # calcul de l'impôt avec enfants
    result1 = calcul_impot_2(admin_data, marie, enfants, salaire)
    impot1 = result1['impot']

    # calcul de l'impôt sans les enfants
    if enfants != 0:
        result2 = calcul_impot_2(admin_data, marie, 0, salaire)
        impot2 = result2['impot']
        # application du plafonnement du quotient familial
        if enfants < 3:
            # PLAFOND_QF_DEMI_PART euros pour les 2 premiers enfants
            impot2 = impot2 - enfants * admin_data['PLAFOND_QF_DEMI_PART']
        else:
            # PLAFOND_QF_DEMI_PART euros pour les 2 premiers enfants, le double pour les suivants
            impot2 = impot2 - 2 * admin_data['PLAFOND_QF_DEMI_PART'] - (enfants - 2) * 2 * admin_data['PLAFOND_QF_DEMI_PART']
    else:
        impot2 = impot1
        result2 = result1

        # on prend l'impot le plus fort avec le taux et la surcôte qui vont avec
    if impot1 > impot2:
        impot = impot1
        taux = result1['taux']
        surcote = result1['surcote']
    else:
        surcote = impot2 - impot1 + result2['surcote']
        impot = impot2
        taux = result2['taux']

    # calcul d'une éventuelle décôte
    decote = get_decote(admin_data, marie, salaire, impot)
    impot -= decote

    # calcul d'une éventuelle réduction d'impôts
    reduction = get_reduction(admin_data,marie, salaire, enfants, impot)
    impot -= reduction
    # résultat
    return {"marie": marie, "enfants": enfants, "salaire": salaire, "impot": math.floor(impot), "surcote":surcote,
                "decote": decote, "reduction": reduction, "taux": taux}

# calcul de l'impôt2
def calcul_impot_2(admin_data: dict, marie: str, enfants: int, salaire: int) -> list:

    # marié : oui, non
    # enfants : nombre d'enfants
    # salaire : salaire annuel
    # limites, coeffr, coeffn : les tableaux des données permettant le calcul de l'impôt
    #
    # nombre de parts
    marie = marie.strip().lower()
    if marie == "oui":
        nb_parts = enfants / 2 + 2
    else:
        nb_parts = enfants / 2 + 1

    # 1 part par enfant à partir du 3ème
    if enfants >= 3:
        # une demi-part de + pour chaque enfant à partir du 3ème
        nb_parts += 0.5 * (enfants - 2)

    # revenu imposable
    revenu_imposable = get_revenu_imposable(admin_data,salaire)
    # surcote
    surcote = math.floor(revenu_imposable - 0.9 * salaire)
    # pour les problèmes d'arrondis
    if surcote < 0:
        surcote = 0
    # quotient familial
    quotient = revenu_imposable / nb_parts
    # est mis à la fin du tableau limites pour arrêter la boucle qui suit
    # len(limites) - 1
    admin_data['limites'][len(admin_data['limites'])-1] = quotient
    # Calcul de l'impot
    i = 0
    while quotient > admin_data['limites'][i]:
        i += 1
        # du fait qu'on a placé quotient à la fin du tableau limites, la boucle précédente
    # ne peut déborder du tableau limites

    # maintenant on peut calculer l'impôt
    impot = math.floor(revenu_imposable * admin_data['coeffR'][i] - nb_parts * admin_data['coeffN'][i])
    # résultat
    temp = {"impot": impot, "surcote": surcote, "taux": admin_data['coeffR'][i]}
    return {"impot": impot, "surcote": surcote, "taux": admin_data['coeffR'][i]}

# lecture des données des contribuables
def get_taxpayers_data(taxpayers_filename: str) -> list:
    # lecture des données des contribuables
    file = None
    try:
        # la liste des contribuables
        taxpayers = []
        # ouverture du fichier
        file = codecs.open(taxpayers_filename, "r", "utf8")
        # on lit la première ligne du fichier des contribuables
        ligne = file.readline().strip()
        # tant qu'il reste une ligne à exploiter
        while ligne != '':
            # on récupère les 3 champs marié, enfants, salaire qui forment la ligne
            (marie, enfants, salaire) = ligne.split(",")
            # on les ajoute à la liste des contribuables
            taxpayers.append({"marie":marie.strip().lower(), "enfants": int(enfants), "salaire": int(salaire)})
            # on lit une nouvelle ligne du fichier des contribuables
            ligne = file.readline().strip()
        # on rend le résultats
        return taxpayers
    finally:
        # on ferme le fichier s'il a été ouvert
        if file:
            file.close()

# lecture des données de l'administration fiscale dans un fichier JSON
def get_admindata(admindata_filename: str) -> dict:
    # lecture des données de l'administration fiscale
    # on laisse remonter les éventuelles exceptions : absence de fichier, contenu JSON incorrect
    file = None
    try:
        # ouverture du fichier jSON en lecture
        file = codecs.open(admindata_filename, "r","utf8")
        # transfert du contenu dans un dictionnaire
        admin_data = json.load(file)
        # on rend le résultat
        return admin_data
    finally:
        # fermeture du fichier s'il a été ouvert
        if file:
            file.close()


# écriture des résultats dans un fichier jSON
def record_results_in_json_file(results_filename: str, results: list):

    file = None
    try:
        # ouverture du fichier des résultats
        file = codecs.open(results_filename,"w","utf8")
        # écriture en bloc
        json.dump(results, file, ensure_ascii=False)
    finally:
        # on ferme le fichier s'il a été ouvert
        if file:
            file.close()