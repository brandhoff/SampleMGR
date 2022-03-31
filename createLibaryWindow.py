# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createLibary.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1092, 363)
        Dialog.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 361, 81))
        self.label.setStyleSheet("color: rgb(95, 171, 48);\n"
"font: 32pt \"Cambria\";")
        self.label.setObjectName("label")
        self.btnFinish = QtWidgets.QPushButton(Dialog)
        self.btnFinish.setGeometry(QtCore.QRect(10, 230, 111, 111))
        self.btnFinish.setStyleSheet("QPushButton{background-color:rgba(95, 171, 48);\n"
"color: rgb(255,255,255);\n"
"border-radius: 15px;}")
        self.btnFinish.setObjectName("btnFinish")
        self.textEditLibaryName = QtWidgets.QPlainTextEdit(Dialog)
        self.textEditLibaryName.setGeometry(QtCore.QRect(390, 100, 651, 91))
        self.textEditLibaryName.setStyleSheet("color: rgb(95, 171, 48);\n"
"font: 32pt \"Cambria\";")
        self.textEditLibaryName.setPlainText("")
        self.textEditLibaryName.setObjectName("textEditLibaryName")
        self.btnAbort = QtWidgets.QPushButton(Dialog)
        self.btnAbort.setGeometry(QtCore.QRect(930, 220, 111, 111))
        self.btnAbort.setStyleSheet("QPushButton{background-color:rgba(3, 99, 3);\n"
"color: rgb(255,255,255);\n"
"border-radius: 15px;}\n"
"    ")
        self.btnAbort.setObjectName("btnAbort")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 361, 81))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 24pt \"Cambria\";")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Create Libary"))
        self.btnFinish.setText(_translate("Dialog", "Finish"))
        self.btnAbort.setText(_translate("Dialog", "Abort"))
        self.label_2.setText(_translate("Dialog", "Sample name:"))

