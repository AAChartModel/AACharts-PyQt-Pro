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
    
    def minSizeSet(self, prop: str):
        minSize = prop
        return self
    
    def maxSizeSet(self, prop: str):
        maxSize = prop
        return self
    
    def zMinSet(self, prop: any):
        zMin = prop
        return self
    
    def zMaxSet(self, prop: any):
        zMax = prop
        return self
    
    def layoutAlgorithmSet(self, prop: AALayoutAlgorithm):
        layoutAlgorithm = prop
        return self
    
    def dataLabelsSet(self, prop: AADataLabels):
        dataLabels = prop
        return self
    
    def useSimulationSet(self, prop: bool):
        useSimulation = prop
        return self
