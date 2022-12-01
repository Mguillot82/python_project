# imports
from abc import ABC, abstractmethod

# interface métier
class InterfaceMetier(ABC):
    # une seule méthode
    @abstractmethod
    def do_something_in_metier_layer(self, x: int, y: int) -> int:
        pass
