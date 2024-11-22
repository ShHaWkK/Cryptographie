import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTextEdit, QPushButton, 
                             QVBoxLayout, QHBoxLayout, QWidget, QFileDialog, 
                             QInputDialog, QMessageBox, QLabel, QComboBox)
from PyQt5.QtGui import QFont
from src.chiffrement import ChiffrementClassique
from src.analyse import AnalyseCryptographique
from src.moderne import ChiffrementModerne

class CryptoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Application de Cryptographie Avancée")
        self.setGeometry(100, 100, 800, 600)
        
        # Initialisation des composants de chiffrement
        self.chiffrement_classique = ChiffrementClassique()
        self.analyse = AnalyseCryptographique()
        self.chiffrement_moderne = ChiffrementModerne()
        
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
        
        layout_controles.addWidget(bouton_chiffrer)
        layout_controles.addWidget(bouton_dechiffrer)
        layout_controles.addWidget(bouton_charger)
        layout_controles.addWidget(bouton_sauvegarder)
        
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
            cle, ok = QInputDialog.getText(self, "Chiffrement par Substitution", "Entrez la clé (laissez vide pour une clé aléatoire):")
            if ok:
                resultat = self.chiffrement_classique.chiffrer_substitution(texte, cle if cle else None)
                self.text_output.setPlainText(resultat)
        elif methode == "Vigenère":
            cle, ok = QInputDialog.getText(self, "Chiffrement de Vigenère", "Entrez la clé:")
            if ok:
                resultat = self.chiffrement_classique.chiffrer_vigenere(texte, cle)
                self.text_output.setPlainText(resultat)
        elif methode == "Hill":
            cle, ok = QInputDialog.getText(self, "Chiffrement de Hill", "Entrez la clé (matrice sous forme de chaîne):")
            if ok:
                try:
                    resultat = self.chiffrement_classique.chiffrer_hill(texte, cle)
                    self.text_output.setPlainText(resultat)
                except Exception as e:
                    QMessageBox.warning(self, "Erreur", str(e))
        elif methode == "Vernam":
            cle, ok = QInputDialog.getText(self, "Chiffrement de Vernam", "Entrez la clé (aussi longue que le texte):")
            if ok:
                try:
                    resultat = self.chiffrement_classique.chiffrer_vernam(texte, cle)
                    self.text_output.setPlainText(resultat)
                except ValueError as e:
                    QMessageBox.warning(self, "Erreur", str(e))
        elif methode == "Beaufort":
            cle, ok = QInputDialog.getText(self, "Chiffrement de Beaufort", "Entrez la clé:")
            if ok:
                resultat = self.chiffrement_classique.chiffrer_beaufort(texte, cle)
                self.text_output.setPlainText(resultat)
        elif methode == "Rail Fence":
            rails, ok = QInputDialog.getInt(self, "Chiffrement Rail Fence", "Entrez le nombre de rails:")
            if ok:
                resultat = self.chiffrement_classique.chiffrer_rail_fence(texte, rails)
                self.text_output.setPlainText(resultat)
        elif methode == "AES":
            cle, ok = QInputDialog.getText(self, "Chiffrement AES", "Entrez la clé (16, 24 ou 32 caractères):")
            if ok and len(cle) in [16, 24, 32]:
                resultat = self.chiffrement_moderne.chiffrer_aes(texte, cle)
                self.text_output.setPlainText(resultat)
            else:
                QMessageBox.warning(self, "Erreur", "La clé AES doit faire 16, 24 ou 32 caractères.")
        elif methode == "RSA":
            resultat = self.chiffrement_moderne.chiffrer_rsa(texte)
            self.text_output.setPlainText(resultat)
        elif methode == "Analyse Fréquentielle":
            resultat = self.analyse.analyse_frequentielle(texte)
            self.text_output.setPlainText(str(resultat))
    
    def action_dechiffrer(self):
        methode = self.combo_methode.currentText()
        texte = self.text_input.toPlainText()
        
        if methode == "César":
            decalage, ok = QInputDialog.getInt(self, "Déchiffrement César", "Entrez le décalage:")
            if ok:
                resultat = self.chiffrement_classique.dechiffrer_cesar(texte, decalage)
                self.text_output.setPlainText(resultat)
        elif methode == "Substitution":
            cle, ok = QInputDialog.getText(self, "Déchiffrement par Substitution", "Entrez la clé:")
            if ok:
                resultat = self.chiffrement_classique.dechiffrer_substitution(texte, cle)
                self.text_output.setPlainText(resultat)
        elif methode == "Vigenère":
            cle, ok = QInputDialog.getText(self, "Déchiffrement de Vigenère", "Entrez la clé:")
            if ok:
                resultat = self.chiffrement_classique.dechiffrer_vigenere(texte, cle)
                self.text_output.setPlainText(resultat)
        elif methode == "Hill":
            cle, ok = QInputDialog.getText(self, "Déchiffrement de Hill", "Entrez la clé (matrice sous forme de chaîne):")
            if ok:
                try:
                    resultat = self.chiffrement_classique.dechiffrer_hill(texte, cle)
                    self.text_output.setPlainText(resultat)
                except Exception as e:
                    QMessageBox.warning(self, "Erreur", str(e))
        elif methode == "Vernam":
            cle, ok = QInputDialog.getText(self, "Déchiffrement de Vernam", "Entrez la clé:")
            if ok:
                try:
                    resultat = self.chiffrement_classique.dechiffrer_vernam(texte, cle)
                    self.text_output.setPlainText(resultat)
                except ValueError as e:
                    QMessageBox.warning(self, "Erreur", str(e))
        elif methode == "Beaufort":
            cle, ok = QInputDialog.getText(self, "Déchiffrement de Beaufort", "Entrez la clé:")
            if ok:
                resultat = self.chiffrement_classique.dechiffrer_beaufort(texte, cle)
                self.text_output.setPlainText(resultat)
        elif methode == "Rail Fence":
            rails, ok = QInputDialog.getInt(self, "Déchiffrement Rail Fence", "Entrez le nombre de rails:")
            if ok:
                resultat = self.chiffrement_classique.dechiffrer_rail_fence(texte, rails)
                self.text_output.setPlainText(resultat)
        elif methode == "AES":
            cle, ok = QInputDialog.getText(self, "Déchiffrement AES", "Entrez la clé:")
            if ok:
                try:
                    resultat = self.chiffrement_moderne.dechiffrer_aes(texte, cle)
                    self.text_output.setPlainText(resultat)
                except:
                    QMessageBox.warning(self, "Erreur", "Impossible de déchiffrer. Vérifiez la clé.")
        elif methode == "RSA":
            QMessageBox.information(self, "Information", "Le déchiffrement RSA n'est pas implémenté dans cette interface.")
        else:
            QMessageBox.information(self, "Information", "Opération non applicable pour cette méthode.")
    
    def charger_fichier(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Charger un fichier", "", "Fichiers texte (*.txt);;Tous les fichiers (*)", options=options)
        if fileName:
            try:
                with open(fileName, 'r', encoding='utf-8') as file:
                    self.text_input.setPlainText(file.read())
            except Exception as e:
                QMessageBox.warning(self, "Erreur", f"Impossible de charger le fichier: {str(e)}")
    
    def sauvegarder_fichier(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "Sauvegarder le fichier", "", "Fichiers texte (*.txt);;Tous les fichiers (*)", options=options)
        if fileName:
            try:
                with open(fileName, 'w', encoding='utf-8') as file:
                    file.write(self.text_output.toPlainText())
                QMessageBox.information(self, "Succès", "Fichier sauvegardé avec succès.")
            except Exception as e:
                QMessageBox.warning(self, "Erreur", f"Impossible de sauvegarder le fichier: {str(e)}")

def main():
    app = QApplication(sys.argv)
    crypto_app = CryptoApp()
    crypto_app.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
