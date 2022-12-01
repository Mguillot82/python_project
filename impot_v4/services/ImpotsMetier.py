# imports
import math

from AdminData import AdminData
from InterfaceImpotsMetier import InterfaceImpotsMetier
from TaxPayer import TaxPayer

# couche métier
class ImpotsMetier(InterfaceImpotsMetier):
    # calcul de l'impôt
    # revenu_imposable = salaireAnnuel - abattement
    # l'abattement a un min et un max
    def get_revenu_imposable(self, taxpayer: TaxPayer, admindata: AdminData):

        salaire = taxpayer.salaire
        # abattement de 10% du salaire
        abattement = 0.1 * salaire
        # cet abattement ne peut dépasser ABATTEMENT_DIXPOURCENT_MAX
        if abattement > admindata.abattement_dixpourcent_max:
            abattement = admindata.abattement_dixpourcent_max

        # l'abattement ne peut être inférieur à ABATTEMENT_DIXPOURCENT_MIN
        if abattement < admindata.abattement_dixpourcent_min:
            abattement = admindata.abattement_dixpourcent_min

        # revenu imposable
        revenu_imposable = salaire - abattement
        # résultat
        return math.floor(revenu_imposable)

    def get_reduction(self, taxpayer: TaxPayer, admindata: AdminData):
        # le plafond des revenus pour avoir droit à la réduction de 20%
        marie = taxpayer.marie
        enfants = taxpayer.enfants
        salaire = taxpayer.salaire
        impot = taxpayer.impot

        plafond_revenus_pour_reduction = admindata.plafond_revenus_couple_pour_reduction if marie == "oui" else \
            admindata.plafond_revenus_celibataire_pour_reduction
        plafond_revenus_pour_reduction += enfants * admindata.valeur_reduc_demi_part
        if enfants > 2:
            plafond_revenus_pour_reduction += (enfants - 2) * admindata.valeur_reduc_demi_part

        # revenu imposable
        revenu_imposable = self.get_revenu_imposable(taxpayer, admindata)
        # reduction
        reduction = 0
        if revenu_imposable < plafond_revenus_pour_reduction:
            # reduction de 20%
            reduction = 0.2 * impot

        taxpayer.reduction = math.ceil(reduction)

    def get_decote(self, taxpayer: TaxPayer, admindata: AdminData):
        # au départ, une décôte nulle

        marie = taxpayer.marie
        impot = taxpayer.impot

        decote = 0
        # montant maximal d'impôt pour avoir la décôte
        plafond_pour_decote = admindata.plafond_impot_couple_pour_decote if marie == "oui" else \
            admindata.plafond_impot_celibataire_pour_decote
        if impot < plafond_pour_decote:
            # montant maximal de la décôte
            plafond_decote = admindata.plafond_decote_couple if marie == "oui" \
                else admindata.plafond_decote_celibataire
            # decote théorique
            decote = plafond_decote - 0.75 * impot
            # la décôte ne peut dépasser le montant de l'impôt
            if decote > impot:
                decote = impot

            # pas de décôte < 0
            if decote < 0:
                decote = 0

        taxpayer.decote = math.ceil(decote)

    def calculate_tax_2(self, taxpayer: TaxPayer, admindata: AdminData):
        # taxpayer(id, marie, enfants, salaire, impot, decote, surcote, reduction, taux)
        # admindata : données de l'administration fiscale
        #
        marie = taxpayer.marie
        enfants = taxpayer.enfants
        salaire = taxpayer.salaire
        marie = marie.strip().lower()

        if marie == "oui":
            nb_parts = enfants / 2 + 2
        else:
            nb_parts = enfants / 2 + 1

        # 1 part par enfant à partir du 3ème
        if enfants >= 3:
            # une demi-part de + pour chaque enfant à partir du 3ème
            nb_parts += 0.5 * (enfants - 2)

        # revenu imposable
        revenu_imposable = self.get_revenu_imposable(taxpayer, admindata)
        # surcote
        surcote = math.floor(revenu_imposable - 0.9 * salaire)
        # pour les problèmes d'arrondis
        if surcote < 0:
            surcote = 0
        # quotient familial
        quotient = revenu_imposable / nb_parts

        limites = admindata.limites
        coeffr = admindata.coeffr
        coeffn = admindata.coeffn

        limites[len(limites) -1] = quotient
        i=0

        while quotient > limites[i]:
            i += 1
            # du fait qu'on a placé quotient à la fin du tableau limites, la boucle précédente
        # ne peut déborder du tableau limites

        # maintenant on peut calculer l'impôt
        impot = math.floor(revenu_imposable * coeffr[i] - nb_parts * coeffn[i])

        taxpayer.impot = impot
        taxpayer.surcote = surcote
        taxpayer.taux = coeffr[i]


    def calculate_tax(self, taxpayer: TaxPayer, admindata: AdminData):
        # taxpayer(id, marie, enfants, salaire, impot, decote, surcote, reduction, taux)
        # admindata : données de l'adm fiscale

       # calcul de l'impôt avec enfants
        self.calculate_tax_2(taxpayer, admindata)
        # les résultats sont dans un taxpayer
        taux1 = taxpayer.taux
        surcote1 = taxpayer.surcote
        impot1 = taxpayer.impot
        # calcul de l'impot sans les enfants
        if taxpayer.enfants != 0:
            # calcul de l'impot pour le même contribuable sans enfants
            taxpayer2 = TaxPayer().fromdict(
                {'id':0,'marie': taxpayer.marie, 'enfants':0, 'salaire': taxpayer.salaire})
            self.calculate_tax_2(taxpayer2,admindata)
            # les résultats sont dans taxpayer2
            taux2 = taxpayer2.taux
            surcote2 = taxpayer2.surcote
            impot2 = taxpayer2.impot
            # application du plafonnement du quotient familial
            if taxpayer.enfants < 3:
                # Plafond qf demi part euros pour les 2 premiers enfants
                impot2 = impot2 - taxpayer.enfants * admindata.plafond_qf_demi_part
            else:
                impot2 = impot2 - 2 * admindata.plafond_qf_demi_part - (taxpayer.enfants - 2) \
                         * 2 * admindata.plafond_qf_demi_part
        else:
            impot2 = impot1

        # on prend l'impot le plus fort avec le taux et la surcote qui vont avec
        (impot, surcote, taux) = (impot1, surcote1, taux1) if impot1 >= impot2 else (
            impot2, impot2 - impot1 + surcote2, taux2)

        # résultats partiels
        taxpayer.impot = impot
        taxpayer.surcote = surcote
        taxpayer.taux = taux
        # calcul d'une éventuelle décote
        self.get_decote(taxpayer,admindata)
        taxpayer.impot -= taxpayer.decote
        # calcul d'une éventueller éduction d'impot
        self.get_reduction(taxpayer,admindata)
        taxpayer.impot -= taxpayer.reduction
        # resultat
        taxpayer.impot = math.floor(taxpayer.impot)
