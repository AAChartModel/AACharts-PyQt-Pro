# //
# //  AATreemap.swift
# //  AAInfographics-ProDemo
# //
# //  Created by AnAn on 2020/11/10.
# //
#
# import UIKit

class AATreemap:
    layoutAlgorithm: str
    allowTraversingTree: bool
    
    def layoutAlgorithmSet(self, prop: str):
        layoutAlgorithm = prop
        return self
    
    def allowTraversingTreeSet(self, prop: bool):
        allowTraversingTree = prop
        return self

