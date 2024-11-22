import unittest
from src.chiffrement import ChiffrementSubstitution

class TestChiffrementSubstitution(unittest.TestCase):
    def setUp(self):
        self.chiffrement = ChiffrementSubstitution()

    def test_chiffrer_cesar(self):
        self.assertEqual(self.chiffrement.chiffrer_cesar("HELLO", 3), "KHOOR")

    def test_dechiffrer_cesar(self):
        self.assertEqual(self.chiffrement.dechiffrer_cesar("KHOOR", 3), "HELLO")

    def test_chiffrer_substitution(self):
        cle = "QWERTYUIOPASDFGHJKLZXCVBNM"
        self.assertEqual(self.chiffrement.chiffrer_substitution("HELLO", cle), "ITSSG")

    def test_dechiffrer_substitution(self):
        cle = "QWERTYUIOPASDFGHJKLZXCVBNM"
        self.assertEqual(self.chiffrement.dechiffrer_substitution("ITSSG", cle), "HELLO")

    def test_chiffrer_vigenere(self):
        self.assertEqual(self.chiffrement.chiffrer_vigenere("HELLO", "KEY"), "RIJVS")

    def test_dechiffrer_vigenere(self):
        self.assertEqual(self.chiffrement.dechiffrer_vigenere("RIJVS", "KEY"), "HELLO")

if __name__ == '__main__':
    unittest.main()
