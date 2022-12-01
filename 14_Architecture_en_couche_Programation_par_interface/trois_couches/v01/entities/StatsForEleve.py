# imports
from BaseEntity import BaseEntity

# statistiques d'un élève particulier

class StatsForEleve(BaseEntity):
    # attributs exclus de l'état de la classe
    excluded_keys = []

    # propriétés de la classe
    @staticmethod
    def get_allowed_keys() -> list:
        # id: identifiant de la note
        # élève : l'élève concerné
        # notes : ses notes
        # moyennePondérée : sa moyenne pondérée par les coefficients des matières
        # min : sa note minimale
        # max : sa note maximale

        return BaseEntity.get_allowed_keys() + ["eleve", "notes", "moyenne_ponderee", "min", "max"]

    # toString
    # Renvoie une chaîne de caractère reprenant les propriétés de l'objet
    def __str__(self) -> str:
        # cas de l'élève sans notes
        if len(self.notes) == 0:
            return f"Eleve={self.eleve}, notes= []"
        # cas de l'élève avec notes
        str = ""
        for note in self.notes:
            str += f"{note.valeur}"
        return f"Eleve={self.eleve}, notes=[{str.strip()}], max={self.max}, min={self.min}," \
               f"moyenne ponderee = {self.moyenne_ponderee:4.2f}"
