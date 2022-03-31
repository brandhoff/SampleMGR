# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1945, 139)
        Form.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.btnFinish = QtWidgets.QPushButton(Form)
        self.btnFinish.setGeometry(QtCore.QRect(1820, 20, 111, 111))
        self.btnFinish.setStyleSheet("QPushButton{background-color:rgba(95, 171, 48);\n"
"color: rgb(255,255,255);\n"
"border-radius: 15px;}")
        self.btnFinish.setObjectName("btnFinish")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 30, 1551, 81))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 32pt \"Cambria\";")
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btnFinish.setText(_translate("Form", "Finish"))
        self.label.setText(_translate("Form", "Sample Name"))

