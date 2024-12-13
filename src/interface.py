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
    def __init__(selt):
        super().__init__()
        selt.setWindowTitle("Application de Cryptographie Avancée")
        selt.setGeometry(100, 100, 800, 600)
        
        # Initialisation des composants de chiffrement
        selt.chiffrement_classique = ChiffrementClassique()
        selt.analyse_avancee = AnalyseAvancee()
        selt.traitement_fichiers = TraitementFichiers()
        selt.steganographie = Steganographie()
        
        selt.init_ui()
    
    def init_ui(selt):
        # Widget central et layout principal
        central_widget = QWidget(selt)
        selt.setCentralWidget(central_widget)
        layout_principal = QVBoxLayout(central_widget)
        
        # Zones de texte
        selt.text_input = QTextEdit()
        selt.text_output = QTextEdit()
        selt.text_input.setPlaceholderText("Entrez votre texte ici...")
        selt.text_output.setPlaceholderText("Le résultat apparaîtra ici...")
        
        # Labels
        input_label = QLabel("Texte d'entrée:")
        output_label = QLabel("Texte de sortie:")
        
        # Ajout des widgets au layout
        layout_principal.addWidget(input_label)
        layout_principal.addWidget(selt.text_input)
        layout_principal.addWidget(output_label)
        layout_principal.addWidget(selt.text_output)
        
        # Layout des contrôles
        layout_controles = QHBoxLayout()
        
        # Sélection de la méthode
        selt.combo_methode = QComboBox()
        selt.combo_methode.addItems([
            "César", "Substitution", "Vigenère", "Hill", "Vernam", 
            "Beaufort", "Rail Fence", "AES", "RSA", "Analyse Fréquentielle"
        ])
        
        layout_controles.addWidget(QLabel("Méthode:"))
        layout_controles.addWidget(selt.combo_methode)
        
        # Boutons
        bouton_chiffrer = QPushButton("Chiffrer/Analyser")
        bouton_dechiffrer = QPushButton("Déchiffrer")
        bouton_charger = QPushButton("Charger")
        bouton_sauvegarder = QPushButton("Sauvegarder")
        
        bouton_chiffrer.clicked.connect(selt.action_chiffrer)
        bouton_dechiffrer.clicked.connect(selt.action_dechiffrer)
        bouton_charger.clicked.connect(selt.charger_fichier)
        bouton_sauvegarder.clicked.connect(selt.sauvegarder_fichier)

        # Boutons pour les nouvelles fonctionnalités
        bouton_analyse_avancee = QPushButton("Analyse Avancée")
        bouton_traitement_fichiers = QPushButton("Traitement Fichiers")
        bouton_steganographie = QPushButton("Stéganographie")

        bouton_analyse_avancee.clicked.connect(selt.ouvrir_analyse_avancee)
        bouton_traitement_fichiers.clicked.connect(selt.ouvrir_traitement_fichiers)
        bouton_steganographie.clicked.connect(selt.ouvrir_steganographie)

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
        selt.setStyleSheet("""
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
        selt.setFont(app_font)

    def action_chiffrer(selt):
         methode = selt.combo_methode.currentText()
         texte = selt.text_input.toPlainText()

         if methode == "César":
             decalage, ok = QInputDialog.getInt(selt, "Chiffrement César", "Entrez le décalage:")
             if ok:
                 resultat = selt.chiffrement_classique.chiffrer_cesar(texte, decalage)
                 selt.text_output.setPlainText(resultat)

         elif methode == "Substitution":
             cle, ok = QInputDialog.getText(selt, "Chiffrement par Substitution", 
                                             "Entrez la clé (laissez vide pour une clé aléatoire):")
             if ok:
                 resultat = selt.chiffrement_classique.chiffrer_substitution(texte, cle if cle else None)
                 selt.text_output.setPlainText(resultat)

         elif methode == "Vigenère":
             cle, ok = QInputDialog.getText(selt, "Chiffrement de Vigenère", "Entrez la clé:")
             if ok:
                 resultat = selt.chiffrement_classique.chiffrer_vigenere(texte, cle)
                 selt.text_output.setPlainText(resultat)

         elif methode == "Hill":
             cle, ok = QInputDialog.getText(selt, "Chiffrement de Hill", 
                                             "Entrez la clé (matrice sous forme de chaîne):")
             if ok:
                 try:
                     resultat = selt.chiffrement_classique.chiffrer_hill(texte, cle)
                     selt.text_output.setPlainText(resultat)
                 except exception as e:
                     QMessageBox.warning(selt, "Erreur", str(e))

         elif methode == "Vernam":
             cle, ok = QInputDialog.getText(selt, "Chiffrement de Vernam", 
                                             "Entrez la clé (aussi longue que le texte):")
             if ok:
                 try:
                     resultat = selt.chiffrement_classique.chiffrer_vernam(texte, cle)
                     selt.text_output.setPlainText(resultat)
                 except ValueError as e:
                     QMessageBox.warning(selt, "Erreur", str(e))

         elif methode == "Beaufort":
             cle, ok = QInputDialog.getText(selt, "Chiffrement de Beaufort", 
                                             "Entrez la clé:")
             if ok:
                 resultat = selt.chiffrement_classique.chiffrer_beaufort(texte, cle)
                 selt.text_output.setPlainText(resultat)

         elif methode == "Rail Fence":
             rails, ok = QInputDialog.getInt(selt, "Chiffrement Rail Fence", 
                                              "Entrez le nombre de rails:")
             if ok:
                 resultat = selt.chiffrement_classique.chiffrer_rail_fence(texte, rails)
                 selt.text_output.setPlainText(resultat)

         elif methode == "AES":
             cle, ok = QInputDialog.getText(selt, "Chiffrement AES", 
                                             "Entrez la clé (16, 24 ou 32 caractères):")
             if ok and len(cle) in [16, 24, 32]:
                 resultat = selt.chiffrement_classique.chiffrer_aes(texte.encode(), cle)  
                 selt.text_output.setPlainText(resultat.decode())
             else:
                 QMessageBox.warning(selt, "Erreur", 
                                     "La clé AES doit faire 16, 24 ou 32 caractères.")

         elif methode == "RSA":
             resultat = selt.chiffrement_moderne.chiffrer_rsa(texte)  
             selt.text_output.setPlainText(resultat)

         elif methode == "Analyse Fréquentielle":
             resultat = selt.analyse_avancee.analyse_frequentielle(texte)  
             selt.text_output.setPlainText(str(resultats))

    def action_dechiffrer(selt):
         methode = selt.combo_methode.currentText()
         texte = selt.text_input.toPlainText()

         if methode == "César":
             decalage, ok = QInputDialog.getInt(selt, "Déchiffrement César", 
                                                 "Entrez le décalage:")
             if ok:
                 resultat = selt.chiffrement_classique.dechiffrer_cesar(texte, decalage)
                 selt.text_output.setPlainText(resultat)

         elif methode == "Substitution":
             cle, ok = QInputDialog.getText(selt,
                                             "Déchiffrement par Substitution", 
                                             "Entrez la clé:")
             if ok:
                 resultat = selt.chiffrement_classique.dechiffrer_substitution(texte, cle)
                 selt.text_output.setPlainText(resultat)

         elif methode == "Vigenère":
             cle, ok = QInputDialog.getText(selt,
                "Déchiffrement de Vigenère",
                "Entrez la clé:")
             if ok:
                 resultat = selt.chiffrement_classique.dechiffrer_vigenere(texte.encode(), cle)  
                 selt.text_output.setPlainText(resultat.decode())

         elif methode == "Hill":
             cle ,ok=QInputDialog.getText(
                    selt,"Déchiffrement de Hill","Entrez la clé (matrice sous forme de chaîne):")
             if ok :
                  try :
                      resultat=selt.chiffrement_classique.dechiffrer_hill(texte.encode(),cle)  
                      selt.text_output.setplaintext(resultat.decode())
                  except exception as e :
                      QMessageBox.warning(selt,"Erreur ",str(e))


         elif methode=="Vernam" :
              cle ,ok=QInputDialog.gettext(
                  selt,"Déchiffer Vernam","Entrez la clé : ")
              if ok :
                    try :
                        result=selt.chffre_classique.dechiffer_vernam(text ,cle )  
                        text_output.setplaintext(result.decode())
                    except ValueError as e :
                        QMessageBox.warning(selt,"Erreur ",str(e))
            
         elif methode=="Beaufort" :
                cle ,ok=QInputDialog.gettext(
                    selt,"Déchiffer Beaufort","Entrez la clé : ")
                if ok :
                    result=selt.chffre_classique.dechiffer_beaufort(text ,cle )
                    text_output.setplaintext(result.decode())


         elif methode=="Rail Fence" :
              rails ,ok=QInputDialog.getInt(
                  selt,"Déchiffer Rail Fence","Entrez le nombre de rails : ")
              if ok :
                  result=selt.chffre_rail_fence.dechiffer_rail_fence(text ,rails )
                  text_output.setplaintext(result.decode())


         elif methode=="AES" :
              key ,ok=QInputDialog.gettext(
                  selt,"Déchiffer AES","Entrez la clé : ")
              if ok :
                  try :
                      result=selt.chffre_modern.dechiffer_aes(text ,key )
                      text_output.setplaintext(result.decode())
                  except :
                      QMessageBox.warning(selt,"Erreur","Impossible de déchiffrer. Vérifiez la clé.")

         elif methode=="RSA" :
              QMessageBox.information(selt,"Information","Le déchiffre RSA n'est pas implémenté dans cette interface.")
         else : 
                QMessageBox.information(selt,"Information","La méthode sélectionnée n'a pas de déchiffrement associé.")

    def charger_fichier(selt):
         options = QFileDialog.Options()
         fileName,_=QFileDialog.getOpenFileName(
               selt,"Charger un fichier","","Fichiers texte (*.txt);;Tous les fichiers (*)",
               options=options )
         
         if fileName :
              try :
                  with open(fileName,'r',encoding='utf-8') as file :
                      selt.text_input.setplaintext(file.read())
              except exception as e :
                  QMessageBox.warning(selt,"Erreur",
                                      f"Impossible de charger le fichier: {str(e)}")

    def sauvegarder_fichier(selt):
          options=QFileDialog.Options()
          fileName,_=QFileDialog.getSaveFileName(
               selt,"Sauvegarder le fichier","","Fichiers texte (*.txt);;Tous les fichiers (*)",
               options=options )
          
          if fileName :
              try :
                  with open(fileName,'w',encoding='utf-8') as file :
                      file.write(selt.text_output.toPlaintext())
                  QMessageBox.information(selt,"Succès","Fichier sauvegardé avec succès.")
              except exception as e :
                  QMessageBox.warning(selt,"Erreur",
                                      f"Impossible de sauvegarder le fichier: {str(e)}")

    def ouvrir_analyse_avancee(selt):
          dialog=QDialog(selt)
          dialog.setWindowTitle("Analyse Cryptographique Avancée")
          layout=QVBoxLayout()

          bouton_dictionnaire=QPushButton("Attaque par Dictionnaire")
          bouton_kasiski=QPushButton("Analyse de Kasiski")
          bouton_frequences=QPushButton("Visualiser Fréquences")

          bouton_dictionnaire.clicked.connect(selt.attaque_dictionnaire)
          bouton_kasiski.clicked.connect(selt.analyse_kasiski)
          bouton_frequences.clicked.connect(selt.visualiser_frequences)

          layout.addWidget(bouton_dictionnaire)
          layout.addWidget(bouton_kasiski)
          layout.addWidget(bouton_frequences)

          dialog.setLayout(layout)
          dialog.exec_()

    def attaque_dictionnaire(selt):
           texte=selt.text_input.toPlaintext()
           methode ,ok=QInputDialog.getItem(selt,"Attaque par Dictionnaire",
                                            'Choisissez la méthode:',["cesar","vigenere"])
           if ok :
               dictionnaire=["le","la","les","un","une","des","et","est"]#Exemple simple
               resultats=selt.analyse_avancee.attaque_dictionnaire(texte,methode,dictionnaire )
               selt.text_output.setplaintext(str(resultats))

    def analyse_kasiski(selt):
           texte=selt.text_input.toPlaintext()
           resultats=selt.analyse_avancee.analyse_kasiski(texte )
           selt.text_output.setplaintext(str(resultats))

    def visualiser_frequences(selt):
           texte=selt.text_input.toPlaintext()
           selt.analyse_avancee.visualiser_frequences(texte )

    def ouvrir_traitement_fichiers(selt):
           chemin_entree,_=QFileDialog.getOpenFileName(selt,"Sélectionner le fichier d'entrée ")
           if chemin_entree :
               chemin_sortie,_=QFileDialog.getSaveFileName(selt,"Sélectionner le fichier de sortie ")
               if chemin_sortie :
                   methode ,ok=QInputDialog.getItem(selt,"Traitement de Fichiers",
                                                     'Choisissez la méthode:',["aes","cesar"])
                   if ok :
                       cle ,ok=QInputDialog.gettext(selt,"Traitement de Fichiers",
                                                     'Entrez la clé : ')
                       if ok :
                           action ,ok=QInputDialog.getItem(selt,"Traitement de Fichiers",
                                                            'Choisissez l\'action:',["chiffrer","dechiffrer"])
                           if ok :
                               try :
                                   if action=="chiffrer" :
                                       selt.traitement_fichiers.chiffrer_fichier(
                                           chemin_entree ,chemin_sortie,methode ,cle )
                                   else :
                                       selt.traitement_fichiers.dechiffrer_fichier(
                                           chemin_entree ,chemin_sortie,methode ,cle )
                                   QMessageBox.information(selt,"Succès","Opération réussie!")
                               except exception as e:
                                   QMessageBox.warning(selt,"Erreur ",str(e))

    def ouvrir_steganographie(selt):
           action ,ok=QInputDialog.getItem(selt,"Stéganographie",
                                            'Choisissez l\'action:',["cacher","extraire"])
           if ok :
               if action=="cacher" :
                   chemin_image,_=QFileDialog.getOpenFileName(selt,"Sélectionner l'image ")
                   if chemin_image :
                       message ,ok=QInputDialog.gettext(
                           selt,"Stéganographie ","Entrez le message à cacher : ")
                       if ok :
                           chemin_sortie,_=QFileDialog.getSaveFileName(
                               selt,"Sélectionner le fichier de sortie ")
                           if chemin_sortie :
                               try :
                                   selt.steganographie.cacher_message(
                                       chemin_image,message ,chemin_sortie )
                                   QMessageBox.information(
                                       selt ,"Succès ","Message caché avec succès ! ")
                               except exception as e:
                                   QMessageBox.warning(
                                       selt ,"Erreur ",str(e))
               else :#Extraire un message caché
                   chemin_image,_=QFileDialog.getOpenFileName(
                       selt ,"Sélectionner l'image ")
                   if chemin_image :#Extraire un message caché.
                       try:
                           message=selt.steganographie.extraire_message(chemin_image )
                           selt.text_output.setplaintext(f"Message extrait : {message}")
                       except exception as e:
                           QMessageBox.warning(
                               selt ,"Erreur ",str(e))


def main():
    app = QApplication(sys.argv)
    crypto_app = CryptoApp()
    crypto_app.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

