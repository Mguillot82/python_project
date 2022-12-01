# interface de la couche metier

# imports
from abc import ABC, abstractmethod

from StatsForEleve import StatsForEleve

# interface Metier
class InterfaceMetier(ABC):
    # calcul de statistiques pour un élève
    @abstractmethod
    # Rend les notes de l'eleve idEleve et les informations associées : moyenne pondérée, note la plus basse, note la
    # plus haute. Ces informations sont encapsulées dans un objet de type StatsForEleve
    def get_stats_for_eleve(self, idEleve: int) -> StatsForEleve:
        pass
