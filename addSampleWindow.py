# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addSample.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1139, 398)
        Dialog.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 10, 361, 81))
        self.label.setStyleSheet("color: rgb(95, 171, 48);\n"
"font: 32pt \"Cambria\";")
        self.label.setObjectName("label")
        self.textEditSampleName = QtWidgets.QPlainTextEdit(Dialog)
        self.textEditSampleName.setGeometry(QtCore.QRect(420, 140, 651, 91))
        self.textEditSampleName.setStyleSheet("color: rgb(95, 171, 48);\n"
"font: 32pt \"Cambria\";")
        self.textEditSampleName.setPlainText("")
        self.textEditSampleName.setObjectName("textEditSampleName")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 140, 361, 81))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 24pt \"Cambria\";")
        self.label_2.setObjectName("label_2")
        self.btnFinish = QtWidgets.QPushButton(Dialog)
        self.btnFinish.setGeometry(QtCore.QRect(40, 270, 111, 111))
        self.btnFinish.setStyleSheet("QPushButton{background-color:rgba(95, 171, 48);\n"
"color: rgb(255,255,255);\n"
"border-radius: 15px;}")
        self.btnFinish.setObjectName("btnFinish")
        self.btnAbort = QtWidgets.QPushButton(Dialog)
        self.btnAbort.setGeometry(QtCore.QRect(960, 260, 111, 111))
        self.btnAbort.setStyleSheet("QPushButton{background-color:rgba(3, 99, 3);\n"
"color: rgb(255,255,255);\n"
"border-radius: 15px;}\n"
"    ")
        self.btnAbort.setObjectName("btnAbort")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Add Sample"))
        self.label_2.setText(_translate("Dialog", "Sample name:"))
        self.btnFinish.setText(_translate("Dialog", "Finish"))
        self.btnAbort.setText(_translate("Dialog", "Abort"))

