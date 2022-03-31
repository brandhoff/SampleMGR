# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 20:07:16 2022

@author: Jonas
"""
import json
class Libary:
    def __init__(self):
        self.name = ""
        self.Samples = []
    
    def addSample(self, sample):
        self.Samples.append(sample)
        print(self.Samples)
        
        
    def removeSample(self, sample):
        if sample in self.Samples:
            Samples.remove(sample)
        
    def readFromFile(self, file):
        print(file)
        
        
    def writeToFile(self, file):
        
        
        sampleDumpArr = []
        
        for smp in self.Samples:
            sampleDumpArr.append(smp.dump())
        dumpDic = {'name': self.name,
                   'Samples': sampleDumpArr}
        
        print(dumpDic)