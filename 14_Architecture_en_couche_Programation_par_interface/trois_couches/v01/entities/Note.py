# imports
from BaseEntity import BaseEntity
from Eleve import Eleve
from Matiere import Matiere
from MyException import MyException

class Note(BaseEntity):
    # attributs exclus de l'état de la classe
    excluded_keys = []

    # propriétés de la classe
    @staticmethod
    def get_allowed_keys() -> list:
        # id : identifiant de l'élève
        # nom : nom de l'élève
        # coefficient : coefficient de l'élève
        return BaseEntity.get_allowed_keys() + ["valeur", "eleve", "matiere"]

    # getters
    @property
    def valeur(self: object) -> float:
        return self.__valeur

    @property
    def eleve(self: object) -> Eleve:
        return self.__eleve

    @property
    def matiere(self: object) -> Matiere:
        return self.__matiere

    # getters
    @valeur.setter
    def valeur(self: object, valeur: float):
        # la note doit être un réel entre 0 et 20
        if isinstance(valeur, (int, float)) and 0 <= valeur <= 20:
            self.__valeur = valeur
        else:
            raise MyException(31, f"L'attribut {valeur} de la note {self.id} doit être un nombre dans l'intervalle [0,20]")

    @eleve.setter
    def eleve(self: object, value):
        try:
            # on attend un type Eleve
            if isinstance(value, Eleve):
                self.__eleve = value
            # ou un type dict
            elif isinstance(value, dict):
                self.__eleve = Eleve().fromdict(value)
            # ou un type json
            elif isinstance(value, str):
                self.__eleve = Eleve().fromjson(value)
        except BaseException as erreur:
            raise MyException(32, f"L'attribut [{value}] de la note {self.id} doit être de type Eleve ou dict ou json. Erreur {erreur}")

    @matiere.setter
    def matiere(self: object, value):
        try:
            # on attend un type Matière
            if isinstance(value, Matiere):
                self.__matiere = value
            # ou un type dict
            elif isinstance(value, dict):
                self.__matiere = Matiere().fromdict(value)
            # ou un type jSON
            elif isinstance(value, str):
                self.__matiere = Matiere().fromjson(value)
        except BaseException as erreur:
            raise MyException(33, f"L'attribut [{value}] de la note {self.id} doit être de type Matière ou dict ou jSON. Erreur : {erreur}")