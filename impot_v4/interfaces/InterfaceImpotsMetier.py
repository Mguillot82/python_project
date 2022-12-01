# imports
from abc import ABC, abstractmethod

from AdminData import AdminData
from TaxPayer import TaxPayer


# interface IImpôtsMétier
class InterfaceImpotsMetier(ABC):
    # calcul de l'impôt pour 1 contribuable
    @abstractmethod
    def calculate_tax(self, taxpayer: TaxPayer, admindata: AdminData):
        pass