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

    def key(self, prop: str):
        key = prop
        return self

    def to(self, prop: any):
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
    
    def borderColor(self, prop: str):
        borderColor = prop
        return self
    
    def borderDashStyle(self, prop: str):
        borderDashStyle = prop
        return self
    
    def borderWidth(self, prop: Any):
        borderWidth = prop
        return self
    
    def color(self, prop: str):
        color = prop
        return self
    
    def colorByPoint(self, prop: any):
        colorByPoint = prop
        return self
    
    def dataLabels(self, prop: AADataLabels):
        dataLabels = prop
        return self
    
    def layoutAlgorithm(self, prop: str):
        layoutAlgorithm = prop
        return self
    
    def layoutStartingDirection(self, prop: str):
        layoutStartingDirection = prop
        return self
    
    def level(self, prop: any):
        level = prop
        return self
    
    def colorVariation(self, prop: AAColorVariation):
        colorVariation = prop
        return self
    
    def height(self, prop: float):
        height = prop
        return self
    


