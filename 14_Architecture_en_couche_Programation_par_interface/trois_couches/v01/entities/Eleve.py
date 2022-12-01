# imports
from BaseEntity import BaseEntity
from Classe import Classe
from MyException import MyException

from Utils import Utils


class Eleve(BaseEntity):
    # attributs exclus de l'état de la classe
    excluded_keys = []

    # propriétés de la classe
    @staticmethod
    def get_allowed_keys() -> list:
        # id : identifiant de l'élève
        # nom : nom de l'élève
        # prenom : prenom de l'élève
        # coefficient : coefficient de l'élève
        return BaseEntity.get_allowed_keys() + ["nom", "prenom", "classe"]

    # getters
    @property
    def nom(self: object) -> str:
        return self.__nom

    @property
    def prenom(self: object) -> str:
        return self.__prenom

    @property
    def classe(self: object) -> Classe:
        return self.__classe

    # setters
    @nom.setter
    def nom(self: object, nom: str) -> str:
        # nom doit être une chaîne de caractères non vide
        if Utils.is_string_ok(nom):
            self.__nom = nom
        else:
            raise MyException(41, f"Le nom de l'élève {self.id} doit être une chaîne de caractères non vide")

    @prenom.setter
    def prenom(self: object, prenom: str) -> str:
        # nom doit être une chaîne de caractères non vide
        if Utils.is_string_ok(prenom):
            self.__prenom = prenom
        else:
            raise MyException(42, f"Le prénom de l'élève {self.id} doit être une chaîne de caractères non vide")

    @classe.setter
    def classe(self: object, value):
        try:
            # on attend un type Classe
            if isinstance(value, Classe):
                self.__classe = value
            # ou un type dict
            elif isinstance(value, dict):
                self.__classe=Classe().fromdict(value)
            # ou un type json
            elif isinstance(value, str):
                self.__classe = Classe().fromjson(value)
        except BaseException as erreur:
            raise MyException(43, f" L'attribut [{value}] de l'élève {self.id} doit être de type Classe ou dict ou json. Erreur : {erreur}")