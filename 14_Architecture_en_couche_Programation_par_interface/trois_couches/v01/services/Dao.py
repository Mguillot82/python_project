# get_classes rend la listes des classes du collège
# get_matiere rend la liste des matières enseignées au collège
# get_eleve rend la liste des éleves du collèges
# get_notes rend la liste des notes de tous les éleves
# get_notes_for_eleve_by_id rend les notes d'un élève particulier
# get_eleve_by_id rend un élève repéré par un id

# la couche Dao implémente l'interface comme suit :

# imports des entités et des interfaces
from Classe import Classe
from Eleve import Eleve
from InterfaceDao import InterfaceDao
from Matiere import Matiere
from MyException import MyException
from Note import Note

# couche dao implémente l'interface InterfaceDao. La classe Dao dérive de la classe abstraite InterfaceDao. Elle
# implémente l'interface InterfaceDao

class Dao(InterfaceDao):
    # constructeur : on construit les listes en dur
    def __init__(self):
        # on instancie les classes
        classe1 = Classe().fromdict({"id": 1, "nom": "classe1"})
        classe2 = Classe().fromdict({"id": 2, "nom": "classe2"})
        self.classes = [classe1, classe2]

        # les matières
        matiere1 = Matiere().fromdict({"id": 1, "nom": "matiere1", "coefficient": 1})
        matiere2 = Matiere().fromdict({"id": 2, "nom": "matiere2", "coefficient": 2})
        self.matieres = [matiere1, matiere2]

        # les élèves
        eleve11 = Eleve().fromdict({"id":11, "nom":"nom1", "prenom":"prenom1", "classe": classe1})
        eleve21 = Eleve().fromdict({"id":21, "nom":"nom2", "prenom":"prenom2", "classe": classe1})
        eleve32 = Eleve().fromdict({"id":32, "nom":"nom3", "prenom":"prenom3", "classe": classe2})
        eleve42 = Eleve().fromdict({"id":42, "nom":"nom4", "prenom":"prenom4", "classe": classe2})
        self.eleves = [eleve11, eleve21, eleve32,eleve42]

        # les notes des élèves dans les différentes matières
        note1 = Note().fromdict({"id": 1, "valeur": 10, "eleve": eleve11, "matiere": matiere1})
        note2 = Note().fromdict({"id": 2, "valeur": 12, "eleve": eleve21, "matiere": matiere1})
        note3 = Note().fromdict({"id": 3, "valeur": 14, "eleve": eleve32, "matiere": matiere1})
        note4 = Note().fromdict({"id": 4, "valeur": 16, "eleve": eleve42, "matiere": matiere1})
        note5 = Note().fromdict({"id": 5, "valeur": 6, "eleve": eleve11, "matiere": matiere2})
        note6 = Note().fromdict({"id": 6, "valeur": 8, "eleve": eleve21, "matiere": matiere2})
        note7 = Note().fromdict({"id":7, "valeur": 10, "eleve": eleve32, "matiere": matiere2})
        note8 = Note().fromdict({"id":8, "valeur": 12, "eleve": eleve42, "matiere": matiere2})
        self.notes = [note1, note2, note3,note4,note5,note6,note7, note8]

    # ---------------
    # interface IDao
    # --------------
    def get_classes(self: object) -> list:
        return self.classes

    def get_eleves(self: object) -> list:
        return self.eleves

    def get_matieres(self: object) -> list:
        return self.matieres

    def get_notes(self: object) -> list:
        return self.notes

    def get_notes_for_eleve_by_id(self: object, eleve_id: int) -> list:
        # on recherche l'élève
        eleve = self.get_eleve_by_id(eleve_id)
        # on récupère ses notes
        notes = list(filter(lambda n: n.eleve.id == eleve_id, self.get_notes()))
        # on rend le résultat
        return {"eleve": eleve, "notes": notes}

    def get_eleve_by_id(self, eleve_id: int) -> Eleve:
        # on filtre les élèves
        eleves = list(filter(lambda e: e.id == eleve_id, self.get_eleves()))
        # trouvé ?
        if not eleves:
            raise MyException(10, f"L'élève d'identifiant {eleve_id} n'existe pas")
        # résultat
        return eleves[0]