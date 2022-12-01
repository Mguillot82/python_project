# imports
from abc import ABC, abstractmethod

from InterfaceDao import InterfaceDao
from InterfaceMetier import InterfaceMetier

class AbstractBaseMetier(InterfaceMetier, ABC):
    # propriétés
    # __dao est une référence sur la couche dao
    @property
    def dao(self) -> InterfaceDao:
        return self.__dao
    @dao.setter
    def dao(self, dao: InterfaceDao):
        self.__dao = dao

    # implémentation de l'interface InterfaceMetier
    @abstractmethod
    def do_something_in_metier_layer(self, x: int, y: int) -> int:
        pass