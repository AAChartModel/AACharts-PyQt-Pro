# //
# //  AAColorAxis.swift
# //  AAInfographics-ProDemo
# //
# //  Created by AnAn on 2020/11/10.
# //
#
# import UIKit

from ast import Num

from aacharts.aaoptionsmodel.AALabels import AALabels


class AAColorAxis:
    min: any
    minColor: str
    maxColor: str
    dataClasses: list
    stops: list
    max: Num
    startOnTick: bool
    endOnTick: bool
    labels: AALabels
    
    
    def minSet(self, prop: any):
        self.min = prop
        return self
    
    def minColorSet(self, prop: str):
        self.minColor = prop
        return self
    
    def maxColorSet(self, prop: str):
        self.maxColor = prop
        return self
    
    def dataClassesSet(self, prop: list):
        self.dataClasses = prop
        return self

    def stopsSet(self, prop: list):
        self.stops = prop
        return self

    def maxSet(self, prop: Num):
        self.max = prop
        return self

    def startOnTickSet(self, prop: bool):
        self.startOnTick = prop
        return self

    def endOnTickSet(self, prop: bool):
        self.endOnTick = prop
        return self

    def labelsSet(self, prop: AALabels):
        self.labels = prop
        return self


class AADataClassesElement:
    _from: any
    to: any
    color: str
    name: str
    
    def fromSet(self, prop: any):
        self._from = prop
        return self
    
    def toSet(self, prop: any):
        self.to = prop
        return self
    
    def colorSet(self, prop: str):
        self.color = prop
        return self
    
    def nameSet(self, prop: str):
        self.name = prop
        return self

