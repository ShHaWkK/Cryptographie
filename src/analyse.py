import string
from collections import Counter

class AnalyseCryptographique:
    def __init__(self):
        self.alphabet = string.ascii_uppercase
    
    def analyse_frequentielle(self, texte):
        # Analyse des fréquences des lettres
        frequences = Counter(char for char in texte.upper() if char in self.alphabet)
        total = sum(frequences.values())
        
        return {
            lettre: (count / total) * 100 
            for lettre, count in sorted(frequences.items(), key=lambda x: x[1], reverse=True)
        }
    
    def casser_cesar(self, texte_chiffre):
        # Tentative de cassage du chiffrement de César
        resultats = []
        for decalage in range(26):
            texte_dechiffre = ''.join(
                self.alphabet[(self.alphabet.index(char) - decalage) % 26] 
                if char in self.alphabet else char 
                for char in texte_chiffre
            )
            resultats.append((decalage, texte_dechiffre))
        return resultats
