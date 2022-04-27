# //
# //  AAColorAxis.swift
# //  AAInfographics-ProDemo
# //
# //  Created by AnAn on 2020/11/10.
# //
#
# import UIKit

class AAColorAxis:
    min: any
    minColor: str
    maxColor: str
    dataClasses: list
    
    def minSet(self, prop: any):
        min = prop
        return self
    
    def minColorSet(self, prop: str):
        minColor = prop
        return self
    
    def maxColorSet(self, prop: str):
        maxColor = prop
        return self
    
    def dataClassesSet(self, prop: list):
        dataClasses = prop
        return self


class AADataClassesElement:
    _from: any
    to: any
    color: str
    name: str
    
    def _fromSet(self, prop: any):
        _from = prop
        return self
    
    def toSet(self, prop: any):
        to = prop
        return self
    
    def colorSet(self, prop: str):
        color = prop
        return self
    
    def nameSet(self, prop: str):
        name = prop
        return self

