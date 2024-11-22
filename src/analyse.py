class AnalyseCryptographique:
    def __init__(self):
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def analyser_frequences(self, texte):
        frequences = {}
        for char in texte.upper():
            if char in self.alphabet:
                frequences[char] = frequences.get(char, 0) + 1
        return dict(sorted(frequences.items(), key=lambda x: x[1], reverse=True))

    def casser_cesar(self, texte_chiffre):
        resultats = []
        for decalage in range(26):
            texte_dechiffre = ChiffrementSubstitution().dechiffrer_cesar(texte_chiffre, decalage)
            resultats.append((decalage, texte_dechiffre))
        return resultats

from src.chiffrement import ChiffrementSubstitution
