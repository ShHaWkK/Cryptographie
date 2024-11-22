# src/chiffrement.py

import string
import random
import numpy as np

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

    def dechiffrer_cesar(self, texte, decalage):
        return self.chiffrer_cesar(texte, -decalage)

    def chiffrer_substitution(self, texte, cle=None):
        if not cle:
            cle = ''.join(random.sample(self.alphabet, len(self.alphabet)))
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

    def chiffrer_hill(self, texte, cle):
        texte = ''.join(filter(str.isalpha, texte.upper()))
        n = int(len(cle) ** 0.5)
        cle_matrix = np.array([self.alphabet.index(c) for c in cle]).reshape((n, n))
        
        # Padding du texte si nécessaire
        while len(texte) % n != 0:
            texte += 'X'
        
        resultat = ""
        for i in range(0, len(texte), n):
            bloc = np.array([self.alphabet.index(c) for c in texte[i:i+n]])
            chiffre = np.dot(cle_matrix, bloc) % 26
            resultat += ''.join([self.alphabet[int(c)] for c in chiffre])
        
        return resultat

    def dechiffrer_hill(self, texte, cle):
        n = int(len(cle) ** 0.5)
        cle_matrix = np.array([self.alphabet.index(c) for c in cle]).reshape((n, n))
        inv_matrix = np.linalg.inv(cle_matrix)
        det = round(np.linalg.det(cle_matrix))
        adj_matrix = det * inv_matrix
        cle_inv = adj_matrix % 26
        
        return self.chiffrer_hill(texte, ''.join([self.alphabet[int(c) % 26] for c in cle_inv.flatten()]))

    def chiffrer_vernam(self, texte, cle):
        texte = ''.join(filter(str.isalpha, texte.upper()))
        cle = cle.upper()
        if len(cle) < len(texte):
            raise ValueError("La clé doit être au moins aussi longue que le texte")
        
        resultat = ""
        for t, k in zip(texte, cle):
            chiffre = (self.alphabet.index(t) + self.alphabet.index(k)) % 26
            resultat += self.alphabet[chiffre]
        return resultat

    def dechiffrer_vernam(self, texte, cle):
        texte = texte.upper()
        cle = cle.upper()
        resultat = ""
        for t, k in zip(texte, cle):
            dechiffre = (self.alphabet.index(t) - self.alphabet.index(k)) % 26
            resultat += self.alphabet[dechiffre]
        return resultat

    def chiffrer_beaufort(self, texte, cle):
        texte = ''.join(filter(str.isalpha, texte.upper()))
        cle = cle.upper()
        resultat = ""
        cle_index = 0
        for char in texte:
            k = self.alphabet.index(cle[cle_index])
            t = self.alphabet.index(char)
            chiffre = (k - t) % 26
            resultat += self.alphabet[chiffre]
            cle_index = (cle_index + 1) % len(cle)
        return resultat
 # Le chiffrement et le déchiffrement sont identiques pour Beaufort
    def dechiffrer_beaufort(self, texte, cle):
        return self.chiffrer_beaufort(texte, cle)

    def chiffrer_rail_fence(self, texte, rails):
        fence = [['\n' for _ in range(len(texte))] for _ in range(rails)]
        rail = 0
        direction = 1
        
        for i, char in enumerate(texte):
            fence[rail][i] = char
            rail += direction
            if rail == 0 or rail == rails - 1:
                direction = -direction
        
        return ''.join(char for rail in fence for char in rail if char != '\n')

    def dechiffrer_rail_fence(self, texte, rails):
        fence = [['\n' for _ in range(len(texte))] for _ in range(rails)]
        rail = 0
        direction = 1
        
        for i in range(len(texte)):
            fence[rail][i] = '*'
            rail += direction
            if rail == 0 or rail == rails - 1:
                direction = -direction
        
        index = 0
        for i in range(rails):
            for j in range(len(texte)):
                if fence[i][j] == '*' and index < len(texte):
                    fence[i][j] = texte[index]
                    index += 1
        
        rail = 0
        direction = 1
        resultat = ""
        for i in range(len(texte)):
            resultat += fence[rail][i]
            rail += direction
            if rail == 0 or rail == rails - 1:
                direction = -direction
        
        return resultat
