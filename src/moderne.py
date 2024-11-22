from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
import base64

class ChiffrementModerne:
    def chiffrer_aes(self, texte, cle):
        # Chiffrement AES
        cipher = AES.new(cle.encode('utf-8'), AES.MODE_ECB)
        texte_padding = self._pad(texte)
        return base64.b64encode(cipher.encrypt(texte_padding.encode('utf-8'))).decode('utf-8')
    
    def chiffrer_rsa(self, texte):
        # Chiffrement RSA
        key = RSA.generate(2048)
        cipher = PKCS1_OAEP.new(key.publickey())
        return base64.b64encode(cipher.encrypt(texte.encode('utf-8'))).decode('utf-8')
    
    def _pad(self, texte):
        # Padding pour AES
        return texte + (16 - len(texte) % 16) * chr(16 - len(texte) % 16)
