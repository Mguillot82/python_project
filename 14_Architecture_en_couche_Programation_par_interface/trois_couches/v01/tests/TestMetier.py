# Classe UnitTest de test de la classe Metier
import unittest

class Testmetier(unittest.TestCase):
    def setUp(self):
        # on configure l'application
        import config
        config.configure()

    def test_statsForEleve11(self):
        # imports
        from Dao import Dao
        from Metier import Metier
        # on teste les indicateurs de l'élève 11
        dao = Dao()
        stats_for_eleve = Metier(dao).get_stats_for_eleve(11)
        # affichage
        print(f"\nstats={stats_for_eleve}")
        # vérifications
        self.assertEqual(stats_for_eleve.min,6)
        self.assertEqual(stats_for_eleve.max, 10)
        self.assertAlmostEqual(stats_for_eleve.moyenne_ponderee, 7.333, delta=1e-3)

if __name__ == '__main__':
    if __name__ == '__main__':
        unittest.main()
