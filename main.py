# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 16:56:55 2022

@author: Jonas
"""

import os
import sys
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QFileDialog,QListWidgetItem
from MainWindow import Ui_MainWindow

import addMeasurementWindow
import addSampleWindow
import createLibaryWindow
import listWidgetWindow

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QTimer
import numpy as np
import webbrowser
from asyncqt import QEventLoop, asyncSlot
import Config as cfg
import Libary as lib
import Sample as sp
import Measurement as msr
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *






class AddMSRDialog(QDialog, addMeasurementWindow.Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


class AddSampleDialog(QDialog, addSampleWindow.Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

class CreateLibaryDialog(QDialog, createLibaryWindow.Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)



class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.loadedLib = lib.Libary()
        self.connectSignalsSlots()

    """
   Connect all signals to the according slots -> most use async functions
   so asyncSlot() should be used
    """
    def connectSignalsSlots(self):
        
        self.btnOpenLib.clicked.connect(self.loadLib)
        self.btnCreateSample.clicked.connect(self.createSample)
        self.btnSaveLib.clicked.connect(self.saveLib)
        self.btnCreateLib.clicked.connect(self.createLibary)

        
    """
    Is called after initalising, used to set all defaults
    and remind the user that a device should be connected
    """
    def postInit(self):
       self.clearDisplayList()



    """
    LIST ITEMS
    """
    def createListItem(self, dark):
        item = QListWidgetItem(self.listWidget)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        if dark:
            item.setBackground( QColor('#036303') )
        else:
            item.setBackground( QColor('#5fab30') )
            
        return item



"""
LIBARY------------------------------------------------------
"""

    def clearDisplayList(self):
        self.listWidget.clear()

    def saveLib(self):
        self.loadedLib.writeToFile('')
        

    def loadLib(self):
        fileName, filter = QFileDialog.getOpenFileName(self, 'Open file', 
            '', 'Libary (*.json)')
        if fileName:
            self.loadedLib.readFromFile(fileName)

        self.showLibary()



    def createLibary(self):
        dlg = CreateLibaryDialog()
        if dlg.exec_():
            print('yo')
            
            
            
    def showLibary(self):
        self.clearDisplayList()
        flag = False
        for sample in self.loadedLib.Samples:
            item = self.createListItem(flag)
            item.setText(sample.name)
            self.listWidget.addItem(item)
            if flag:
                flag = False
            else:
                flag = True
                
                
"""
LIBARY------------------------------------------------------
"""




"""
SAMPLE------------------------------------------------------
"""
                
    def createSample(self):
        
        dlg = AddSampleDialog()
        if dlg.exec_():
            print('yo')
            #values = dlg.getValues()
        sample = sp.Sample("NERO")
        
        mear = msr.Measurement('UPS', 'JB', '1.6.2020', ['lol','mmm'], ['ok','na ok'])
        #mear2 = msr.Measurement('XPS', 'JB', '1.6.2020', ['lol','mmm'], ['ok','na ok'])

        sample.addMeasurement(mear)    
        #sample.addMeasurement(mear2)

        self.loadedLib.addSample(sample)



        
        
        
        
        
        

if __name__ == "__main__":
    

    """
    QT Application window start
   """
    app = QApplication(sys.argv)
    
    
    loop = QEventLoop(app)
    win = Window()
    win.show()
    win.postInit()
    
    with loop:
        loop.run_forever()
    
    sys.exit(app.exec())