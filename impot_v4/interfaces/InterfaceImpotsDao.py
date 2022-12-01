# imports
from abc import ABC, abstractmethod


# interface IImpôtsDao
from AdminData import AdminData


class InterfaceImpotsDao(ABC):
    # liste des tranches de l'impôt
    @abstractmethod
    def get_admindata(self) -> AdminData:
        pass

    # liste des données contribuables
    @abstractmethod
    def get_taxpayers_data(self) -> dict:
        pass

    # écriture des résultats du calcul de l'impôt
    @abstractmethod
    def write_taxpayers_results(self, taxpayers_results: list):
        pass
