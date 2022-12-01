# imports
from BaseEntity import BaseEntity
from ImpotsError import ImpotsError

# un contribuable
class TaxPayer(BaseEntity):
    # modélise un contribuable
    # id : identifiant du contribuable
    # marié : oui / non
    # enfants : nombre d'enfants
    # salaire : salaire annuel
    # impôt : montant de l'impôt à payer
    # surcôte : surcôte d'impôt à payer
    # décôte : décôte de l'impôt à payer
    # réduction : réduction sur l'impôt à payer
    # taux : taux d'imposition du contribuable

    # clés exclues de l'état de la classe
    excluded_keys = []

    # clés autorisées
    @staticmethod
    def get_allowed_keys() -> list:
        return ['id', 'marie', 'enfants','salaire','impot','surcote','decote','reduction','taux']

    # properties
    @property
    def marie(self) -> str:
        return self.__marie

    @property
    def enfants(self) -> int:
        return self.__enfants

    @property
    def salaire(self) -> int:
        return self.__salaire

    @property
    def impot(self) -> int:
        return self.__impot

    @property
    def surcote(self) -> int:
        return self.__surcote

    @property
    def decote(self) -> int:
        return self.__decote

    @property
    def reduction(self) -> int:
        return self.__reduction

    @property
    def taux(self) -> float:
        return self.__taux

    # setters
    @marie.setter
    def marie(self, marie: str):
        ok = isinstance(marie, str)
        if ok:
            marie = marie.strip().lower()
            ok = marie == "oui" or marie == "non"
        if ok:
            self.__marie=marie
        else:
            raise ImpotsError(31, f"L'attribut marie [{marie}] doit être 'oui' ou 'non' ")
    @enfants.setter
    def enfants(self, enfants):
        # enfants doit être un entier >= 0
        try:
            enfants = int(enfants)
            erreur = enfants < 0
        except:
            erreur = True
        if not erreur:
            self.__enfants = enfants
        else:
            raise ImpotsError(32, f"L'attribut enfants [{enfants}] doit être un entier >= 0")

    @salaire.setter
    def salaire(self, salaire):
        # salaire doit être un entier >= 0
        try:
            salaire = int(salaire)
            erreur = salaire < 0
        except:
            erreur = True
        if not erreur:
            self.__salaire = salaire
        else:
            raise ImpotsError(33, f"L'attribut salaire [{salaire}] doit être un entier >= 0")

    @impot.setter
    def impot(self, impot):
        # impot doit être un entier >= 0
        try:
            impot = int(impot)
            erreur = impot < 0
        except:
            erreur = True
        if not erreur:
            self.__impot = impot
        else:
            raise ImpotsError(34, f"L'attribut impot [{impot}] doit être un nombre >= 0")

    @decote.setter
    def decote(self, decote):
        # decote doit être un entier >= 0
        try:
            decote = int(decote)
            erreur = decote < 0
        except:
            erreur = True
        if not erreur:
            self.__decote = decote
        else:
            raise ImpotsError(35, f"L'attribut décôte [{decote}] doit être un nombre >=0")

    @surcote.setter
    def surcote(self, surcote):
        try:
            surcote = int(surcote)
            erreur = surcote < 0
        except:
            erreur  = True
        if not erreur:
            self.__surcote = surcote
        else:
            raise ImpotsError(36,f"L'attribut surcôte [{surcote}] doit être un nombre >= 0")
    @reduction.setter
    def reduction(self, reduction):
        # reduction doit être un entier >= 0
        try:
            reduction = int(reduction)
            erreur = reduction < 0
        except:
            erreur = True
        if not erreur:
            self.__reduction = reduction
        else:
            raise ImpotsError(37,f"L'attribut réduction [{reduction}] doit être un nombre >= 0")

    @taux.setter
    def taux(self, taux):
        # taux doit être un réel >= 0
        try:
            taux = float(taux)
            erreur = taux < 0
        except:
            erreur = True
        if not erreur:
            self.__taux = taux
        else:
            raise ImpotsError(38,f"L'attribut taux [{taux}] doit être un nombre >= 0")