# interface de la couche ui
from abc import ABC, abstractmethod

# interface UI
class InterfaceUi(ABC):
    # exécution de la couche UI
    @abstractmethod
    def run(self: object):
        pass
