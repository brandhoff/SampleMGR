# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 20:07:40 2022

@author: Jonas
"""

class Measurement:
    def __init__(self, art, author, datum, GraphFiles, RawFiles):
        self.art = art
        self.author = author
        self.datum = datum
        self.GraphFiles = GraphFiles
        self.RawFiles = RawFiles
        
    def addGraphFile(self, gfl):
        self.GraphFiles.append(gfl)
        
    def addRawFile(self, rfl):
        self.RawFiles.append(rfl)
    
    def dump(self):
        dumpDic = {
            'art': self.art,
            'author': self.author,
            'datum': self.datum,
            'GraphFiles': self.GraphFiles,
            'RawFiles': self.RawFiles}
        
        return dumpDic
