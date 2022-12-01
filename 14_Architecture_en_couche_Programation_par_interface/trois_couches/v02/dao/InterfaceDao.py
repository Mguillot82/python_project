# imports
from abc import ABC, abstractmethod

# interface Dao
class InterfaceDao(ABC):
    # une seule méthode
    @abstractmethod
    def do_something_in_dao_layer(self, x: int, y: int) -> int:
        pass