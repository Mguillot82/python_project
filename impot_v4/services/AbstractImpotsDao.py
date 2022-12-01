# imports
import codecs
import json
from abc import abstractmethod

from AdminData import AdminData
from ImpotsError import ImpotsError
from InterfaceImpotsDao import InterfaceImpotsDao
from TaxPayer import TaxPayer

# classe de base pour la couche dao
class AbstractImpotsDao(InterfaceImpotsDao):
    def __init__(self, config: dict):
        # config[taxpayersFilename] : le nom du fichier texte des contribuables
        # config[resultsFilename] : le nom du fichier jSON des résultats
        # config[errorsFilename] : le nom du fichier des erreurs

        # on mémorise les paramètres
        self.taxpayers_filename = config.get("taxpayersFilename")
        self.taxpayers_results_filename = config.get("resultsFilename")
        self.errors_filename = config.get("errorsFilename")

        # interface IImpotsDao

        # liste des données contribuables
    def get_taxpayers_data(self) -> dict:
        # initialisation
        taxpayers_data = []
        datafile = None
        erreurs = []
        try:
            # ouverture du fichier des données
            datafile = open(self.taxpayers_filename, "r")
            # on exploite la ligne courante du fichier
            ligne = datafile.readline()
            # n° de ligne
            numligne = 0
            while ligne != '':
                # une ligne de +
                numligne += 1
                # on enlève les blancs
                ligne = ligne.strip()
                # on ignore les lignes vides et les commentaires
                if ligne != "" and ligne[0] != "#":
                    try:
                        # on récupère les 4 champs id, marié, enfants, salaire qui forment la ligne contribuable
                        (id, marie, enfants, salaire) = ligne.split(",")
                        # on crée un nouveau TaxPayer
                        taxpayers_data.append(
                            TaxPayer().fromdict({'id': id,"marie": marie,"enfants": enfants, "salaire": salaire}))
                    except BaseException as erreur:
                        # on note l'erreur
                        erreurs.append(f"Ligne {numligne}, {erreur}")
                # on lit une nouvelle ligne contribuable
                ligne = datafile.readline()

            # on enregistre les erreurs s'il y en a
            if erreurs:
                text = f"Analyse du fichier {self.taxpayers_filename}\n\n" + "\n".join(erreurs)
                with codecs.open(self.errors_filename, "w","utf-8") as fd:
                    fd.write(text)
            # on rend le résultat
            return {"taxpayers": taxpayers_data, "erreurs": erreurs}
        except BaseException as erreur:
            # on lance une exception ImpotsError
            raise ImpotsError(11, f"{erreur}")
        finally:
            # on ferme le fichier
            if datafile:
                datafile.close()

    # écriture de l'impôt des contribuables
    def write_taxpayers_results(self, taxpayers: list):
        # écriture des résultats dans un fichier jSON
        # taxpayers : liste d'objets de type TaxPayer
        # (id, marie, enfants, salaire, impot, surcote, decote, reduction, taux)
        # la liste taxpayers est enregistrée dans le fichier texte self.taxpayers_results_filename
        file = None
        try:
            # ouverture du fichier des résultats
            file = codecs.open(self.taxpayers_results_filename, "w", "utf8")
            # création de la liste à sérialiser en jSON
            mapping = map(lambda taxpayer: taxpayer.asdict(), taxpayers)
            # sérialisation jSON
            json.dump(list(mapping),file, ensure_ascii=False)
        except BaseException as erreur:
            # on relance l'erreur sous un autre type
            raise ImpotsError(12, f"{erreur}")
        finally:
            # on ferme le fichier s'il a été ouvert
            if file:
                file.close()
    # lecture des tranches de l'impôt
    @abstractmethod
    def get_admindata(self) -> AdminData:
        pass