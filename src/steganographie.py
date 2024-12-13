######################################################
#                   EXPLICATIONS                     #
#   Author:  ShHawk                                  #
#   La classe Steganographie contient deux méthodes  #
#   principales : cacher_message et extraire_message.#
#                                                    #
#   La méthode cacher_message prend en paramètres    #
#   le chemin de l'image à laquelle on veut cacher le#
#   message, le message à cacher et le chemin de     #
#   l'image de sortie.                               #
#                                                    #
#   La méthode extraire_message prend en paramètre   #
#   le chemin de l'image à partir de laquelle on veut#
#   extraire le message caché.                       #
#                                                    #
######################################################

from PIL import Image
import numpy as np

class Steganographie:

    # Méthode pour cacher un message dans une image
    def cacher_message(self, chemin_image, message, chemin_sortie):
        img = Image.open(chemin_image)
        largeur, hauteur = img.size
        array = np.array(list(img.getdata()))

        # Vérification du mode de l'image
        if img.mode == 'RGB':
            n = 3
        # Si l'image est en mode RGBA
        elif img.mode == 'RGBA':
            n = 4

        total_pixels = array.size // n

        message += "≈"  # Caractère de fin de message
        b_message = ''.join([format(ord(i), "08b") for i in message])
        req_pixels = len(b_message)

        # Vérification de la taille du message
        if req_pixels > total_pixels:
            raise ValueError("La taille du message est trop grande pour cette image")

        index = 0
        # Cacher le message dans l'image en faisant un remplacement bit à bit
        for p in range(total_pixels):
            for q in range(0, 3):
                if index < req_pixels:
                    array[p][q] = int(bin(array[p][q])[2:9] + b_message[index], 2)
                    index += 1

        array = array.reshape(hauteur, largeur, n)
        enc_img = Image.fromarray(array.astype('uint8'), img.mode)
        enc_img.save(chemin_sortie)

    # Méthode pour extraire un message caché dans une image

    def extraire_message(self, chemin_image):
        img = Image.open(chemin_image)
        array = np.array(list(img.getdata()))

        if img.mode == 'RGB':
            n = 3
        elif img.mode == 'RGBA':
            n = 4

        total_pixels = array.size // n

        hidden_bits = ""
        # Extraire le message caché dans l'image en récupérant les bits de poids faible
        for p in range(total_pixels):
            for q in range(0, 3):
                hidden_bits += (bin(array[p][q])[2:][-1])

        hidden_bits = [hidden_bits[i:i+8] for i in range(0, len(hidden_bits), 8)]

        message = ""
        for i in range(len(hidden_bits)):
            if message[-2:] == "≈":  
                break
            else:
                message += chr(int(hidden_bits[i], 2))
        
        return message[:-1]  


