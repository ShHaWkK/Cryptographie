import unittest
from src.analyse import AnalyseCryptographique

class TestAnalyseCryptographique(unittest.TestCase):
    def setUp(self):
        self.analyse = AnalyseCryptographique()

    def test_analyser_frequences(self):
        texte = "HELLO WORLD"
        frequences = self.analyse.analyser_frequences(texte)
        self.assertEqual(frequences['L'], 3)
        self.assertEqual(frequences['O'], 2)

    def test_casser_cesar(self):
        texte_chiffre = "KHOOR"
        resultats = self.analyse.casser_cesar(texte_chiffre)
        self.assertEqual(resultats[3][1], "HELLO")

if __name__ == '__main__':
    unittest.main()
