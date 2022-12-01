# classe parent de la pluplart des classes à créer pour encapsuler des informations sur un objet.
# deux types de classes :
# ° classes qui ont pour but d'encapsuler des informations sur un même objet avec uniquement des getters /setters.
# ° classe avec peu d'informations mais des méthodes pour implémenter des algorithmes

# imports
import json
import re

from MyException import MyException

# l'objectif de la classe BaseEntity est de faciliter les conversions Objet / Dictionnaire et Objet /jSON

class BaseEntity(object):
    # propriétés exclues de l'état de la classe
    excluded_keys = []

    # propriétés de la classe
    @staticmethod
    def get_allowed_keys() -> list:
        # id : identifiant de l'objet
        return ["id"]

    # toString
    def __str__(self) -> str:
        return self.asjson()

    # getter
    @property
    def id(self) -> int:
        return self.__id 
    
    # setter
    @id.setter
    def id(self,  id):
        # l'id doit être un entier >= 0
        try:
            id = int(id)
            erreur = id < 0
        except :
            erreur = True
        # erreur ?
        if erreur:
            raise MyException(1, f"L'identifiant d'une entité {self.__class__} doit être un entier >= 0")
        else:
            self.__id = id
    
    # On créé les méthodes suivantes :
    # asdict : rend le dictionnaire des propriétés de l'objet
    # fromdict : construit un objet à partir d'un dictionnaire
    # asjson : rend la chaîne jSON de l'objet comme le fait la fonction __str__
    # fromjson : construit un objet à partir de sa chaîne jSON

    # Méthode BaseEntity.fromdict : Permet d'initialiser un objet BaseEntity ou dérivé à partir d'un dictionnaire.

    def fromdict(self, state: dict, silent=False):
        # on met à jour l'objet
        # clés autorisées
        allowed_keys = self.__class__.get_allowed_keys()
        # parcourt des clés de state
        for key, value in state.items():
            # la clé est elle autorisée ? 
            if key not in allowed_keys:
                if not silent:
                    raise MyException(2, f"la clé {key} n'est pas autorisée")
            else:
                # on essaie d'affecter la valeur à la clé
                # on laisse remonter l'éventuelle exception
                setattr(self, key, value)
        # on rend l'objet
        return self

    def asdict(self, included_keys: list = None, excluded_keys: list =[]) -> dict:
        # attributs de l'objet
        attributes = self.__dict__
        # les nouveaux attributs
        new_attributes = {}
        # on parcourt les attributs
        for key, value in attributes.items():
            # si la clé est  explicitement demandée
            if included_keys and key in included_keys:
                self.set_value(key, value, new_attributes)
            # sinon la clé n'est pas exclue
            elif not included_keys and key not in self.__class__.excluded_keys and key not in excluded_keys:
                self.set_value(key, value, new_attributes)
            # on rend le dictionnaire des attributs
        return new_attributes

    @staticmethod
    def set_value(key: str, value, new_attributes: dict):
        # les clés peuvent être de la forme __Class__key
        match = re.match("^.*?__(.*?)$", key)
        if match:
            # on note la nouvelle clé
            newkey = match.groups()[0]
            
        else:
            # la clé reste inchangée
            newkey = key
        # on insère la nouvelle clé dans le dictionnaire [new_attributes]
        # en transformant si besoin est la valeur assiciée en l'un des types
        # dict, list, type simple
        new_attributes[newkey] = BaseEntity.check_value(value)

    @staticmethod
    def check_value(value):
        # la valeur peut être de type BaseEntity, list, dict ou un type simple
        # value est-elle une instance de BaseEntity ?
        if isinstance(value, BaseEntity):
            value2 = value.asdict()
        # value est elle de type list
        elif isinstance(value, list):
            value2 = BaseEntity.list2list(value)
        # value est elle de type dict ?
        elif isinstance(value, dict):
            value2 = BaseEntity.dict2dict(value)
        # value est un type simple
        else:
            value2 = value
        # on rend le résultat
        return value2


    def asjson(self, included_keys: list = None, excluded_keys: list = []) -> str:
            # la chaîne json
            return json.dumps(self.asdict(included_keys=included_keys, excluded_keys=excluded_keys),ensure_ascii=False)

    # toString
    def __str__(self) -> str:
        return self.asjson()

    def fromjson(self, json_state: str, silent: bool = False):
        # on met à jour l'état de l'objet à partir de la chaîne jSON
        # json_state : dictionnaire json pour initialiser l'objet BaseEntity
        # on construit un dictionnaire python à partir du dictionnaire jSON 
        # puis fromdict pour initialiser l'objet BaseEntity à partir du dictionnaire Python
        return self.fromdict(json.loads(json_state), silent = silent)


    @staticmethod
    def list2list(liste: list) -> list:
        # on inspecte les éléments de la liste
        newlist = []
        for value in liste:
            newlist.append(BaseEntity.check_value(value))
        # on rend la nouvelle liste
        return newlist

    @staticmethod
    def dict2dict(dictionary: dict) -> dict:
        # on inspecte les éléments du dictionnaire
        newdict = {}
        for key, value in dictionary.items():
            newdict[key] = BaseEntity.check_value(value)
        # on rend le nouveau dictionnaire
        return newdict
        
