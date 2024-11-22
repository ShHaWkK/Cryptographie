import random
import re

def generer_cle_aleatoire():
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    random.shuffle(alphabet)
    return ''.join(alphabet)

def nettoyer_texte(texte):
    return re.sub(r'[^A-Z]', '', texte.upper())
