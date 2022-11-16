import Chapitre
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="ldvelh"
)

from PyQt5 import QtCore, QtGui, QtWidgets
from Menuaccueil import Ui_MainWindow
from Chapitre import Ui_Dialog as ChapitreDialog

import sys

# Fonction qui sélectionne le livre
def selectionLivre():
  # Création du curseur
  mycursor = mydb.cursor()

  requeteLivre = "SELECT titre FROM livre"

  mycursor.execute(requeteLivre)

  # Le curseur récupère toutes les données du résultat de la requête
  myresult = mycursor.fetchall()

  for (titre) in myresult:
    ui.comboBoxLivre.addItem(titre[0])

# Fonction qui sélectionne le prologue
def selectionPrologue():
  # Création du curseur
  mycursor = mydb.cursor()

  requetePrologue = "SELECT prologue.titre, prologue.texte FROM prologue INNER JOIN livre on prologue.id = livre.id WHERE livre.id = 1"

  mycursor.execute(requetePrologue)

  # Le curseur récupère toutes les données du résultat de la requête
  myresult = mycursor.fetchall()

  for (prologue) in myresult:
    uichapitre.labelChapitreNo.setText(prologue[0])
    uichapitre.labelTexteChapitre.setText(prologue[1])

# Fonction qui insert le personnage créé par le joueur dans la BD
def insertionPersonnage():
    mycursor = mydb.cursor()

    sql = "INSERT INTO personnage (nom, livre_id) VALUES (%s, %s)"
    val_nom = ui.textEditNomPersonnage.toPlainText()
    val_livre_id = 1

    mycursor.execute(sql, (val_nom, val_livre_id))

    mydb.commit()

def afficheChapitre():
    chapitre.show()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

selectionLivre()

#Création de la boite de dialogue Chapitre
chapitre = QtWidgets.QDialog()
uichapitre = ChapitreDialog()
uichapitre.setupUi(chapitre)

MainWindow.show()

ui.pushButtonDebutPartie.clicked.connect(afficheChapitre)

ui.pushButtonDebutPartie.clicked.connect(insertionPersonnage)

selectionPrologue()

sys.exit(app.exec_())

#setText("clément")