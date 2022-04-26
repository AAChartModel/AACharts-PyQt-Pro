# //
# //  AAPackedbubble.swift
# //  AAInfographics-ProDemo
# //
# //  Created by AnAn on 2020/11/10.
# //
#
# import UIKit
from aacharts.aaoptionsmodel.AADataLabels import AADataLabels
from aacharts.aaoptionsmodelpro.AALayoutAlgorithm import AALayoutAlgorithm


class AAPackedbubble:
    minSize: str
    maxSize: str
    zMin: any
    zMax: any
    layoutAlgorithm: AALayoutAlgorithm
    dataLabels: AADataLabels
    useSimulation: bool
    
    def minSize(self, prop: str):
        minSize = prop
        return self
    
    def maxSize(self, prop: str):
        maxSize = prop
        return self
    
    def zMin(self, prop: any):
        zMin = prop
        return self
    
    def zMax(self, prop: any):
        zMax = prop
        return self
    
    def layoutAlgorithm(self, prop: AALayoutAlgorithm):
        layoutAlgorithm = prop
        return self
    
    def dataLabels(self, prop: AADataLabels):
        dataLabels = prop
        return self
    
    def useSimulation(self, prop: bool):
        useSimulation = prop
        return self
