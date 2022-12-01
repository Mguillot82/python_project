# imports
import codecs
import json

from AbstractImpotsDao import AbstractImpotsDao
from AdminData import AdminData
from ImpotsError import ImpotsError


# une implémentation de la couche [dao] où les données de l'administration fiscale sont dans un fichier jSON
class ImpotsDaoWithAdminDataInJsonFile(AbstractImpotsDao):
    # constructeur
    def __init__(self, config: dict):
        # config[admindataFilename] : le nom du fichier jSON contenant les données de l'administration fiscale
        # config[taxpayersFilename] : le nom du fichier texte des contribuables
        # config[resultsFilename] : le nom du fichier jSON des résultats
        # config[errorsFilename] : le nom du fichier des erreurs

        # initialisation de la classe Parent
        AbstractImpotsDao.__init__(self, config)
        # lecture des données de l'administration fiscale
        file = None
        try:
            # ouverture du fichier jSON des données fiscales en lecture
            file = codecs.open(config["admindataFilename"], "r", "utf8")
            # transfert du contenu du fichier jSON dans un objet [AdminData]
            self.admindata = AdminData().fromdict(json.load(file))
        except BaseException as erreur:
            # on relance l'erreur sous la forme d'un type [ImpôtsError]
            raise ImpotsError(21, f"{erreur}")
        finally:
            # fermeture du fichier s'il a été ouvert
            if file:
                file.close()

    # -------------
    # interface
    # -------------

    # récupération des données de l'administration fiscale
    # la méthode rend un objet [AdminData]
    def get_admindata(self) -> AdminData:
        return self.admindata
