# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addSample.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1011, 312)
        Dialog.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 10, 361, 81))
        self.label.setStyleSheet("color: rgb(95, 171, 48);\n"
"font: 32pt \"Cambria\";")
        self.label.setObjectName("label")
        self.textEditSampleName = QtWidgets.QPlainTextEdit(Dialog)
        self.textEditSampleName.setGeometry(QtCore.QRect(210, 100, 791, 81))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.textEditSampleName.setFont(font)
        self.textEditSampleName.setStyleSheet("color: rgb(95, 171, 48);\n"
"font: 24pt \"Cambria\";")
        self.textEditSampleName.setPlainText("")
        self.textEditSampleName.setObjectName("textEditSampleName")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 171, 81))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 24pt \"Cambria\";")
        self.label_2.setObjectName("label_2")
        self.btnFinish = QtWidgets.QPushButton(Dialog)
        self.btnFinish.setGeometry(QtCore.QRect(30, 210, 80, 80))
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
        self.btnAbort.setGeometry(QtCore.QRect(130, 210, 80, 80))
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

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Add Sample"))
        self.label_2.setText(_translate("Dialog", "Sample name:"))
