# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Chapitre.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1055, 827)
        Dialog.setStyleSheet("")
        self.pushButtonSauvegarde = QtWidgets.QPushButton(Dialog)
        self.pushButtonSauvegarde.setGeometry(QtCore.QRect(50, 30, 93, 41))
        self.pushButtonSauvegarde.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonSauvegarde.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButtonSauvegarde.setObjectName("pushButtonSauvegarde")
        self.labelChapitreNo = QtWidgets.QLabel(Dialog)
        self.labelChapitreNo.setGeometry(QtCore.QRect(340, 10, 311, 101))
        font = QtGui.QFont()
        font.setFamily("Viner Hand ITC")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.labelChapitreNo.setFont(font)
        self.labelChapitreNo.setTextFormat(QtCore.Qt.AutoText)
        self.labelChapitreNo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelChapitreNo.setObjectName("labelChapitreNo")
        self.labelNumeroChapitre = QtWidgets.QLabel(Dialog)
        self.labelNumeroChapitre.setGeometry(QtCore.QRect(610, 10, 111, 101))
        font = QtGui.QFont()
        font.setFamily("Viner Hand ITC")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.labelNumeroChapitre.setFont(font)
        self.labelNumeroChapitre.setText("")
        self.labelNumeroChapitre.setTextFormat(QtCore.Qt.AutoText)
        self.labelNumeroChapitre.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNumeroChapitre.setObjectName("labelNumeroChapitre")
        self.labelTexteChapitre = QtWidgets.QLabel(Dialog)
        self.labelTexteChapitre.setGeometry(QtCore.QRect(50, 110, 971, 601))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        font.setItalic(False)
        self.labelTexteChapitre.setFont(font)
        self.labelTexteChapitre.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.labelTexteChapitre.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelTexteChapitre.setScaledContents(True)
        self.labelTexteChapitre.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.labelTexteChapitre.setWordWrap(True)
        self.labelTexteChapitre.setObjectName("labelTexteChapitre")
        self.pushButtonChoixChapitre = QtWidgets.QPushButton(Dialog)
        self.pushButtonChoixChapitre.setGeometry(QtCore.QRect(630, 740, 81, 71))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonChoixChapitre.setFont(font)
        self.pushButtonChoixChapitre.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonChoixChapitre.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButtonChoixChapitre.setObjectName("pushButtonChoixChapitre")
        self.pushButtonPasserPrologue = QtWidgets.QPushButton(Dialog)
        self.pushButtonPasserPrologue.setEnabled(True)
        self.pushButtonPasserPrologue.setGeometry(QtCore.QRect(810, 30, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonPasserPrologue.setFont(font)
        self.pushButtonPasserPrologue.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonPasserPrologue.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButtonPasserPrologue.setObjectName("pushButtonPasserPrologue")
        self.comboBoxChapitreSuivant = QtWidgets.QComboBox(Dialog)
        self.comboBoxChapitreSuivant.setGeometry(QtCore.QRect(410, 740, 211, 71))
        self.comboBoxChapitreSuivant.setObjectName("comboBoxChapitreSuivant")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButtonSauvegarde.setText(_translate("Dialog", "SAUVEGARDE"))
        self.labelChapitreNo.setText(_translate("Dialog", "Chapitre N°"))
        self.labelTexteChapitre.setText(_translate("Dialog", "TextLabel"))
        self.pushButtonChoixChapitre.setText(_translate("Dialog", "GO"))
        self.pushButtonPasserPrologue.setText(_translate("Dialog", "Passer le prologue"))
