# imports
from BaseEntity import BaseEntity
from MyException import MyException
from Utils import Utils

class Classe(BaseEntity):
    # attributs exclus de l'état de la classe
    excluded_keys = []

    # propriétés de la classe
    @staticmethod
    def get_allowed_keys() -> list:
        # id : identifiant de la classe
        # nom : nom de la classe
        return BaseEntity.get_allowed_keys() + ["nom"]

    # getter
    @property
    def nom(self: object) -> str:
        return self.__nom

    # setters
    @nom.setter
    def nom(self: object, nom: str):
        # nom doit être une chaîne de caractères non vide
        if Utils.is_string_ok(nom):
            self.__nom = nom
        else:
            raise MyException(11, f"Le nom de la classe {self.id} doit être une chaîne de caractère non vide")
        