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

# Fonction qui sélectionne l'arme
def selectionArmePersonnage():
  # Création du curseur
  mycursor = mydb.cursor()

  requeteArmePersonnage = "SELECT id, nom FROM arme"

  mycursor.execute(requeteArmePersonnage)

  # Le curseur récupère toutes les données du résultat de la requête
  myresult = mycursor.fetchall()

  for (arme) in myresult:
    ui.comboBoxArmePersonnage.addItem(arme[1],arme[0])

# Fonction qui sélectionne les disciplines
def selectionDisciplinePersonnage():
  # Création du curseur
  mycursor = mydb.cursor()

  requeteDisciplinePersonnage = "SELECT nom FROM discipline"

  mycursor.execute(requeteDisciplinePersonnage)

  # Le curseur récupère toutes les données du résultat de la requête
  myresult = mycursor.fetchall()

  for (discipline) in myresult:
    ui.comboBoxDisciplinePersonnage_1.addItem(discipline[0])
    ui.comboBoxDisciplinePersonnage_2.addItem(discipline[0])
    ui.comboBoxDisciplinePersonnage_3.addItem(discipline[0])
    ui.comboBoxDisciplinePersonnage_4.addItem(discipline[0])
    ui.comboBoxDisciplinePersonnage_5.addItem(discipline[0])


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

  return mycursor.lastrowid

def recupererIdPersonnage():
  mycursor = mydb.cursor()
  sql = "SELECT id FROM personnage WHERE id = LAST_INSERT_ID()"

  mycursor.execute(sql,)

  myresult = mycursor.fetchall()

  return myresult

    
# Fonction qui insert l'arme du personnage dans la BD
def insertionArme(val_personnage_id):
  mycursor = mydb.cursor()

  sql = "INSERT INTO personnage_arme (personnage_id, arme_id) VALUES (%s, %s)"
  val_arme_id = ui.comboBoxArmePersonnage.itemData(ui.comboBoxArmePersonnage.currentIndex())
  #val_personnage_id = recupererIdPersonnage()[0][0]

  mycursor.execute(sql, (val_personnage_id, val_arme_id))

  mydb.commit()

# Fonction qui insert les disciplines du personnage dans la BD
def insertionDiscipline1(val_personnage_id):
  mycursor = mydb.cursor()

  sql = "INSERT INTO personnage_discipline (personnage_id, discipline_id) VALUES (%s, %s)"
  val_discipline1_id = ui.comboBoxArmePersonnage.itemData(ui.comboBoxDisciplinePersonnage_1.currentIndex())
  #val_personnage_id = recupererIdPersonnage()[0][0]

  mycursor.execute(sql, (val_personnage_id, val_discipline1_id))

  mydb.commit()

# Fonction qui insert les disciplines du personnage dans la BD
def insertionDiscipline2(val_personnage_id):
  mycursor = mydb.cursor()

  sql = "INSERT INTO personnage_discipline (personnage_id, discipline_id) VALUES (%s, %s)"
  val_discipline2_id = ui.comboBoxArmePersonnage.itemData(ui.comboBoxDisciplinePersonnage_2.currentIndex())
  #val_personnage_id = recupererIdPersonnage()[0][0]

  mycursor.execute(sql, (val_personnage_id, val_discipline2_id))

  mydb.commit()

# Fonction qui insert les disciplines du personnage dans la BD
def insertionDiscipline3(val_personnage_id):
  mycursor = mydb.cursor()

  sql = "INSERT INTO personnage_discipline (personnage_id, discipline_id) VALUES (%s, %s)"
  val_discipline3_id = ui.comboBoxArmePersonnage.itemData(ui.comboBoxDisciplinePersonnage_3.currentIndex())
  #val_personnage_id = recupererIdPersonnage()[0][0]

  mycursor.execute(sql, (val_personnage_id, val_discipline3_id))

  mydb.commit()

# Fonction qui insert les disciplines du personnage dans la BD
def insertionDiscipline4(val_personnage_id):
  mycursor = mydb.cursor()

  sql = "INSERT INTO personnage_discipline (personnage_id, discipline_id) VALUES (%s, %s)"
  val_discipline4_id = ui.comboBoxArmePersonnage.itemData(ui.comboBoxDisciplinePersonnage_4.currentIndex())
  #val_personnage_id = recupererIdPersonnage()[0][0]

  mycursor.execute(sql, (val_personnage_id, val_discipline4_id))

  mydb.commit()

# Fonction qui insert les disciplines du personnage dans la BD
def insertionDiscipline5(val_personnage_id):
  mycursor = mydb.cursor()

  sql = "INSERT INTO personnage_discipline (personnage_id, discipline_id) VALUES (%s, %s)"
  val_discipline5_id = ui.comboBoxArmePersonnage.itemData(ui.comboBoxDisciplinePersonnage_5.currentIndex())
  #val_personnage_id = recupererIdPersonnage()[0][0]

  mycursor.execute(sql, (val_personnage_id, val_discipline5_id))

  mydb.commit()

def afficheChapitre():
  chapitre.show()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

selectionLivre()
selectionArmePersonnage()
selectionDisciplinePersonnage()
recupererIdPersonnage()


#Création de la boite de dialogue Chapitre
chapitre = QtWidgets.QDialog()
uichapitre = ChapitreDialog()
uichapitre.setupUi(chapitre)

MainWindow.show()

def debuterPartie():

  afficheChapitre()

  personnage_id = insertionPersonnage()

  insertionArme(personnage_id)

  insertionDiscipline1(personnage_id)

  insertionDiscipline2(personnage_id)

  insertionDiscipline3(personnage_id)

  insertionDiscipline4(personnage_id)

  insertionDiscipline5(personnage_id)

  selectionPrologue()


ui.pushButtonDebutPartie.clicked.connect(debuterPartie)


sys.exit(app.exec_())