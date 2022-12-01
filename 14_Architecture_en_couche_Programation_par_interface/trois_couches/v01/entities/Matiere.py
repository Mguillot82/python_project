# imports
from BaseEntity import BaseEntity
from MyException import MyException
from Utils import Utils

class Matiere(BaseEntity):
    # attributs exclus de l'état de la classe
    excluded_keys = []

    # propriétés de la classe
    @ staticmethod
    def get_allowed_keys() -> list:
        # id : identifiant de la matière
        # nom : nom de la matière
        # coefficient : coefficient de la matière
        return BaseEntity.get_allowed_keys() + ["nom", "coefficient"]

    # getter
    @property
    def nom(self: object) -> str:
        return self.__nom

    @property
    def coefficient(self: object) -> float:
        return self.__coefficient

    # setters
    @nom.setter
    def nom(self: object, nom: str):
        # nom doit être une chaîne de caractères non vide
        if Utils.is_string_ok(nom):
            self.__nom = nom
        else:
            raise MyException(21, f"Le nom de la matière {self.id} doit être une chaîne de caractères non vide.")

    @coefficient.setter
    def coefficient(self, coefficient: float):
        # le coefficient doit être un réel >= 0
        erreur = False
        if isinstance(coefficient, (int, float)):
            if coefficient >= 0:
                self.__coefficient = coefficient
            else:
                erreur = True
        else:
            erreur = True
        # erreur ?
        if erreur:
            raise MyException(22, f"Le coefficient de la matière {self.nom} doit être un réel >= 0")