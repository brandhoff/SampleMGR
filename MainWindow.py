# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2529, 1625)
        MainWindow.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnOpenLib = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpenLib.setGeometry(QtCore.QRect(70, 1340, 311, 101))
        self.btnOpenLib.setStyleSheet("QPushButton{background-color:rgba(95, 171, 48);\n"
"color: rgb(255,255,255);\n"
"border-radius: 15px;}")
        self.btnOpenLib.setObjectName("btnOpenLib")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(60, 160, 1751, 1111))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(95, 171, 48))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget.addItem(item)
        self.btnOpenSample = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpenSample.setGeometry(QtCore.QRect(1830, 170, 311, 101))
        self.btnOpenSample.setStyleSheet("QPushButton{background-color:rgba(95, 171, 48);\n"
"color: rgb(255,255,255);\n"
"border-radius: 15px;}")
        self.btnOpenSample.setObjectName("btnOpenSample")
        self.btnShowAll = QtWidgets.QPushButton(self.centralwidget)
        self.btnShowAll.setGeometry(QtCore.QRect(1830, 290, 311, 101))
        self.btnShowAll.setStyleSheet("QPushButton{background-color:rgba(95, 171, 48);\n"
"color: rgb(255,255,255);\n"
"border-radius: 15px;}")
        self.btnShowAll.setObjectName("btnShowAll")
        self.btnOpenFolder = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpenFolder.setGeometry(QtCore.QRect(1830, 410, 311, 101))
        self.btnOpenFolder.setStyleSheet("QPushButton{background-color:rgba(95, 171, 48);\n"
"color: rgb(255,255,255);\n"
"border-radius: 15px;}")
        self.btnOpenFolder.setObjectName("btnOpenFolder")
        self.btnCreateSample = QtWidgets.QPushButton(self.centralwidget)
        self.btnCreateSample.setGeometry(QtCore.QRect(500, 1340, 311, 101))
        self.btnCreateSample.setStyleSheet("QPushButton{background-color:rgba(3, 99, 3);\n"
"color: rgb(255,255,255);\n"
"border-radius: 15px;}\n"
"    ")
        self.btnCreateSample.setObjectName("btnCreateSample")
        self.btnCreateLib = QtWidgets.QPushButton(self.centralwidget)
        self.btnCreateLib.setGeometry(QtCore.QRect(70, 1460, 311, 101))
        self.btnCreateLib.setStyleSheet("QPushButton{background-color:rgba(3, 99, 3);\n"
"color: rgb(255,255,255);\n"
"border-radius: 15px;}\n"
"    ")
        self.btnCreateLib.setObjectName("btnCreateLib")
        self.labelHead = QtWidgets.QLabel(self.centralwidget)
        self.labelHead.setGeometry(QtCore.QRect(60, 40, 671, 91))
        self.labelHead.setStyleSheet("color: rgb(95, 171, 48);\n"
"font: 32pt \"Cambria\";")
        self.labelHead.setObjectName("labelHead")
        self.btnAddMeasurement = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddMeasurement.setGeometry(QtCore.QRect(1830, 600, 311, 101))
        self.btnAddMeasurement.setStyleSheet("QPushButton{background-color:rgba(3, 99, 3);\n"
"color: rgb(255,255,255);\n"
"border-radius: 15px;}\n"
"    ")
        self.btnAddMeasurement.setObjectName("btnAddMeasurement")
        self.btnSaveLib = QtWidgets.QPushButton(self.centralwidget)
        self.btnSaveLib.setGeometry(QtCore.QRect(2200, 1450, 311, 101))
        self.btnSaveLib.setStyleSheet("QPushButton{background-color:rgba(95, 171, 48);\n"
"color: rgb(255,255,255);\n"
"border-radius: 15px;}")
        self.btnSaveLib.setObjectName("btnSaveLib")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 2529, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnOpenLib.setText(_translate("MainWindow", "Open Libary"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "TEST"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.btnOpenSample.setText(_translate("MainWindow", "Open Sample"))
        self.btnShowAll.setText(_translate("MainWindow", "Show All Graphs"))
        self.btnOpenFolder.setText(_translate("MainWindow", "Open Folder"))
        self.btnCreateSample.setText(_translate("MainWindow", "Create Sample"))
        self.btnCreateLib.setText(_translate("MainWindow", "Create Libary"))
        self.labelHead.setText(_translate("MainWindow", "Samples"))
        self.btnAddMeasurement.setText(_translate("MainWindow", "Add Measurement"))
        self.btnSaveLib.setText(_translate("MainWindow", "Save to disk"))

