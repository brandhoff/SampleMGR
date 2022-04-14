# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addMeasurement.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(914, 499)
        Dialog.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 521, 81))
        self.label.setStyleSheet("color: rgb(95, 171, 48);\n"
"font: 32pt \"Cambria\";")
        self.label.setObjectName("label")
        self.textEditMsrType = QtWidgets.QPlainTextEdit(Dialog)
        self.textEditMsrType.setGeometry(QtCore.QRect(236, 100, 651, 80))
        self.textEditMsrType.setStyleSheet("color: rgb(95, 171, 48);\n"
"font: 32pt \"Cambria\";")
        self.textEditMsrType.setPlainText("")
        self.textEditMsrType.setObjectName("textEditMsrType")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(116, 100, 80, 80))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 24pt \"Cambria\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(116, 190, 101, 80))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 24pt \"Cambria\";")
        self.label_3.setObjectName("label_3")
        self.textEditMsrAuthor = QtWidgets.QPlainTextEdit(Dialog)
        self.textEditMsrAuthor.setGeometry(QtCore.QRect(236, 190, 651, 80))
        self.textEditMsrAuthor.setStyleSheet("color: rgb(95, 171, 48);\n"
"font: 32pt \"Cambria\";")
        self.textEditMsrAuthor.setPlainText("")
        self.textEditMsrAuthor.setObjectName("textEditMsrAuthor")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(116, 290, 71, 80))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 24pt \"Cambria\";")
        self.label_4.setObjectName("label_4")
        self.dateEdit = QtWidgets.QDateEdit(Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(236, 290, 651, 80))
        self.dateEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 24pt \"Cambria\";")
        self.dateEdit.setObjectName("dateEdit")
        self.btnFinish = QtWidgets.QPushButton(Dialog)
        self.btnFinish.setGeometry(QtCore.QRect(10, 390, 80, 80))
        self.btnFinish.setStyleSheet("QPushButton{background-color:rgba(95, 171, 48);\n"
"color: rgb(255,255,255);\n"
"border-radius: 15px;}")
        self.btnFinish.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons-1.8.1/icons/check2.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnFinish.setIcon(icon)
        self.btnFinish.setIconSize(QtCore.QSize(64, 64))
        self.btnFinish.setObjectName("btnFinish")
        self.btnAbort = QtWidgets.QPushButton(Dialog)
        self.btnAbort.setGeometry(QtCore.QRect(110, 390, 80, 80))
        self.btnAbort.setStyleSheet("QPushButton{background-color:rgba(250, 30, 30);\n"
"color: rgb(255,255,255);\n"
"border-radius: 15px;}\n"
"    ")
        self.btnAbort.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons-1.8.1/icons/x-square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAbort.setIcon(icon1)
        self.btnAbort.setIconSize(QtCore.QSize(64, 64))
        self.btnAbort.setObjectName("btnAbort")
        self.btnaddGraphs = QtWidgets.QPushButton(Dialog)
        self.btnaddGraphs.setGeometry(QtCore.QRect(10, 190, 80, 80))
        self.btnaddGraphs.setStyleSheet("QPushButton{background-color:rgba(95, 171, 48);\n"
"color: rgb(255,255,255);\n"
"border-radius: 15px;}")
        self.btnaddGraphs.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons-1.8.1/icons/graph-down.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnaddGraphs.setIcon(icon2)
        self.btnaddGraphs.setIconSize(QtCore.QSize(64, 64))
        self.btnaddGraphs.setObjectName("btnaddGraphs")
        self.btnAddRaw = QtWidgets.QPushButton(Dialog)
        self.btnAddRaw.setGeometry(QtCore.QRect(10, 290, 80, 80))
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
        self.btnAddRaw.setText(_translate("Dialog", "Add RAW"))
