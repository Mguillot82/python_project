# implémentation de l'interface ui

# imports des couches

from InterfaceDao import InterfaceDao
from InterfaceMetier import InterfaceMetier
from InterfaceUi import InterfaceUi

# autres dépendances
from MyException import MyException

class Console(InterfaceUi):
    # constructeur
    def __init__(self: object, metier: InterfaceMetier):
        # metier : la couche metier

        # on mémorise les attributs
        self.metier = metier

        # interface

    def run(self):
        # dialogue utilisateur
        fini = False
        while not fini:
            # question / réponse
            reponse = input("Numéro de l'élève (>= 1 et * pour arrêter) : ").strip()
            # fini?
            if reponse == "*":
                break
            # a t'on une saisie correcte ?
            ok = False
            try:
                id_eleve = int(reponse, 10)
                ok = id_eleve >=1
            except ValueError as erreur:
                pass
            # donnée correcte ?
            if not ok:
                print("Saisie incorrecte. Recommencez ...")
                continue
            # calcul des statistiques pour l'élève choisi
            try:
                print(self.metier.get_stats_for_eleve(id_eleve))
            except MyException as erreur:
                print(f"L'erreur suivante s'est produite : {erreur}")
