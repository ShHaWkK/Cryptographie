from src.chiffrement import ChiffrementSubstitution
from src.analyse import AnalyseCryptographique
from src.utils import generer_cle_aleatoire, nettoyer_texte

def menu():
    chiffrement = ChiffrementSubstitution()
    analyse = AnalyseCryptographique()

    while True:
        print("\n--- Menu Chiffrement par Substitution ---")
        print("1. Chiffrer (César)")
        print("2. Déchiffrer (César)")
        print("3. Chiffrer (Substitution monoalphabétique)")
        print("4. Déchiffrer (Substitution monoalphabétique)")
        print("5. Chiffrer (Vigenère)")
        print("6. Déchiffrer (Vigenère)")
        print("7. Analyser les fréquences")
        print("8. Casser le chiffrement de César")
        print("9. Quitter")

        choix = input("Choisissez une option : ")

        if choix == '1':
            texte = input("Entrez le texte à chiffrer : ")
            decalage = int(input("Entrez le décalage : "))
            print("Texte chiffré :", chiffrement.chiffrer_cesar(texte, decalage))
        elif choix == '2':
            texte = input("Entrez le texte à déchiffrer : ")
            decalage = int(input("Entrez le décalage : "))
            print("Texte déchiffré :", chiffrement.dechiffrer_cesar(texte, decalage))
        elif choix == '3':
            texte = input("Entrez le texte à chiffrer : ")
            cle = input("Entrez la clé de substitution (26 lettres uniques) ou laissez vide pour une clé aléatoire : ")
            if not cle:
                cle = generer_cle_aleatoire()
                print("Clé générée :", cle)
            print("Texte chiffré :", chiffrement.chiffrer_substitution(texte, cle))
        elif choix == '4':
            texte = input("Entrez le texte à déchiffrer : ")
            cle = input("Entrez la clé de substitution (26 lettres uniques) : ")
            print("Texte déchiffré :", chiffrement.dechiffrer_substitution(texte, cle))
        elif choix == '5':
            texte = input("Entrez le texte à chiffrer : ")
            cle = input("Entrez la clé Vigenère : ")
            print("Texte chiffré :", chiffrement.chiffrer_vigenere(texte, cle))
        elif choix == '6':
            texte = input("Entrez le texte à déchiffrer : ")
            cle = input("Entrez la clé Vigenère : ")
            print("Texte déchiffré :", chiffrement.dechiffrer_vigenere(texte, cle))
        elif choix == '7':
            texte = input("Entrez le texte à analyser : ")
            print("Analyse des fréquences :", analyse.analyser_frequences(texte))
        elif choix == '8':
            texte = input("Entrez le texte chiffré : ")
            resultats = analyse.casser_cesar(texte)
            for decalage, texte_dechiffre in resultats:
                print(f"Décalage {decalage}: {texte_dechiffre[:50]}...")
        elif choix == '9':
            print("Au revoir !")
            break
        else:
            print("Option invalide. Veuillez réessayer.")
