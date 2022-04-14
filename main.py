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
import ast





class AddMSRDialog(QDialog, addMeasurementWindow.Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.btnFinish.clicked.connect(self.close)
#textEditMsrType
#textEditMsrAuthor
#dateEdit

class AddSampleDialog(QDialog, addSampleWindow.Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.btnFinish.clicked.connect(self.close)
#textEditSampleName
class CreateLibaryDialog(QDialog, createLibaryWindow.Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)









#MAIN WINDWO-------------------------------------------


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.loadedLib = lib.Libary()
        self.showsLib = True
        self.activeSample = None
        self.activeMeasurement = None
        self.connectSignalsSlots()
        self.savePath = None

    """
   Connect all signals to the according slots -> most use async functions
   so asyncSlot() should be used
    """
    def connectSignalsSlots(self):
        
        shortcut = QShortcut(QKeySequence("Ctrl+S"), self)
        shortcut.activated.connect(self.saveLib)
        
        
        self.btnOpenLib.clicked.connect(self.loadLib)
        self.btnCreateSample.clicked.connect(self.createSample)
        self.btnSaveLib.clicked.connect(self.saveLib)
        #self.btnCreateLib.clicked.connect(self.createLibary)
        self.btnAddMeasurement.clicked.connect(self.addMeasurement)
        self.listWidget.activated.connect(self.openSample)
        self.btnBack.clicked.connect(self.goBack)
        self.btnShowGraphs.clicked.connect(self.addGraph)
        
    """
    Is called after initalising, used to set all defaults
    and remind the user that a device should be connected
    """
    def postInit(self):
       self.clearDisplayList()


    def goBack(self):
        if self.showsLib:
            return
        if self.activeMeasurement:
            if self.activeSample:
                self.activeMeasurement = None
                self.showSampleInList(self.activeSample)
                return #if no active sample go back to lib
            self.showsLib = True
            self.activeMeasurement = None
            self.showLibary()
            return
        self.showsLib = True
        self.activeMeasurement = None
        self.showLibary()
        return
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
        if self.savePath == None:   
            fileName, filter = QFileDialog.getSaveFileName(self, 'Save file', 
                                                           '', 'Libary (*.json)')
            self.loadedLib.writeToFile(fileName)
        else:
            self.loadedLib.writeToFile(self.savePath)
        

    def loadLib(self):
        fileName, filter = QFileDialog.getOpenFileName(self, 'Open file', 
            '', 'Libary (*.json)')
        if fileName:
            self.listWidget.clear()
            self.savePath = fileName
            self.loadedLib = lib.Libary()
            data = self.loadedLib.readFromFile(fileName)
            if data:
                LibName = data['name']
                Samples = data['Samples']
                #loadedSamples = []
                for smp in Samples:
                    smp_dic = ast.literal_eval(smp)
                    SmpName = smp_dic['name']
                    sample = sp.Sample(SmpName)
                    for msr_str in smp_dic['measurements']:
                        msr_dic = ast.literal_eval(msr_str)
                        Type = msr_dic['art']
                        Author = msr_dic['author']
                        Date = msr_dic['datum']
                        #(self, art, author, datum, GraphFiles, RawFiles)
                        measure = msr.Measurement(Type,Author,Date, [''],[''])
                        sample.addMeasurement(measure)
                    #loadedSamples.append(sample)
                    self.loadedLib.addSample(sample)

        self.showLibary()




                
                
    """
LIBARY------------------------------------------------------
    """


            
            
            
    def showLibary(self):
        self.showsLib = True
        self.activeSample = None
        self.activeMeasurement = None
        self.clearDisplayList()
        self.labelHead.setText("Samples")

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
SAMPLE------------------------------------------------------
    """
    

    def showSampleInList(self, smp):
        if self.showsLib:
            return
        if self.activeMeasurement:
            return
        if smp == None:
            return
        self.clearDisplayList()
        
        self.labelHead.setText(smp.name)

        flag = False
        for msr in smp.measurements:
            item = self.createListItem(flag)
            art = msr.art
            author = msr.author
            datum = msr.datum
            DisplayString = ""+art+" "+" "+datum+" "+author
            item.setText(DisplayString)
            self.listWidget.addItem(item)
            if flag:
                flag = False
            else:
                flag = True
            
    def findSampleFromName(self, name):
        lib = self.loadedLib
        for sample in lib.Samples:
            if sample.name == name:
                return sample
        return None
        
    def createSample(self):
        
        dlg = AddSampleDialog()
        dlg.exec_()
        SmName = dlg.textEditSampleName.toPlainText()
        sample = sp.Sample(SmName)
        self.loadedLib.addSample(sample)
        self.showLibary()
        
        
    def openSample(self):
        if self.activeMeasurement:
            path = self.listWidget.selectedItems()[0].text()
            if path:
                os.system('open '+path)
                return
        if self.showsLib:
               sampleName = self.listWidget.selectedItems()[0].text()
               smp = self.findSampleFromName(sampleName)
               if smp == None:
                   return
               self.showsLib = False
               self.activeSample = smp
               self.showSampleInList(self.activeSample)
               return
        if self.activeSample:
            if self.showsLib:
                return
            measureString = self.listWidget.selectedItems()[0].text()
            measure = self.findMeasureInList(measureString)
            if measure:
                self.activeMeasurement = measure
                self.showMeasurementsinList(measure)
                return
            
     
        
    """
MSRMNT------------------------------------------------------
    """
    def addMeasurement(self):
        if self.activeSample == None:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("No Sample Selected")
            msg.setInformativeText("Please select a sample for the measurement to be added to.")
            msg.exec_()
            return
        dlg = AddMSRDialog()
        dlg.exec_()
        #textEditMsrType
        #textEditMsrAuthor
        #dateEdit
        Type = dlg.textEditMsrType.toPlainText()
        Author = dlg.textEditMsrAuthor.toPlainText()
        Date = dlg.dateEdit.text()
        #(self, art, author, datum, GraphFiles, RawFiles)
        measure = msr.Measurement(Type,Author,Date, [''],[''])
        self.activeSample.addMeasurement(measure)
        self.showSampleInList(self.activeSample)
        
        
    def findMeasureInList(self, measureName):
        sample = self.activeSample
        for msru in sample.measurements:
            art = msru.art
            author = msru.author
            datum = msru.datum
            searchString = ""+art+" "+" "+datum+" "+author
            if searchString == measureName:
                return msru
        return None
    
    
    def showMeasurementsinList(self, measure):
        if self.showsLib:
            return
        if measure == None:
            return
        self.clearDisplayList()
        art = measure.art
        author = measure.author
        datum = measure.datum
        DisplayString = ""+art+" "+" "+datum+" "+author

        self.labelHead.setText(DisplayString)
        flag = False
        for graph in measure.GraphFiles:
            item = self.createListItem(flag)
            item.setText(graph)
            self.listWidget.addItem(item)
            if flag:
                flag = False
            else:
                flag = True
    def addGraph(self):
        if self.activeMeasurement:
            fileName, filter = QFileDialog.getOpenFileName(self, 'Add Grpah', 
                '', 'Graph (*.png);; (*.pdf)')
            if fileName:
                if self.activeMeasurement:
                    self.activeMeasurement.addGraphFile(fileName)
        
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