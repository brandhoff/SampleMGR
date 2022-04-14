# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 20:07:27 2022

@author: Jonas
"""
import json
class Sample:
    def __init__(self, name, SystemListe = None):
        self.name = name
        self.SystemListe = SystemListe
        self.measurements = []
        
    def addMeasurement(self, msr):
        self.measurements.append(msr)


    def dump(self):
        
        measureDumpArray = []
        
        for msr in self.measurements:
            measureDumpArray.append(msr.dump())
        
        dumpDic = {'name': self.name,
                   'measurements': measureDumpArray}
        
        json_string = json.dumps(dumpDic)
        return json_string