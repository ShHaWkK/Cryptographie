import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTextEdit, QPushButton, 
                             QVBoxLayout, QHBoxLayout, QWidget, QFileDialog, 
                             QInputDialog, QMessageBox, QLabel, QComboBox, QDialog)
from PyQt5.QtGui import QFont
from src.chiffrement import ChiffrementClassique
from src.analyse_avancee import AnalyseAvancee
from src.traitement_fichiers import TraitementFichiers
from src.steganographie import Steganographie

class CryptoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Application de Cryptographie Avancée")
        self.setGeometry(100, 100, 800, 600)
        
        # Initialisation des composants de chiffrement
        self.chiffrement_classique = ChiffrementClassique()
        self.analyse_avancee = AnalyseAvancee()
        self.traitement_fichiers = TraitementFichiers()
        self.steganographie = Steganographie()
        
        self.init_ui()
    
    def init_ui(self):
        # Widget central et layout principal
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout_principal = QVBoxLayout(central_widget)
        
        # Zones de texte
        self.text_input = QTextEdit()
        self.text_output = QTextEdit()
        self.text_input.setPlaceholderText("Entrez votre texte ici...")
        self.text_output.setPlaceholderText("Le résultat apparaîtra ici...")
        
        # Labels
        input_label = QLabel("Texte d'entrée:")
        output_label = QLabel("Texte de sortie:")
        
        # Ajout des widgets au layout
        layout_principal.addWidget(input_label)
        layout_principal.addWidget(self.text_input)
        layout_principal.addWidget(output_label)
        layout_principal.addWidget(self.text_output)
        
        # Layout des contrôles
        layout_controles = QHBoxLayout()
        
        # Sélection de la méthode
        self.combo_methode = QComboBox()
        self.combo_methode.addItems([
            "César", "Substitution", "Vigenère", "Hill", "Vernam", 
            "Beaufort", "Rail Fence", "AES", "RSA", "Analyse Fréquentielle"
        ])
        
        layout_controles.addWidget(QLabel("Méthode:"))
        layout_controles.addWidget(self.combo_methode)
        
        # Boutons
        bouton_chiffrer = QPushButton("Chiffrer/Analyser")
        bouton_dechiffrer = QPushButton("Déchiffrer")
        bouton_charger = QPushButton("Charger")
        bouton_sauvegarder = QPushButton("Sauvegarder")
        
        bouton_chiffrer.clicked.connect(self.action_chiffrer)
        bouton_dechiffrer.clicked.connect(self.action_dechiffrer)
        bouton_charger.clicked.connect(self.charger_fichier)
        bouton_sauvegarder.clicked.connect(self.sauvegarder_fichier)

        # Boutons pour les nouvelles fonctionnalités
        bouton_analyse_avancee = QPushButton("Analyse Avancée")
        bouton_traitement_fichiers = QPushButton("Traitement Fichiers")
        bouton_steganographie = QPushButton("Stéganographie")

        bouton_analyse_avancee.clicked.connect(self.ouvrir_analyse_avancee)
        bouton_traitement_fichiers.clicked.connect(self.ouvrir_traitement_fichiers)
        bouton_steganographie.clicked.connect(self.ouvrir_steganographie)

        layout_controles.addWidget(bouton_chiffrer)
        layout_controles.addWidget(bouton_dechiffrer)
        layout_controles.addWidget(bouton_charger)
        layout_controles.addWidget(bouton_sauvegarder)

        layout_controles.addWidget(bouton_analyse_avancee)
        layout_controles.addWidget(bouton_traitement_fichiers)
        layout_controles.addWidget(bouton_steganographie)

        
         # Ajout du layout des contrôles au layout principal
         layout_principal.addLayout(layout_controles)

         # Stylisation
         self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QTextEdit {
                border: 1px solid #ccc;
                border-radius: 4px;
                padding: 5px;
                background-color: white;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 6px 12px;
                border: none;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QLabel {
                font-weight: bold;
            }
         """)
        
         # Police
         app_font = QFont("Arial", 10)
         self.setFont(app_font)

    def action_chiffrer(self):
         methode = self.combo_methode.currentText()
         texte = self.text_input.toPlainText()

         if methode == "César":
             decalage, ok = QInputDialog.getInt(self, "Chiffrement César", "Entrez le décalage:")
             if ok:
                 resultat = self.chiffrement_classique.chiffrer_cesar(texte, decalage)
                 self.text_output.setPlainText(resultat)

         elif methode == "Substitution":
             cle, ok = QInputDialog.getText(self, "Chiffrement par Substitution", 
                                             "Entrez la clé (laissez vide pour une clé aléatoire):")
             if ok:
                 resultat = self.chiffrement_classique.chiffrer_substitution(texte, cle if cle else None)
                 self.text_output.setPlainText(resultat)

         elif methode == "Vigenère":
             cle, ok = QInputDialog.getText(self, "Chiffrement de Vigenère", "Entrez la clé:")
             if ok:
                 resultat = self.chiffrement_classique.chiffrer_vigenere(texte, cle)
                 self.text_output.setPlainText(resultat)

         elif methode == "Hill":
             cle, ok = QInputDialog.getText(self, "Chiffrement de Hill", 
                                             "Entrez la clé (matrice sous forme de chaîne):")
             if ok:
                 try:
                     resultat = self.chiffrement_classique.chiffrer_hill(texte, cle)
                     self.text_output.setPlainText(resultat)
                 except Exception as e:
                     QMessageBox.warning(self, "Erreur", str(e))

         elif methode == "Vernam":
             cle, ok = QInputDialog.getText(self, "Chiffrement de Vernam", 
                                             "Entrez la clé (aussi longue que le texte):")
             if ok:
                 try:
                     resultat = self.chiffrement_classique.chiffrer_vernam(texte, cle)
                     self.text_output.setPlainText(resultat)
                 except ValueError as e:
                     QMessageBox.warning(self, "Erreur", str(e))

         elif methode == "Beaufort":
             cle, ok = QInputDialog.getText(self, "Chiffrement de Beaufort", 
                                             "Entrez la clé:")
             if ok:
                 resultat = self.chiffrement_classique.chiffrer_beaufort(texte, cle)
                 self.text_output.setPlainText(resultat)

         elif methode == "Rail Fence":
             rails, ok = QInputDialog.getInt(self, "Chiffrement Rail Fence", 
                                              "Entrez le nombre de rails:")
             if ok:
                 resultat = self.chiffrement_classique.chiffrer_rail_fence(texte, rails)
                 self.text_output.setPlainText(resultat)

         elif methode == "AES":
             cle, ok = QInputDialog.getText(self, "Chiffrement AES", 
                                             "Entrez la clé (16, 24 ou 32 caractères):")
             if ok and len(cle) in [16, 24, 32]:
                 resultat = self.chiffrement_classique.chiffrer_aes(texte.encode(), cle)  
                 self.text_output.setPlainText(resultat.decode())
             else:
                 QMessageBox.warning(self, "Erreur", 
                                     "La clé AES doit faire 16, 24 ou 32 caractères.")

         elif methode == "RSA":
             resultat = self.chiffrement_moderne.chiffrer_rsa(texte)  
             self.text_output.setPlainText(resultat)

         elif methode == "Analyse Fréquentielle":
             resultat = self.analyse_avancee.analyse_frequentielle(texte)  
             self.text_output.setPlainText(str(resultats))

    def action_dechiffrer(self):
         methode = self.combo_methode.currentText()
         texte = self.text_input.toPlainText()

         if methode == "César":
             decalage, ok = QInputDialog.getInt(self, "Déchiffrement César", 
                                                 "Entrez le décalage:")
             if ok:
                 resultat = self.chiffrement_classique.dechiffrer_cesar(texte, decalage)
                 self.text_output.setPlainText(resultat)

         elif methode == "Substitution":
             cle, ok = QInputDialog.getText(self,
                                             "Déchiffrement par Substitution", 
                                             "Entrez la clé:")
             if ok:
                 resultat = self.chiffrement_classique.dechiffrer_substitution(texte, cle)
                 self.text_output.setPlainText(resultat)

         elif methode == "Vigenère":
             cle, ok = QInputDialog.getText(self,
                                             "Déchiffrement de Vigenère",
                                             "Entrez la clé:")
             if ok:
                 resultat = self.chiffrement_classique.dechiffrer_vigenere(texte.encode(), cle)  
                 self.text_output.setPlainText(resultat.decode())

         elif methode == "Hill":
             cle ,ok=QInputDialog.getText(
                    Self,"Déchiffrement de Hill","Entrez la clé (matrice sous forme de chaîne):")
             
              if ok :
                  try :
                      resultat=self.chiffrement_classique.dechiffrer_hill(texte.encode(),cle)  
                      Self.text_output.setplaintext(resultat.decode())
                  except Exception as e :
                      QMessageBox.warning(Self,"Erreur ",str(e))

          elif methode=="Vernam" :
              cle ,ok=QInputDialog.gettext(
                  Self,"Déchiffer Vernam","Entrez la clé : ")
              If ok :
                  Try :
                      result=self.chffre_classique.dechiffer_vernam(text ,cle )  
                      text_output.setplaintext(result.decode())
                  Except ValueError as e :
                      QMessageBox.warning(Self,"Erreur ",str(e))

          elif methode=="Beaufort" :
              cle ,ok=QInputDialog.gettext(
                  Self,"Déchiffer Beaufort","Entrez la clé : ")
              If ok :
                  result=self.chffre_classique.dechiffer_beaufort(text ,cle )  
                  text_output.setplaintext(result.decode())

          elif methode=="Rail Fence" :
              rails ,ok=QInputDialog.getInt(
                  Self,"Déchiffer Rail Fence","Entrez le nombre de rails : ")
              If ok :
                  result=self.chffre_rail_fence.dechiffer_rail_fence(text ,rails )
                  text_output.setplaintext(result.decode())


          elif methode=="AES" :
              key ,ok=QInputDialog.gettext(
                  Self,"Déchiffer AES","Entrez la clé : ")
              If ok :
                  Try :
                      result=self.chffre_modern.dechiffer_aes(text ,key )
                      text_output.setplaintext(result.decode())
                  Except :
                      QMessageBox.warning(Self,"Erreur","Impossible de déchiffrer. Vérifiez la clé.")

          elif methode=="RSA" :
              QMessageBox.information(Self,"Information","Le déchiffre RSA n'est pas implémenté dans cette interface.")
          else :
              QMessageBox.information(Self,"Information","Opération non applicable pour cette méthode.")

    def charger_fichier(self):
         options = QFileDialog.Options()
         fileName,_=QFileDialog.getOpenFileName(
               Self,"Charger un fichier","","Fichiers texte (*.txt);;Tous les fichiers (*)",
               options=options )
         
          If fileName :
              Try :
                  With open(fileName,'r',encoding='utf-8') as file :
                      Self.text_input.setplaintext(file.read())
              Except Exception as e :
                  QMessageBox.warning(Self,"Erreur",
                                      f"Impossible de charger le fichier: {str(e)}")

    def sauvegarder_fichier(self):
          options=QFileDialog.Options()
          fileName,_=QFileDialog.getSaveFileName(
               Self,"Sauvegarder le fichier","","Fichiers texte (*.txt);;Tous les fichiers (*)",
               options=options )
          
          If fileName :
              Try :
                  With open(fileName,'w',encoding='utf-8') as file :
                      file.write(Self.text_output.toPlaintext())
                  QMessageBox.information(Self,"Succès","Fichier sauvegardé avec succès.")
              Except Exception as e :
                  QMessageBox.warning(Self,"Erreur",
                                      f"Impossible de sauvegarder le fichier: {str(e)}")

    def ouvrir_analyse_avancee(self):
          dialog=QDialog(Self)
          dialog.setWindowTitle("Analyse Cryptographique Avancée")
          layout=QVBoxLayout()

          bouton_dictionnaire=QPushButton("Attaque par Dictionnaire")
          bouton_kasiski=QPushButton("Analyse de Kasiski")
          bouton_frequences=QPushButton("Visualiser Fréquences")

          bouton_dictionnaire.clicked.connect(Self.attaque_dictionnaire)
          bouton_kasiski.clicked.connect(Self.analyse_kasiski)
          bouton_frequences.clicked.connect(Self.visualiser_frequences)

          layout.addWidget(bouton_dictionnaire)
          layout.addWidget(bouton_kasiski)
          layout.addWidget(bouton_frequences)

          dialog.setLayout(layout)
          dialog.exec_()

    def attaque_dictionnaire(Self):
           texte=Self.text_input.toPlaintext()
           methode ,ok=QInputDialog.getItem(Self,"Attaque par Dictionnaire",
                                            'Choisissez la méthode:',["cesar","vigenere"])
           If ok :
               dictionnaire=["le","la","les","un","une","des","et","est"]#Exemple simple
               resultats=Self.analyse_avancee.attaque_dictionnaire(texte,methode,dictionnaire )
               Self.text_output.setplaintext(str(resultats))

    def analyse_kasiski(Self):
           texte=Self.text_input.toPlaintext()
           resultats=Self.analyse_avancee.analyse_kasiski(texte )
           Self.text_output.setplaintext(str(resultats))

    def visualiser_frequences(Self):
           texte=Self.text_input.toPlaintext()
           Self.analyse_avancee.visualiser_frequences(texte )

    def ouvrir_traitement_fichiers(Self):
           chemin_entree,_=QFileDialog.getOpenFileName(Self,"Sélectionner le fichier d'entrée ")
           If chemin_entree :
               chemin_sortie,_=QFileDialog.getSaveFileName(Self,"Sélectionner le fichier de sortie ")
               If chemin_sortie :
                   methode ,ok=QInputDialog.getItem(Self,"Traitement de Fichiers",
                                                     'Choisissez la méthode:',["aes","cesar"])
                   If ok :
                       cle ,ok=QInputDialog.gettext(Self,"Traitement de Fichiers",
                                                     'Entrez la clé : ')
                       If ok :
                           action ,ok=QInputDialog.getItem(Self,"Traitement de Fichiers",
                                                            'Choisissez l\'action:',["chiffrer","dechiffrer"])
                           If ok :
                               Try :
                                   If action=="chiffrer" :
                                       Self.traitement_fichiers.chiffrer_fichier(
                                           chemin_entree ,chemin_sortie,methode ,cle )
                                   Else :
                                       Self.traitement_fichiers.dechiffrer_fichier(
                                           chemin_entree ,chemin_sortie,methode ,cle )
                                   QMessageBox.information(Self,"Succès","Opération réussie!")
                               Except Exception as e:
                                   QMessageBox.warning(Self,"Erreur ",str(e))

    def ouvrir_steganographie(Self):
           action ,ok=QInputDialog.getItem(Self,"Stéganographie",
                                            'Choisissez l\'action:',["cacher","extraire"])
           If ok :
               If action=="cacher" :
                   chemin_image,_=QFileDialog.getOpenFileName(Self,"Sélectionner l'image ")
                   If chemin_image :
                       message ,ok=QInputDialog.gettext(
                           Self,"Stéganographie ","Entrez le message à cacher : ")
                       If ok :
                           chemin_sortie,_=QFileDialog.getSaveFileName(
                               Self,"Sélectionner le fichier de sortie ")
                           If chemin_sortie :
                               Try :
                                   Self.steganographie.cacher_message(
                                       chemin_image,message ,chemin_sortie )
                                   QMessageBox.information(
                                       Self ,"Succès ","Message caché avec succès ! ")
                               Except Exception as e:
                                   QMessageBox.warning(
                                       Self ,"Erreur ",str(e))
               Else :#Extraire un message caché
                   chemin_image,_=QFileDialog.getOpenFileName(
                       Self ,"Sélectionner l'image ")
                   If chemin_image :#Extraire un message caché.
                       Try:
                           message=self.steganographie.extraire_message(chemin_image )
                           Self.text_output.setplaintext(f"Message extrait : {message}")
                       Except Exception as e:
                           QMessageBox.warning(
                               Self ,"Erreur ",str(e))


def main():
    app = QApplication(sys.argv)
    crypto_app = CryptoApp()
    crypto_app.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

