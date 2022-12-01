# imports
from MyException import MyException
from Personne import Personne
from Utils import Utils

# classe Enseignant

class Enseignant(Personne):
    # propriétés exclues de l'état de la classe
    excluded_keys = []

    # propriétés de la classe
    # id : identifiant de la personne
    # prénom : prénom de la personne
    # nom : nom de la personne
    # âge : âge de la personne
    # discipline : discipline enseignée
    @staticmethod
    def get_allowed_keys() -> list:
        # id : identifiant de l'objet
        return Personne.get_allowed_keys() + ["discipline"]

    # propriétés
    @property
    def discipline(self) -> str:
        return self.__discipline

    @discipline.setter
    def discipline(self, discipline: str):
        # la discipline doit être une chaîne non vide
        if Utils.is_string_ok(discipline):
            self.__discipline = discipline
        else:
            raise MyException(21, "La discipline doit être une chaîne de caractères non vide")

    # méthode show
    def show(self):
        print(f"Enseignant[{self.id}, {self.prenom}, {self.nom}, {self.age}]")
