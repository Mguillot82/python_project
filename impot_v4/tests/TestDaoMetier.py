import unittest


def get_config() -> dict:

    import config

    return config.configure()

class TestDaoMetier(unittest.TestCase):

    def setUp(self) -> None:

        config = get_config()
        self.metier = config['metier']
        self.admindata = config['dao'].get_admindata()

    def test_1(self) -> None:
        from TaxPayer import TaxPayer

        taxpayer = TaxPayer().fromdict({"marie": "oui", "enfants": 2, "salaire": 55555})
        self.metier.calculate_tax(taxpayer, self.admindata)
        self.assertAlmostEqual(taxpayer.impot, 2815, delta=1)
        self.assertEqual(taxpayer.decote, 0)
        self.assertEqual(taxpayer.reduction, 0)
        self.assertAlmostEqual(taxpayer.taux, 0.14, delta=0.01)
        self.assertEqual(taxpayer.surcote, 0)

    def test_2(self) -> None:
        from TaxPayer import TaxPayer

        taxpayer = TaxPayer().fromdict({"marie": "oui", "enfants": 2, "salaire": 50000})
        self.metier.calculate_tax(taxpayer, self.admindata)

        self.assertAlmostEqual(taxpayer.impot, 1384, delta=1)
        self.assertAlmostEqual(taxpayer.decote, 384, delta=1)
        self.assertAlmostEqual(taxpayer.reduction, 347, delta=1)
        self.assertAlmostEqual(taxpayer.taux, 0.14, delta=0.01)
        self.assertEqual(taxpayer.surcote, 0)

    def test_3(self) -> None:
        from TaxPayer import TaxPayer

        taxpayer = TaxPayer().fromdict({"marie":"oui","enfants":3, "salaire": 50000})
        self.metier.calculate_tax(taxpayer, self.admindata)

        self.assertEqual(taxpayer.impot, 0)
        self.assertAlmostEqual(taxpayer.decote, 720, delta=1)
        self.assertAlmostEqual(taxpayer.reduction, 0)
        self.assertAlmostEqual(taxpayer.taux, 0.14, delta=0.01)
        self.assertEqual(taxpayer.surcote, 0)

    def test_4(self) -> None:
        from TaxPayer import TaxPayer

        taxpayer = TaxPayer().fromdict({"marie": "non", "enfants": 2, "salaire": 100000})
        self.metier.calculate_tax(taxpayer, self.admindata)

        self.assertAlmostEqual(taxpayer.impot, 19884, delta=1)
        self.assertEqual(taxpayer.decote, 0)
        self.assertEqual(taxpayer.reduction, 0)
        self.assertAlmostEqual(taxpayer.taux, 0.41, delta=0.01)
        self.assertAlmostEqual(taxpayer.surcote, 4480, delta=1)

    def test_5(self) -> None:
        from TaxPayer import TaxPayer

        taxpayer = TaxPayer().fromdict({"marie": "non", "enfants": 3, "salaire": 100000})
        self.metier.calculate_tax(taxpayer, self.admindata)

        self.assertAlmostEqual(taxpayer.impot, 16782, delta=1)
        self.assertEqual(taxpayer.decote, 0)
        self.assertEqual(taxpayer.reduction, 0)
        self.assertAlmostEqual(taxpayer.taux, 0.41, delta=0.01)
        self.assertAlmostEqual(taxpayer.surcote, 7176, delta=1)

    def test_6(self) -> None:
        from TaxPayer import TaxPayer

        taxpayer = TaxPayer().fromdict({"marie": "oui", "enfants": 3, "salaire": 100000})
        self.metier.calculate_tax(taxpayer, self.admindata)

        self.assertAlmostEqual(taxpayer.impot, 9200, delta=1)
        self.assertEqual(taxpayer.decote, 0)
        self.assertEqual(taxpayer.reduction, 0)
        self.assertAlmostEqual(taxpayer.taux, 0.3, delta=0.01)
        self.assertAlmostEqual(taxpayer.surcote, 2180, delta=1)

    def test_7(self) -> None:
        from TaxPayer import TaxPayer

        taxpayer = TaxPayer().fromdict({"marie": "oui", "enfants": 5, "salaire": 100000})
        self.metier.calculate_tax(taxpayer, self.admindata)

        self.assertAlmostEqual(taxpayer.impot, 4230, delta=1)
        self.assertEqual(taxpayer.decote, 0)
        self.assertEqual(taxpayer.reduction, 0)
        self.assertAlmostEqual(taxpayer.taux, 0.14, delta=0.01)
        self.assertEqual(taxpayer.surcote, 0)

    def test_8(self) -> None:
        from TaxPayer import TaxPayer

        taxpayer = TaxPayer().fromdict({"marie": "non", "enfants": 0, "salaire": 100000})
        self.metier.calculate_tax(taxpayer, self.admindata)

        self.assertAlmostEqual(taxpayer.impot, 22986, delta=1)
        self.assertEqual(taxpayer.decote, 0)
        self.assertEqual(taxpayer.reduction, 0)
        self.assertAlmostEqual(taxpayer.taux, 0.41, delta=0.01)
        self.assertAlmostEqual(taxpayer.surcote, 0)

    def test_9(self) -> None:
        from TaxPayer import TaxPayer

        taxpayer = TaxPayer().fromdict({"marie": "oui", "enfants": 2, "salaire": 30000})
        self.metier.calculate_tax(taxpayer, self.admindata)

        self.assertEqual(taxpayer.impot, 0)
        self.assertEqual(taxpayer.decote, 0)
        self.assertEqual(taxpayer.reduction, 0)
        self.assertAlmostEqual(taxpayer.taux, 0.0, delta=0.01)
        self.assertAlmostEqual(taxpayer.surcote, 0)

    def test_10(self) -> None:
        from TaxPayer import TaxPayer

        taxpayer = TaxPayer().fromdict({"marie": "non", "enfants": 0, "salaire": 200000})
        self.metier.calculate_tax(taxpayer, self.admindata)

        self.assertAlmostEqual(taxpayer.impot, 64210, delta=1)
        self.assertEqual(taxpayer.decote, 0)
        self.assertEqual(taxpayer.reduction, 0)
        self.assertAlmostEqual(taxpayer.taux, 0.45, delta=0.01)
        self.assertAlmostEqual(taxpayer.surcote,7498, delta=1)

    def test_11(self) -> None:
        from TaxPayer import TaxPayer

        taxpayer = TaxPayer().fromdict({"marie": "oui", "enfants": 3, "salaire": 200000})
        self.metier.calculate_tax(taxpayer, self.admindata)

        self.assertAlmostEqual(taxpayer.impot, 42842, delta=1)
        self.assertEqual(taxpayer.decote, 0)
        self.assertEqual(taxpayer.reduction, 0)
        self.assertAlmostEqual(taxpayer.taux, 0.41, delta=0.01)
        self.assertAlmostEqual(taxpayer.surcote, 17283, delta=1)

if __name__ == '__main__':
    unittest.main()