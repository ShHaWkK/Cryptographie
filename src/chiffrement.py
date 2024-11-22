import string

class ChiffrementSubstitution:
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

    def dechiffrer_cesar(self, texte, decalage):
        return self.chiffrer_cesar(texte, -decalage)

    def chiffrer_substitution(self, texte, cle):
        table_chiffrement = str.maketrans(self.alphabet, cle)
        return texte.upper().translate(table_chiffrement)

    def dechiffrer_substitution(self, texte, cle):
        table_dechiffrement = str.maketrans(cle, self.alphabet)
        return texte.upper().translate(table_dechiffrement)

    def chiffrer_vigenere(self, texte, cle):
        texte = texte.upper()
        cle = cle.upper()
        resultat = ""
        cle_index = 0
        for char in texte:
            if char in self.alphabet:
                decalage = self.alphabet.index(cle[cle_index])
                index = (self.alphabet.index(char) + decalage) % 26
                resultat += self.alphabet[index]
                cle_index = (cle_index + 1) % len(cle)
            else:
                resultat += char
        return resultat

    def dechiffrer_vigenere(self, texte, cle):
        texte = texte.upper()
        cle = cle.upper()
        resultat = ""
        cle_index = 0
        for char in texte:
            if char in self.alphabet:
                decalage = self.alphabet.index(cle[cle_index])
                index = (self.alphabet.index(char) - decalage) % 26
                resultat += self.alphabet[index]
                cle_index = (cle_index + 1) % len(cle)
            else:
                resultat += char
        return resultat
