# imports
from abc import ABC, abstractmethod


# interface InterfaceImpôtsUI
class InterfaceImpotsUi(ABC):
    # exécution de la classe implémentant l'interface
    @abstractmethod
    def run(self):
        pass
