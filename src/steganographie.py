from PIL import Image
import numpy as np

class Steganographie:
    def cacher_message(self, chemin_image, message, chemin_sortie):
        img = Image.open(chemin_image)
        largeur, hauteur = img.size
        array = np.array(list(img.getdata()))

        if img.mode == 'RGB':
            n = 3
        elif img.mode == 'RGBA':
            n = 4

        total_pixels = array.size // n

        message += "≈"  # Caractère de fin de message
        b_message = ''.join([format(ord(i), "08b") for i in message])
        req_pixels = len(b_message)

        if req_pixels > total_pixels:
            raise ValueError("La taille du message est trop grande pour cette image")

        index = 0
        for p in range(total_pixels):
            for q in range(0, 3):
                if index < req_pixels:
                    array[p][q] = int(bin(array[p][q])[2:9] + b_message[index], 2)
                    index += 1

        array = array.reshape(hauteur, largeur, n)
        enc_img = Image.fromarray(array.astype('uint8'), img.mode)
        enc_img.save(chemin_sortie)

    def extraire_message(self, chemin_image):
        img = Image.open(chemin_image)
        array = np.array(list(img.getdata()))

        if img.mode == 'RGB':
            n = 3
        elif img.mode == 'RGBA':
            n = 4

        total_pixels = array.size // n

        hidden_bits = ""
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

