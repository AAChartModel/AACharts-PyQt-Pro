# //
# //  AALayoutAlgorithm.swift
# //  AAInfographics-ProDemo
# //
# //  Created by AnAn on 2020/11/10.
# //
#
# import UIKit

class AALayoutAlgorithm:
    gravitationalConstant: any
    splitSeries: bool
    seriesInteraction: bool
    dragBetweenSeries: bool
    parentNodeLimit: bool
    
    def gravitationalConstant(self, prop: any):
        gravitationalConstant = prop
        return self
    
    def splitSeries(self, prop: bool):
        splitSeries = prop
        return self
    
    def seriesInteraction(self, prop: bool):
        seriesInteraction = prop
        return self
    
    def dragBetweenSeries(self, prop: bool):
        dragBetweenSeries = prop
        return self
    
    def parentNodeLimit(self, prop: bool):
        parentNodeLimit = prop
        return self
