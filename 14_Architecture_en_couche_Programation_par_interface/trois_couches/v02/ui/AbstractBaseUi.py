from abc import ABC, abstractmethod

from InterfaceMetier import InterfaceMetier
from InterfaceUi import InterfaceUi

class AbstractBaseUi(InterfaceUi, ABC):
    # propriétés
    # métier est une référence sur la couche métier
    @property
    def metier(self) -> InterfaceMetier:
        return self.__metier

    @metier.setter
    def metier(self, metier: InterfaceMetier):
        self.__metier = metier

    # implémentation de l'interface InterfaceUi
    @abstractmethod
    def do_something_in_ui_layer(self: InterfaceUi, x: int, y: int) -> int:
        pass