import unittest

class TestBaseEntity(unittest.TestCase):

    def setUp(self):
        # on configure l'application
        import config

        config = config.configure()

    def test_note1(self):
        # imports
        from Note import Note
        from Eleve import Eleve
        from Classe import Classe
        from Matiere import Matiere

        # construction d'une note à partie d'une chaîne jSON
        note = Note().fromjson(
            '{"id": 8, "valeur": 12, '
            '"eleve": {"id": 42, "nom": "nom4", "prenom": "prenom4", '
            '"classe":{"id": 2, "nom": "classe2"}}, '
            '"matiere": {"id": 2, "nom": "matiere2", "coefficient": 2}}')

        # vérifications
        self.assertIsInstance(note, Note)
        self.assertIsInstance(note.eleve, Eleve)
        self.assertIsInstance(note.eleve.classe, Classe)
        self.assertIsInstance(note.matiere, Matiere)

    def test_note2(self):
        # imports
        from Note import Note
        from Eleve import Eleve
        from Matiere import Matiere
        from Classe import Classe
        # construction d'une note à partir d'un dictionnaire
        note = Note().fromdict(
            {"id": 8, "valeur": 12,
             "eleve": {"id": 42, "nom": "nom4", "prenom": "prenom4",
                       "classe": {"id": 2, "nom": "classe2"}},
             "matiere": {"id": 2, "nom": "matiere2", "coefficient": 2}})
        # vérifications
        self.assertIsInstance(note, Note)
        self.assertIsInstance(note.eleve, Eleve)
        self.assertIsInstance(note.eleve.classe, Classe)
        self.assertIsInstance(note.matiere, Matiere)

if __name__ == '__main__':
    unittest.main()
