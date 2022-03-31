# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addMeasurement.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1438, 869)
        Dialog.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 521, 81))
        self.label.setStyleSheet("color: rgb(95, 171, 48);\n"
"font: 32pt \"Cambria\";")
        self.label.setObjectName("label")
        self.textEditMsrType = QtWidgets.QPlainTextEdit(Dialog)
        self.textEditMsrType.setGeometry(QtCore.QRect(350, 90, 651, 91))
        self.textEditMsrType.setStyleSheet("color: rgb(95, 171, 48);\n"
"font: 32pt \"Cambria\";")
        self.textEditMsrType.setPlainText("")
        self.textEditMsrType.setObjectName("textEditMsrType")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 331, 81))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 24pt \"Cambria\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 190, 331, 81))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 24pt \"Cambria\";")
        self.label_3.setObjectName("label_3")
        self.textEditMsrAuthor = QtWidgets.QPlainTextEdit(Dialog)
        self.textEditMsrAuthor.setGeometry(QtCore.QRect(350, 190, 651, 91))
        self.textEditMsrAuthor.setStyleSheet("color: rgb(95, 171, 48);\n"
"font: 32pt \"Cambria\";")
        self.textEditMsrAuthor.setPlainText("")
        self.textEditMsrAuthor.setObjectName("textEditMsrAuthor")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 280, 331, 81))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 24pt \"Cambria\";")
        self.label_4.setObjectName("label_4")
        self.dateEdit = QtWidgets.QDateEdit(Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(350, 290, 651, 81))
        self.dateEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 24pt \"Cambria\";")
        self.dateEdit.setObjectName("dateEdit")
        self.btnFinish = QtWidgets.QPushButton(Dialog)
        self.btnFinish.setGeometry(QtCore.QRect(10, 740, 111, 111))
        self.btnFinish.setStyleSheet("QPushButton{background-color:rgba(95, 171, 48);\n"
"color: rgb(255,255,255);\n"
"border-radius: 15px;}")
        self.btnFinish.setObjectName("btnFinish")
        self.btnAbort = QtWidgets.QPushButton(Dialog)
        self.btnAbort.setGeometry(QtCore.QRect(1310, 740, 111, 111))
        self.btnAbort.setStyleSheet("QPushButton{background-color:rgba(3, 99, 3);\n"
"color: rgb(255,255,255);\n"
"border-radius: 15px;}\n"
"    ")
        self.btnAbort.setObjectName("btnAbort")
        self.btnaddGraphs = QtWidgets.QPushButton(Dialog)
        self.btnaddGraphs.setGeometry(QtCore.QRect(10, 380, 261, 81))
        self.btnaddGraphs.setStyleSheet("QPushButton{background-color:rgba(95, 171, 48);\n"
"color: rgb(255,255,255);\n"
"border-radius: 15px;}")
        self.btnaddGraphs.setObjectName("btnaddGraphs")
        self.btnAddRaw = QtWidgets.QPushButton(Dialog)
        self.btnAddRaw.setGeometry(QtCore.QRect(10, 470, 261, 81))
        self.btnAddRaw.setStyleSheet("QPushButton{background-color:rgba(95, 171, 48);\n"
"color: rgb(255,255,255);\n"
"border-radius: 15px;}")
        self.btnAddRaw.setObjectName("btnAddRaw")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Add Measurement"))
        self.label_2.setText(_translate("Dialog", "Type:"))
        self.label_3.setText(_translate("Dialog", "Author:"))
        self.label_4.setText(_translate("Dialog", "Date:"))
        self.btnFinish.setText(_translate("Dialog", "Finish"))
        self.btnAbort.setText(_translate("Dialog", "Abort"))
        self.btnaddGraphs.setText(_translate("Dialog", "Add Graphs"))
        self.btnAddRaw.setText(_translate("Dialog", "Add RAW"))

