# imports
from abc import ABC, abstractmethod

# interfaceDao est une classe abstraite qui dérive de la classe ABC du module abc.
# le décorateur @abstracmethod fait de la méthode une méthode abstraite.
# la classe abstraite InterfaceDao ne peut être instanciée. Seules les classes dérivées de InterfaceDao ayant implémentées
# toutes les méthodes d'InterfaceDao peuvent être implémentée.

# une interface n'a pas d'attributs et ne peut être instanciée. Une classe peut implémenter une interface en définissant
# toutes les méthodes de l'interface.

from Eleve import Eleve

class InterfaceDao(ABC):
    # liste des classes
    @abstractmethod
    def get_eleves(self: object) -> list:
        pass

    # liste des élèves
    @abstractmethod
    def get_eleves(self: object) -> list:
        pass

    # liste des matières
    @abstractmethod
    def get_matieres(self:object) -> list:
        pass

    # liste des notes
    @abstractmethod
    def get_notes(self: object) -> list:
        pass

    # liste des notes d'un élève
    @abstractmethod
    def get_notes_for_eleve_by_id(self: object, eleve_id: int) -> list:
        pass

    # chercher un élève par son id
    @abstractmethod
    def get_eleve_by_id(self, eleve_id: int) -> Eleve:
        pass