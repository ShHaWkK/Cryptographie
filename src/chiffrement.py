import string
import random

class ChiffrementClassique:
    def __init__(self):
        self.alphabet = string.ascii_uppercase
    
    def chiffrer_cesar(self, texte, decalage):
        resultat = ""
        for char in texte.upper():
            if char in self.alphabet:
                index = (self.alphabet.index(char) + decalage) % 26
                resultat += self.alphabet[index]
            else:
                resultat += char
        return resultat
    
    def chiffrer_substitution(self, texte, cle=None):
        if not cle:
            cle = ''.join(random.sample(self.alphabet, len(self.alphabet)))
        
        table_chiffrement = str.maketrans(self.alphabet, cle)
        return texte.upper().translate(table_chiffrement)
    
    def chiffrer_vigenere(self, texte, cle):
        # Implémentation du chiffrement de Vigenère
        pass
    
    def chiffrer_playfair(self, texte, cle):
        # Implémentation du chiffrement de Playfair
        pass
