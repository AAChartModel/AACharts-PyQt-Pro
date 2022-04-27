# //
# //  AALevels.swift
# //  AAInfographics-ProDemo
# //
# //  Created by AnAn on 2020/11/10.
# //
# 
# import UIKit
from aacharts.aaoptionsmodel.AADataLabels import AADataLabels


class AAColorVariation:
    key: str
    to: any

    def keySet(self, prop: str):
        key = prop
        return self

    def toSet(self, prop: any):
        to = prop
        return self


class AALevelsElement:
    borderColor: str
    borderDashStyle: str
    borderWidth: any
    color: str
    colorByPoint: any
    dataLabels: AADataLabels
    layoutAlgorithm: str
    layoutStartingDirection: str
    level: any
    colorVariation: any
    height: float
    
    def borderColorSet(self, prop: str):
        borderColor = prop
        return self
    
    def borderDashStyleSet(self, prop: str):
        borderDashStyle = prop
        return self
    
    def borderWidthSet(self, prop: any):
        borderWidth = prop
        return self
    
    def colorSet(self, prop: str):
        color = prop
        return self
    
    def colorByPointSet(self, prop: any):
        colorByPoint = prop
        return self
    
    def dataLabelsSet(self, prop: AADataLabels):
        dataLabels = prop
        return self
    
    def layoutAlgorithmSet(self, prop: str):
        layoutAlgorithm = prop
        return self
    
    def layoutStartingDirectionSet(self, prop: str):
        layoutStartingDirection = prop
        return self
    
    def levelSet(self, prop: any):
        level = prop
        return self
    
    def colorVariationSet(self, prop: AAColorVariation):
        colorVariation = prop
        return self
    
    def heightSet(self, prop: float):
        height = prop
        return self
    


