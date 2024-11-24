import os
from src.chiffrement import ChiffrementClassique
from src.moderne import ChiffrementModerne

class TraitementFichiers:
    def __init__(self):
        self.chiffrement_classique = ChiffrementClassique()
        self.chiffrement_moderne = ChiffrementModerne()

    def chiffrer_fichier(self, chemin_entree, chemin_sortie, methode, cle):
        with open(chemin_entree, 'rb') as f_entree:
            contenu = f_entree.read()
        
        if methode == "aes":
            contenu_chiffre = self.chiffrement_moderne.chiffrer_aes(contenu, cle)
        elif methode == "cesar":
            contenu_chiffre = self.chiffrement_classique.chiffrer_cesar(contenu.decode(), int(cle)).encode()
        else:
            raise ValueError("Méthode de chiffrement non supportée")

        with open(chemin_sortie, 'wb') as f_sortie:
            f_sortie.write(contenu_chiffre)

    def dechiffrer_fichier(self, chemin_entree, chemin_sortie, methode, cle):
        with open(chemin_entree, 'rb') as f_entree:
            contenu_chiffre = f_entree.read()
        
        if methode == "aes":
            contenu = self.chiffrement_moderne.dechiffrer_aes(contenu_chiffre, cle)
        elif methode == "cesar":
            contenu = self.chiffrement_classique.dechiffrer_cesar(contenu_chiffre.decode(), int(cle)).encode()
        else:
            raise ValueError("Méthode de déchiffrement non supportée")

        with open(chemin_sortie, 'wb') as f_sortie:
            f_sortie.write(contenu)

