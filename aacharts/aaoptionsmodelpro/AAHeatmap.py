from ast import Num

from aacharts.aaoptionsmodel.AATooltip import AATooltip


class AAHeatmap:
    #   public Number borderWidth;
    # public String nullColor;
    # public Number colsize;
    # public AATooltip tooltip;
    # public Object[] data;
    # public Number turboThreshold;

    borderWidth: Num
    nullColor: str
    colsize: Num
    tooltip: AATooltip
    data: list
    turboThreshold: Num

    def borderWidthSet(self, prop: Num):
        self.borderWidth = prop
        return self 

    def nullColorSet(self, prop: str):
        self.nullColor = prop
        return self

    def colsizeSet(self, prop: Num):
        self.colsize = prop
        return self

    def tooltipSet(self, prop: AATooltip):
        self.tooltip = prop
        return self

    def dataSet(self, prop: list):
        self.data = prop
        return self

    def turboThresholdSet(self, prop: Num):
        self.turboThreshold = prop
        return self

        


