# imports
import re

from InterfaceImpôtsUi import InterfaceImpôtsUi
from TaxPayer import TaxPayer


# couche [UI]
class ImpôtsConsole(InterfaceImpôtsUi):
    # constructeur
    def __init__(self, config: dict):
        # on mémorise les paramètres
        self.admindata = config['dao'].get_admindata()
        self.métier = config['métier']

    def run(self):
        # dialogue interactif avec l'utilisateur
        fini = False
        while not fini:
            # le contribuable est-il marié ?
            marié = input("Le contribuable est-il marié / pacsé (oui/non) (* pour arrêter) : ").strip().lower()
            # vérification de la validité de la saisie
            while marié != "oui" and marié != "non" and marié != "*":
                # msg d'erreur
                print("Tapez oui ou non ou *")
                # question de nouveau
                marié = input("Le contribuable est-il marié / pacsé (oui/non) (* pour arrêter) : ").strip().lower()
            # fini ?
            if marié == "*":
                # dialogue terminé
                return
            # nombre d'enfants
            enfants = input("Nombre d'enfants : ").strip()
            # vérification de la validité de la saisie
            if not re.match(r"^\d+$", enfants):
                # msg d'erreur
                print("Tapez un nombre entier positif ou nul")
                # on recommence
                enfants = input("Nombre d'enfants : ").strip()
            # salaire annuel
            salaire = input("Salaire annuel : ").strip()
            # vérification de la validité de la saisie
            if not re.match(r"^\d+$", salaire):
                # msg d'erreur
                print("Tapez un nombre entier positif ou nul")
                # on recommence
                salaire = input("Salaire annuel : ").strip()
            # calcul de l'impôt
            taxpayer = TaxPayer().fromdict({'id': 0, 'marié': marié, 'enfants': int(enfants), 'salaire': int(salaire)})
            self.métier.calculate_tax(taxpayer, self.admindata)
            # affichage
            print(f"Impôt du contribuable = {taxpayer}\n\n")
            # contribuable suivant
