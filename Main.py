import Chapitre
import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="Matthieu",
  password="123",
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

  uichapitre.pushButtonChoixChapitre.setEnabled(False)

# Fonction qui sélectionne le premier chapitre
def selectionChapitre():
  # Création du curseur
  mycursor = mydb.cursor()

  requeteChapitre = "SELECT no_chapitre, texte FROM chapitre WHERE livre_id = 1 AND no_chapitre = 1"

  mycursor.execute(requeteChapitre)

  # Le curseur récupère toutes les données du résultat de la requête
  myresult = mycursor.fetchall()

  for (chapitre) in myresult:
    uichapitre.labelNumeroChapitre.setText(str(chapitre[0]))
    uichapitre.labelTexteChapitre.setText(chapitre[1])

  uichapitre.pushButtonChoixChapitre.setEnabled(True)
  uichapitre.pushButtonPasserPrologue.setEnabled(False)
  uichapitre.labelChapitreNo.setText("Chapitre N°")
  affichageChapitreSuivant()

# Fonction qui sélectionne le chapitre suivant
def affichageChapitreSuivant():
  chapitre_origine = uichapitre.labelNumeroChapitre.text()
  # Création du curseur
  mycursor = mydb.cursor()

  requeteChapitreSuivant = "SELECT no_chapitre_destination FROM lien_chapitre WHERE no_chapitre_origine = %s"
  # Ensuite on crée un tuple avec les valeurs des paramêtres
  parametres = (chapitre_origine,)

  mycursor.execute(requeteChapitreSuivant, parametres)

  # Le curseur récupère toutes les données du résultat de la requête
  myresult = mycursor.fetchall()

  for (no_chapitre_destination) in myresult:
    uichapitre.comboBoxChapitreSuivant.addItem(str(no_chapitre_destination[0]))


def selectionChapitreSuivant():

  # Création du curseur
  mycursor = mydb.cursor()

  requeteChapitre = "SELECT no_chapitre, texte FROM chapitre WHERE livre_id = 1 AND no_chapitre = %s"

  val_chapitre_suivant = (uichapitre.comboBoxChapitreSuivant.currentText(),)

  mycursor.execute(requeteChapitre, val_chapitre_suivant)

  # Le curseur récupère toutes les données du résultat de la requête
  myresult = mycursor.fetchall()

  for (chapitre) in myresult:
    uichapitre.labelNumeroChapitre.setText(str(chapitre[0]))
    uichapitre.labelTexteChapitre.setText(chapitre[1])

  uichapitre.comboBoxChapitreSuivant.clear()
  affichageChapitreSuivant()
  
# Fonction qui insert le personnage créé par le joueur dans la BD
def insertionPersonnage():
  mycursor = mydb.cursor()

  sql = "INSERT INTO personnage (nom, livre_id) VALUES (%s, %s)"
  val_nom = ui.textEditNomPersonnage.toPlainText()
  val_livre_id = 1

  mycursor.execute(sql, (val_nom, val_livre_id))

  mydb.commit()

  return mycursor.lastrowid

# Fonction qui permet de récupérer l'ID du dernier personnage créé
def recupererIdPersonnage():
  mycursor = mydb.cursor()
  sql = "SELECT id FROM personnage ORDER BY id DESC LIMIT 1"

  mycursor.execute(sql,)

  myresult = mycursor.fetchone()

  return myresult[0]

    
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


def effectuerSauvegarde():

  personnage_id = recupererIdPersonnage()

  mycursor = mydb.cursor()

  sql = "INSERT INTO sauvegarde (titre, livre_id, chapitre_id, personnage_id, date_sauvegarde) VALUES ((SELECT nom FROM personnage WHERE id = %s), 1, %s, %s, NOW())"
  
  chapitre_en_cours = uichapitre.labelNumeroChapitre.text()
  parametre = (personnage_id, chapitre_en_cours, personnage_id,)

  mycursor.execute(sql, parametre)

  mydb.commit()


def afficherSauvegarde():
  # Création du curseur
  mycursor = mydb.cursor()

  requeteChapitreSuivant = "SELECT id, titre, date_sauvegarde FROM sauvegarde"
  # Ensuite on crée un tuple avec les valeurs des paramêtres

  mycursor.execute(requeteChapitreSuivant,)

  # Le curseur récupère toutes les données du résultat de la requête
  myresult = mycursor.fetchall()

  for (id, titre, date) in myresult:
    ui.comboBoxAfficherSauvegarde.addItem('{}_{}'.format(titre, date), id)
    

def supprimerSauvegarde():

  mycursor = mydb.cursor()

  sql = "DELETE FROM sauvegarde WHERE id = %s"
  # Le currentData permet de récupérer la valeur de l'id de la valeur du comboBox sélectionné, indiqué dans ui.comboBoxAfficherSauvegarde.addItem('{}_{}'.format(titre, date), id) <--
  val_sauvegarde_id = ui.comboBoxAfficherSauvegarde.currentData()

  mycursor.execute(sql, (val_sauvegarde_id,))

  mydb.commit()

  ui.comboBoxAfficherSauvegarde.clear()

  afficherSauvegarde()


def afficheChapitre():
  chapitre.show()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

selectionLivre()
afficherSauvegarde()
selectionArmePersonnage()
selectionDisciplinePersonnage()


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

uichapitre.pushButtonPasserPrologue.clicked.connect(selectionChapitre)

uichapitre.pushButtonChoixChapitre.clicked.connect(selectionChapitreSuivant)

uichapitre.pushButtonSauvegarde.clicked.connect(effectuerSauvegarde)

ui.pushButtonSupprimer.clicked.connect(supprimerSauvegarde)

sys.exit(app.exec_())