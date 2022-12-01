# Metier est la classe d'implémentation de la couche metier

# imports
from InterfaceDao import InterfaceDao
from InterfaceMetier import InterfaceMetier
from StatsForEleve import StatsForEleve

# la classe métier dérive de l'interface metier. Elle implémente l'interface métier
class Metier(InterfaceMetier):

    # constructeur
    def __init__(self, dao: InterfaceDao):
        # on mémorise le paramètre
        self.__dao = dao

    # -----------
    # interface
    # ----------

    # les indicateurs sur les notes d'un élève particulier
    def get_stats_for_eleve(self, id_eleve: int) -> StatsForEleve:
        # Stats pour l'élève de n° idEleve
        # id_eleve : n° de l'élève

        # on récupère ses notes avec la couche dao
        notes_eleve = self.__dao.get_notes_for_eleve_by_id(id_eleve)
        eleve = notes_eleve["eleve"]
        notes = notes_eleve["notes"]

        # on s'arrête s'il n'y a pas de notes
        if len(notes) == 0:
            # on rend le résultat
            return StatsForEleve().fromdict({"eleve":eleve, "notes": []})

        # exploitation des notes de l'élève
        somme_ponderee = 0
        somme_coeff = 0
        max = -1
        min = 21
        for note in notes:
            # valeur de la note
            valeur = note.valeur
            # coefficient de la matière
            coeff = note.matiere.coefficient
            # somme des coefficients
            somme_coeff += coeff
            # somme pondérée
            somme_ponderee += valeur * coeff
            # recherche du min
            if valeur < min:
                min = valeur
            # recherche du max
            if valeur > max:
                max = valeur
        # calcul des indicateurs manquants
        moyenne_ponderee = float(somme_ponderee) / somme_coeff

        # on rend le résultat sous la forme d'un type [StatsForEleve]
        return StatsForEleve().\
            fromdict({"eleve": eleve, "notes": notes,
                      "moyenne_ponderee": moyenne_ponderee,
                      "min": min, "max":max})
