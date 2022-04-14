# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1222, 740)
        MainWindow.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnOpenLib = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpenLib.setGeometry(QtCore.QRect(10, 50, 70, 70))
        self.btnOpenLib.setStyleSheet("QPushButton{background-color:rgba(95, 171, 48);\n"
"color: rgb(255,255,255);\n"
"border-radius: 15px;}")
        self.btnOpenLib.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons-1.8.1/icons/folder2-open.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnOpenLib.setIcon(icon)
        self.btnOpenLib.setIconSize(QtCore.QSize(50, 64))
        self.btnOpenLib.setObjectName("btnOpenLib")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(90, 50, 1001, 621))
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
        self.btnCreateSample = QtWidgets.QPushButton(self.centralwidget)
        self.btnCreateSample.setGeometry(QtCore.QRect(10, 230, 70, 70))
        self.btnCreateSample.setStyleSheet("QPushButton{background-color:rgba(95, 171, 48);\n"
"color: rgb(255,255,255);\n"
"border-radius: 15px;}")
        self.btnCreateSample.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons-1.8.1/icons/plus-square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCreateSample.setIcon(icon1)
        self.btnCreateSample.setIconSize(QtCore.QSize(64, 64))
        self.btnCreateSample.setObjectName("btnCreateSample")
        self.labelHead = QtWidgets.QLabel(self.centralwidget)
        self.labelHead.setGeometry(QtCore.QRect(90, 0, 671, 51))
        self.labelHead.setStyleSheet("color: rgb(95, 171, 48);\n"
"font: 32pt \"Cambria\";")
        self.labelHead.setObjectName("labelHead")
        self.btnSaveLib = QtWidgets.QPushButton(self.centralwidget)
        self.btnSaveLib.setGeometry(QtCore.QRect(10, 140, 70, 70))
        self.btnSaveLib.setStyleSheet("QPushButton{background-color:rgba(95, 171, 48);\n"
"color: rgb(255,255,255);\n"
"border-radius: 15px;}")
        self.btnSaveLib.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons-1.8.1/icons/save-regular.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSaveLib.setIcon(icon2)
        self.btnSaveLib.setIconSize(QtCore.QSize(30, 30))
        self.btnSaveLib.setObjectName("btnSaveLib")
        self.btnBack = QtWidgets.QPushButton(self.centralwidget)
        self.btnBack.setGeometry(QtCore.QRect(1110, 320, 70, 70))
        self.btnBack.setStyleSheet("QPushButton{background-color:rgba(250, 217, 30);\n"
"color: rgb(255,255,255);\n"
"border-radius: 15px;}")
        self.btnBack.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons-1.8.1/icons/arrow-left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBack.setIcon(icon3)
        self.btnBack.setIconSize(QtCore.QSize(50, 64))
        self.btnBack.setObjectName("btnBack")
        self.btnAddMeasurement = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddMeasurement.setGeometry(QtCore.QRect(1110, 50, 70, 70))
        self.btnAddMeasurement.setStyleSheet("QPushButton{background-color:rgba(95, 171, 48);\n"
"color: rgb(255,255,255);\n"
"border-radius: 15px;}")
        self.btnAddMeasurement.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons-1.8.1/icons/rulers.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAddMeasurement.setIcon(icon4)
        self.btnAddMeasurement.setIconSize(QtCore.QSize(50, 50))
        self.btnAddMeasurement.setObjectName("btnAddMeasurement")
        self.btnRemoveMeasurement = QtWidgets.QPushButton(self.centralwidget)
        self.btnRemoveMeasurement.setGeometry(QtCore.QRect(1110, 140, 70, 70))
        self.btnRemoveMeasurement.setStyleSheet("QPushButton{\n"
"    background-color: rgb(199, 30, 30);\n"
"color: rgb(255,255,255);\n"
"border-radius: 15px;}")
        self.btnRemoveMeasurement.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons-1.8.1/icons/dash-square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRemoveMeasurement.setIcon(icon5)
        self.btnRemoveMeasurement.setIconSize(QtCore.QSize(50, 50))
        self.btnRemoveMeasurement.setObjectName("btnRemoveMeasurement")
        self.btnShowGraphs = QtWidgets.QPushButton(self.centralwidget)
        self.btnShowGraphs.setGeometry(QtCore.QRect(1110, 230, 70, 70))
        self.btnShowGraphs.setStyleSheet("QPushButton{background-color:rgba(95, 171, 48);\n"
"color: rgb(255,255,255);\n"
"border-radius: 15px;}")
        self.btnShowGraphs.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons-1.8.1/icons/graph-down.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnShowGraphs.setIcon(icon6)
        self.btnShowGraphs.setIconSize(QtCore.QSize(50, 50))
        self.btnShowGraphs.setObjectName("btnShowGraphs")
        self.btnRemoveSample = QtWidgets.QPushButton(self.centralwidget)
        self.btnRemoveSample.setGeometry(QtCore.QRect(10, 320, 70, 70))
        self.btnRemoveSample.setStyleSheet("QPushButton{\n"
"    background-color: rgb(199, 30, 30);\n"
"color: rgb(255,255,255);\n"
"border-radius: 15px;}")
        self.btnRemoveSample.setText("")
        self.btnRemoveSample.setIcon(icon5)
        self.btnRemoveSample.setIconSize(QtCore.QSize(50, 50))
        self.btnRemoveSample.setObjectName("btnRemoveSample")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1222, 24))
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
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "TEST"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.labelHead.setText(_translate("MainWindow", "Samples"))
