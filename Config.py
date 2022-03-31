# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 19:59:14 2022

@author: Jonas
"""

import yaml

class Config:
    
    
    # Define data
    dataLibary = {
       'defaultSteps': 2,
       'hasCVelocity':False,
       'moveHome':True,
       'velocity':2
    }
    
    dataSample = {
        }
    
    
    def __init__(self):
        self.defaultStep = 2
        self.hasCustomVelo = False
        self.CustomVelo = 0
        self.moveHomeAtClose = False
        self.moveIndef = False
    
    def loadFromFile(self, filepath, window):
        with open(filepath, "r") as ymlfile:
            try:
                cfg = yaml.safe_load(ymlfile)
                data=cfg
                self.defaultStep = data['defaultSteps']
                self.hasCustomVelo = data['hasCVelocity']
                self.moveHomeAtClose = data['moveHome']
                self.CustomVelo = data['velocity']
                window.configToWindow()
            except yaml.YAMLError as exc:
                window.showErrorMSG('Import fehler', str(exc))
       
    
    def writeToFile(self, filepath):
        data = dict(
        moveHome = self.moveHomeAtClose,
        velocity = self.CustomVelo,
        hasCVelocity = self.hasCustomVelo,
        defaultSteps = self.defaultStep)
        with open(filepath, 'w') as outfile:
            yaml.dump(data, outfile, default_flow_style=False)