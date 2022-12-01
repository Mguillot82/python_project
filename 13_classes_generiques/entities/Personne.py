# imports

from BaseEntity import BaseEntity
from MyException import MyException
from Utils import Utils

# classe Personne
class Personne(BaseEntity):
    # propriétés  exclues de l'état de la classe
    excluded_keys = []

    # propriété de la classe
    #  id : identifiant de la personne
    # prénom : prénom de la personne
    # nom : nom de la personne
    # âge : âge de la personne
    @staticmethod
    def get_allowed_keys() -> list:
        # id : identifiant de l'objet
        return BaseEntity.get_allowed_keys() +["nom", "prenom", "age"]

    # getters 
    @property
    def prenom(self) -> str:
        return self.__prenom
    
    @property
    def nom(self) -> str:
        return self.__nom

    @property
    def age(self) -> int:
        return self.__age 

    # setters
    @prenom.setter
    def prenom(self, prenom:str):
        # le prenom doit être non vide
        if Utils.is_string_ok(prenom):
            self.__prenom = prenom.strip()
        else:
            raise MyException(11, "Le prenom doit être une chaîne de caractères non vide")

    @nom.setter
    def nom(self, nom: str):
        # le prénom doit être non vide
        if Utils.is_string_ok(nom):
            self.__nom = nom.strip()
        else:
            raise MyException(12, "Le nom doit être une chaîne de caractères non vide")
    
    @age.setter
    def age(self, age: int):
        # l'age doit être un entier >= 0
        erreur = False
        if isinstance(age, int):
            if age >= 0:
                self.__age = age
            else:
                erreur = True
        else:
            erreur = True
        # erreur ?
        if erreur:
            raise MyException(13, "l'âge doit être un entier >=0")
            