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
    
    def min(self, prop: any):
        min = prop
        return self
    
    def minColor(self, prop: str):
        minColor = prop
        return self
    
    def maxColor(self, prop: str):
        maxColor = prop
        return self
    
    def dataClasses(self, prop: list):
        dataClasses = prop
        return self


class AADataClassesElement:
    _from: any
    to: any
    color: str
    name: str
    
    def _from(self, prop: any):
        _from = prop
        return self
    
    def to(self, prop: any):
        to = prop
        return self
    
    def color(self, prop: str):
        color = prop
        return self
    
    def name(self, prop: str):
        name = prop
        return self

