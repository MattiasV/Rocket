# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eBoiler.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_eBoiler(object):
    def setupUi(self, eBoiler):
        eBoiler.setObjectName("eBoiler")
        eBoiler.resize(727, 491)
        self.CentralBox = QtWidgets.QWidget(eBoiler)
        self.CentralBox.setGeometry(QtCore.QRect(240, 120, 271, 161))
        self.CentralBox.setObjectName("CentralBox")
        self.label = QtWidgets.QLabel(eBoiler)
        self.label.setGeometry(QtCore.QRect(260, 50, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(eBoiler)
        QtCore.QMetaObject.connectSlotsByName(eBoiler)

    def retranslateUi(self, eBoiler):
        _translate = QtCore.QCoreApplication.translate
        eBoiler.setWindowTitle(_translate("eBoiler", "Form"))
        self.label.setText(_translate("eBoiler", "e-Boiler Setup Lab"))

