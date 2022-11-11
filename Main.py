import Chapitre

from PyQt5 import QtCore, QtGui, QtWidgets
from Menuaccueil import Ui_MainWindow
from Chapitre import Ui_Dialog as ChapitreDialog

import sys

def afficheChapitre():
    chapitre.show()


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

#Création de la boite de dialogue Chapitre
chapitre = QtWidgets.QDialog()
uichapitre = ChapitreDialog()
uichapitre.setupUi(chapitre)

MainWindow.show()

ui.pushButtonDebutPartie.clicked.connect(afficheChapitre)


sys.exit(app.exec_())
