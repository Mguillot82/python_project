from abc import ABC, abstractmethod

# interface ui
class InterfaceUi(ABC):
    # une seule méthode
    @abstractmethod
    def do_something_in_ui_layer(self, x: int, y: int) -> int:
        pass