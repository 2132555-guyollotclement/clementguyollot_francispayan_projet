# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Menu accueil.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1059, 823)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelTitreLivre = QtWidgets.QLabel(self.centralwidget)
        self.labelTitreLivre.setGeometry(QtCore.QRect(60, 40, 951, 151))
        font = QtGui.QFont()
        font.setFamily("Viner Hand ITC")
        font.setPointSize(50)
        font.setBold(False)
        font.setWeight(50)
        self.labelTitreLivre.setFont(font)
        self.labelTitreLivre.setTextFormat(QtCore.Qt.AutoText)
        self.labelTitreLivre.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitreLivre.setObjectName("labelTitreLivre")
        self.labelSousTitreLivre = QtWidgets.QLabel(self.centralwidget)
        self.labelSousTitreLivre.setGeometry(QtCore.QRect(170, 230, 751, 281))
        font = QtGui.QFont()
        font.setFamily("Viner Hand ITC")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.labelSousTitreLivre.setFont(font)
        self.labelSousTitreLivre.setTextFormat(QtCore.Qt.AutoText)
        self.labelSousTitreLivre.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSousTitreLivre.setWordWrap(True)
        self.labelSousTitreLivre.setObjectName("labelSousTitreLivre")
        self.pushButtonDebutPartie = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDebutPartie.setGeometry(QtCore.QRect(410, 570, 281, 151))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonDebutPartie.setFont(font)
        self.pushButtonDebutPartie.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButtonDebutPartie.setObjectName("pushButtonDebutPartie")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1059, 26))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuSauvegarde = QtWidgets.QMenu(self.menubar)
        self.menuSauvegarde.setObjectName("menuSauvegarde")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuSauvegarde.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelTitreLivre.setText(_translate("MainWindow", "Les Maitres des Ténèbres"))
        self.labelSousTitreLivre.setText(_translate("MainWindow", "Seras-tu capable de d\'atteindre le bout de ton aventure ?"))
        self.pushButtonDebutPartie.setText(_translate("MainWindow", "Commencer l\'aventure"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuSauvegarde.setTitle(_translate("MainWindow", "Sauvegardes"))
