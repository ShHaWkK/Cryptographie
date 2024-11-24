import re
from collections import Counter
import matplotlib.pyplot as plt
from src.chiffrement import ChiffrementClassique

class AnalyseAvancee:
    def __init__(self):
        self.chiffrement = ChiffrementClassique()

    def attaque_dictionnaire(self, texte_chiffre, methode, dictionnaire):
        resultats = []
        for mot in dictionnaire:
            if methode == "cesar":
                for decalage in range(26):
                    dechiffre = self.chiffrement.dechiffrer_cesar(texte_chiffre, decalage)
                    if mot in dechiffre.lower():
                        resultats.append((decalage, dechiffre))
            elif methode == "vigenere":
                dechiffre = self.chiffrement.dechiffrer_vigenere(texte_chiffre, mot)
                if any(m in dechiffre.lower() for m in dictionnaire):
                    resultats.append((mot, dechiffre))
        return resultats

    def analyse_kasiski(self, texte_chiffre, longueur_min=3, longueur_max=10):
        repetitions = {}
        for longueur in range(longueur_min, longueur_max + 1):
            for i in range(len(texte_chiffre) - longueur):
                sequence = texte_chiffre[i:i+longueur]
                if sequence in texte_chiffre[i+1:]:
                    if sequence not in repetitions:
                        repetitions[sequence] = []
                    repetitions[sequence].append(i)
        
        distances = []
        for positions in repetitions.values():
            for i in range(len(positions) - 1):
                distances.append(positions[i+1] - positions[i])
        
        facteurs_communs = self.trouver_facteurs_communs(distances)
        return sorted(facteurs_communs.items(), key=lambda x: x[1], reverse=True)

    def trouver_facteurs_communs(self, nombres):
        facteurs = Counter()
        for nombre in nombres:
            for i in range(2, nombre + 1):
                if nombre % i == 0:
                    facteurs[i] += 1
        return facteurs

    def visualiser_frequences(self, texte):
        frequences = Counter(char.upper() for char in texte if char.isalpha())
        lettres = sorted(frequences.keys())
        valeurs = [frequences[lettre] for lettre in lettres]

        plt.figure(figsize=(12, 6))
        plt.bar(lettres, valeurs)
        plt.title("Fréquence des lettres")
        plt.xlabel("Lettres")
        plt.ylabel("Fréquence")
        plt.show()

