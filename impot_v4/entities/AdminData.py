from BaseEntity import BaseEntity

# données de l'administration fiscale
class AdminData(BaseEntity):
    # clés exclues de l'état de la classe
    excluded_keys = []

    # pas de setter car les données sont rentrées en dur, non susceptible d'être erronées.

    # clés autorisées
    @staticmethod
    def get_allowed_keys() -> list:
        return [
            "id",
            "limites",
            "coeffr",
            "coeffn",
            "plafond_qf_demi_part",
            "plafond_revenus_celibataire_pour_reduction",
            "plafond_revenus_couple_pour_reduction",
            "valeur_reduc_demi_part",
            "plafond_decote_celibataire",
            "plafond_decote_couple",
            "plafond_impot_couple_pour_decote",
            "plafond_impot_celibataire_pour_decote",
            "abattement_dixpourcent_max",
            "abattement_dixpourcent_min"
        ]
