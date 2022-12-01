import unittest

class TestEntites(unittest.TestCase):
    def setUp(self):
        # on configure l'application
        import config
        config.configure()

    def test_code1a(self):
        # imports
        from Eleve import Eleve
        from MyException import MyException

        code = None
        try:
            # id invalide
            Eleve().fromdict({"id": "x", "nom":"y", "prenom":"z", "classe": "t"})
        except MyException as ex:
            print(f'\ncode erreur={ex.code}, message = {ex}')
            code = ex.code
        # verification
        self.assertEqual(code, 1)

    def test_code41(self):
        # imports
        from Eleve import Eleve
        from MyException import MyException
        # code d'erreur
        code = None

        try:
            # nom invalide
            Eleve().fromdict({"id": 1, "nom":"", "prenom":"z", "classe": "t"})
        except MyException as ex:
            print(f'\ncode erreur={ex.code}, message = {ex}')
            code = ex.code
        # verification
        self.assertEqual(code, 41)

    def test_code42(self):
        # imports
        from Eleve import Eleve
        from MyException import MyException
        # code d'erreur
        code = None
        try:
            # Prenom invalide
            Eleve().fromdict({"id": 1, "nom": "y", "prenom": "", "classe": "t"})
        except MyException as ex:
            print(f'\ncode erreur={ex.code}, message = {ex}')
            code = ex.code
        # verification
        self.assertEqual(code, 42)

    def test_code43(self):
        # imports
        from Eleve import Eleve
        from MyException import MyException
        # code d'erreur
        code = None
        try:
            # classe invalide
            Eleve().fromdict({"id": 1, "nom": "y", "prenom": "z", "classe": "t"})
        except MyException as ex:
            print(f'\ncode erreur={ex.code}, message = {ex}')
            code = ex.code
        # verification
        self.assertEqual(code, 43)

    def test_code1b(self):
        # imports
        from Classe import Classe
        from MyException import MyException
        # code d'erreur
        code = None
        try:
            # identifiant invalide
            Classe().fromdict({"id": "x", "nom": "y"})
        except MyException as ex:
            print(f"\ncode erreur= {ex.code}, message = {ex}")
            code = ex.code
        # verification
        self.assertEqual(code, 1)

    def test_code11(self):
        # imports
        from Classe import Classe
        from MyException import MyException
        # code d'erreur
        code = None
        try:
            # nom invalide
            Classe().fromdict({"id": 1, "nom": ""})
        except MyException as ex:
            code = ex.code
        # verification
        self.assertEqual(code, 11)

    def test_code1c(self):
        # imports
        from Matiere import Matiere
        from MyException import MyException

        # code d'erreur
        code = None
        try:
            # identifiant invalide
            Matiere().fromdict({"id": "x", "nom": "y", "coefficient": "t"})
        except MyException as ex:
            print(f"\ncode erreur= {ex.code}, message = {ex}")
            code = ex.code
        # verification
        self.assertEqual(code, 1)

    def test_code21(self):
        # imports
        from Matiere import Matiere
        from MyException import MyException

        # code d'erreur
        code = None
        try:
            # identifiant invalide
            Matiere().fromdict({"id": 1, "nom": "", "coefficient": "t"})
        except MyException as ex:
            print(f"\ncode erreur= {ex.code}, message = {ex}")
            code = ex.code
        # verification
        self.assertEqual(code, 21)

    def test_code22(self):
        # imports
        from Matiere import Matiere
        from MyException import MyException

        code = None
        try:
            # coefficient invalide
            Matiere().fromdict({"id": 1, "nom": "y", "coefficient": "t"})
        except MyException as ex:
            print(f"\ncode erreur= {ex.code}, message = {ex}")
            code = ex.code
        # verification
        self.assertEqual(code, 22)

    def test_code1d(self):
        # imports
        from Note import Note
        from MyException import MyException

        code = None
        try:
            # identifiant invalide
            Note().fromdict({"id":"x", "valeur": "x", "eleve":"y", "matiere":"z"})
        except MyException as ex:
            print(f"\ncode erreur= {ex.code}, message = {ex}")
            code = ex.code
        # verification
        self.assertEqual(code, 1)

    def test_code31(self):
        # imports
        from Note import Note
        from MyException import MyException
        code = None
        try:
            # valeur invalide
            Note().fromdict({"id": 1, "valeur": "x", "eleve": "y", "matiere": "z"})
        except MyException as ex:
            print(f"\ncode erreur= {ex.code}, message = {ex}")
            code = ex.code
        # verification
        self.assertEqual(code, 31)

    def test_code32(self):
        # imports
        from Note import Note
        from MyException import MyException

        code = None
        try:
            # eleve invalide
            Note().fromdict({"id":1, "valeur":10, "eleve":"y", "matiere":"z"})
        except MyException as ex:
            print(f"\ncode erreur = {ex.code}, message = {ex}")
            code = ex.code
        # verification
        self.assertEqual(code, 32)

    def test_code33(self):
        # import
        from Eleve import Eleve
        from Note import Note
        from Classe import Classe
        from MyException import MyException

        code = None
        try:
            # matiere invalide
            classe = Classe().fromdict({"id": 1, "nom": "x"})
            eleve = Eleve().fromdict({"id":1, "nom": "a", "prenom": "b", "classe": classe})
            Note().fromdict({"id": 1, "valeur": 10, "eleve": eleve, "matiere": "z"})
        except MyException as ex:
            print(f"\ncode erreur = {ex.code}, message = {ex}")
            code = ex.code
        self.assertEqual(code, 33)

    def test_exception(self):
        from Eleve import Eleve
        from MyException import MyException
        with self.assertRaises(MyException):
            Eleve().fromdict({"id":"x", "nom": "y", "prenom": "z", "classe": "t"})

if __name__ == '__main__':
    unittest.main()
