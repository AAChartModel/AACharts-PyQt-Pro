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
        self.key = prop
        return self

    def toSet(self, prop: any):
        self.to = prop
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
        self.borderColor = prop
        return self
    
    def borderDashStyleSet(self, prop: str):
        self.borderDashStyle = prop
        return self
    
    def borderWidthSet(self, prop: any):
        self.borderWidth = prop
        return self
    
    def colorSet(self, prop: str):
        self.color = prop
        return self
    
    def colorByPointSet(self, prop: any):
        self.colorByPoint = prop
        return self
    
    def dataLabelsSet(self, prop: AADataLabels):
        self.dataLabels = prop
        return self
    
    def layoutAlgorithmSet(self, prop: str):
        self.layoutAlgorithm = prop
        return self
    
    def layoutStartingDirectionSet(self, prop: str):
        self.layoutStartingDirection = prop
        return self
    
    def levelSet(self, prop: any):
        self.level = prop
        return self
    
    def colorVariationSet(self, prop: AAColorVariation):
        self.colorVariation = prop
        return self
    
    def heightSet(self, prop: float):
        self.height = prop
        return self
    


