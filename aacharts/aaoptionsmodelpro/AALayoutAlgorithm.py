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
    
    def gravitationalConstantSet(self, prop: any):
        gravitationalConstant = prop
        return self
    
    def splitSeriesSet(self, prop: bool):
        splitSeries = prop
        return self
    
    def seriesInteractionSet(self, prop: bool):
        seriesInteraction = prop
        return self
    
    def dragBetweenSeriesSet(self, prop: bool):
        dragBetweenSeries = prop
        return self
    
    def parentNodeLimitSet(self, prop: bool):
        parentNodeLimit = prop
        return self
