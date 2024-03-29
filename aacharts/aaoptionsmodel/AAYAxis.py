

from typing import List
from aacharts.aaenum.AAEnum import AAChartLineDashStyleType
from aacharts.aaoptionsmodel.AACrosshair import AACrosshair
from aacharts.aaoptionsmodel.AALabels import AALabels
from aacharts.aaoptionsmodel.AATitle import AATitle
from aacharts.aaenum.AAEnum import AAChartAxisType
from aacharts.aaoptionsmodel.AAXAxis import AADateTimeLabelFormats
from ast import Num


class AAYAxis:
    alternateGridColor: str
    title: AATitle
    type: str
    dateTimeLabelFormats = None
    dateTimeLabelFormats: AADateTimeLabelFormats
    plotBands: List
    plotLines: List
    categories: List
    reversed: bool
    gridLineWidth: float # y-axis grid line width
    gridLineColor: str # y-axis grid line color
    gridLineDashStyle: str # Grid line line style, all available line style references: Highcharts line style
    gridLineInterpolation: str # Polar charts only. Whether the grid lines should draw as a polygon with straight lines between categories, or as circles. Can be either circle or polygon. The default is: null.
    labels: AALabels # Used to set the y-axis text related
    lineWidth: float # y-axis width
    lineColor: str # y--axis line color
    offset: float # y-axis horizontal offset
    allowDecimals: bool # Does the y-axis allow decimals to be displayed
    max: float # y-axis maximum
    min: float # y-axis minimum  (set to 0, there will be no negative numbers)
    maxPadding: float  # Padding of the max value relative to the length of the axis. A padding of 0.05 will make a 100px axis 5px longer. This is useful when you don't want the highest data value to appear on the edge of the plot area. When the axis' max option is set or a max extreme is set using axis.setExtremes(), the maxPadding will be ignored. Defaults to 0.01.
    minPadding: float  # Padding of the min value relative to the length of the axis. A padding of 0.05 will make a 100px axis 5px longer. This is useful when you don't want the lowest data value to appear on the edge of the plot area.  Defaults to 0.05
    # private var minPadding: # Padding of the min value relative to the length of the axis. A padding of 0.05 will make a 100px axis 5px longer. This is useful when you don't want the lowest data value to appear on the edge of the plot area. The default is: 0.05.
    minTickInterval: int #The minimum tick interval allowed in axis values. For example on zooming in on an axis with daily data, self can be used to prevent the axis from showing hours. Defaults to the closest distance between two points on the axis.
    minorGridLineColor: str #Color of the minor, secondary grid lines.
    minorGridLineDashStyle: str #The dash or dot style of the minor grid lines.
    minorGridLineWidth: float #Width of the minor, secondary grid lines.
    minorTickColor: str #Color for the minor tick marks.
    minorTickInterval: str #/*Specific tick interval in axis units for the minor ticks. On a linear axis, if "auto", the minor tick interval is calculated as a fifth of the tickInterval. If null or undefined, minor ticks are not shown.

    #On logarithmic axes, the unit is the power of the value. For example, setting the minorTickInterval to 1 puts one tick on each of 0.1, 1, 10, 100 etc. Setting the minorTickInterval to 0.1 produces 9 ticks between 1 and 10, 10 and 100 etc.

    #If user settings dictate minor ticks to become too dense, they don't make sense, and will be ignored to prevent performance problems.*/
    minorTickLength: float #The pixel length of the minor tick marks.
    minorTickPosition: str #The position of the minor tick marks relative to the axis line. Can be one of inside and outside. Defaults to outside.
    minorTickWidth: float #The pixel width of the minor tick mark.

    visible: bool # Whether the y-axis is allowed to display
    opposite: bool # Whether to display the coordinate axis on the opposite surface. By default, the x axis is displayed below the chart, the y axis is on the left, the coordinate axis is displayed on the opposite surface, and the x axis is displayed on the top. The axis is displayed on the right (that is, the coordinate axis is displayed on the opposite side). This configuration is generally used for multi-axis display, and in Highstock, the y-axis is displayed on the opposite side by default. The default is: false.
    startOnTick: bool #Whether to force the axis to start on a tick. Use self option with the minPadding option to control the axis start. The default is: false.
    endOnTick: bool
    tickAmount: int
    tickInterval: float
    crosshair: AACrosshair # Crosshair (focus line) style settings
    stackLabels: map
    tickWidth: float # The width of the axis tick marks. When set to 0, tick marks are not displayed.
    tickLength: float # The length of the axis tick marks. The default is: 10.
    tickPosition: str # Position of the tick line relative to the axis line. Available values ​​are "inside" and "outside", which represent the inside and outside of the axis line, respectively. The default is: "outside".
    tickPositions: List # Custom Y-axis coordinates (eg: [0, 25, 50, 75, 100])
    top: Num
    height: Num
    tooltipValueFormat: str # Parallel coordinates only.https: // api.highcharts.com.cn / highcharts / yAxis.tooltipValueFormat.html

    def topSet(self, prop:Num):
        self.top = prop
        return self
    def heightSet(self, prop:Num):
        self.height = prop
        return self
    def tooltipValueFormatSet(self, prop:str):
        self.tooltipValueFormat = prop
        return self

    def alternateGridColorSet(self, prop: str):
        self.alternateGridColor = prop
        return self

    def titleSet(self, prop:AATitle):
        self.title = prop
        return self

    def typeSet(self, prop: AAChartAxisType):
        self.type = prop.value
        return self

    def dateTimeLabelFormatsSet(self, prop: AADateTimeLabelFormats):
        self.dateTimeLabelFormats = prop
        return self

    def dateTimeLabelFormatsSet(self, prop):
        self.dateTimeLabelFormats = prop
        return self

    def plotBandsSet(self, prop: List):
        self.plotBands = prop
        return self

    def plotLinesSet(self, prop: List):
        self.plotLines = prop
        return self

    def categoriesSet(self, prop: List):
        self.categories = prop
        return self

    def reversedSet(self, prop: bool):
        self.reversed = prop
        return self

    def gridLineWidthSet(self, prop: float):
        self.gridLineWidth = prop
        return self

    def gridLineColorSet(self, prop: str):
        self.gridLineColor = prop
        return self

    def gridLineDashStyleSet(self, prop: AAChartLineDashStyleType):
        self.gridLineDashStyle = prop.value
        return self

    def gridLineInterpolationSet(self, prop: str):
        self.gridLineInterpolation = prop
        return self

    def labelsSet(self, prop: AALabels):
        self.labels = prop
        return self

    def lineWidthSet(self, prop: float):
        self.lineWidth = prop
        return self

    def lineColorSet(self, prop: str):
        self.lineColor = prop
        return self

    def offsetSet(self, prop: float):
        self.offset = prop
        return self

    def allowDecimalsSet(self, prop: bool):
        self.allowDecimals = prop
        return self

    def maxSet(self, prop: float):
        self.max = prop
        return self

    def minSet(self, prop: float):
        self.min = prop
        return self

    def maxPaddingSet(self, prop: int):
        self.maxPadding = prop
        return self

    def minPaddingSet(self, prop: int):
        self.minPadding = prop
        return self

    def minTickIntervalSet(self, prop: int):
        self.minTickInterval = prop
        return self

    def minorGridLineColorSet(self, prop: str):
        self.minorGridLineColor = prop
        return self

    def minorGridLineDashStyleSet(self, prop: AAChartLineDashStyleType):
        self.minorGridLineDashStyle = prop.value
        return self

    def minorGridLineWidthSet(self, prop: float):
        self.minorGridLineWidth = prop
        return self

    def minorTickColorSet(self, prop: str):
        self.minorTickColor = prop
        return self

    def minorTickIntervalSet(self, prop: str):
        self.minorTickInterval = prop
        return self

    def minorTickLengthSet(self, prop: float):
        self.minorTickLength = prop
        return self

    def minorTickPositionSet(self, prop: str):
        self.minorTickPosition = prop
        return self

    def minorTickWidthSet(self, prop: float):
        self.minorTickWidth = prop
        return self

    def visibleSet(self, prop: bool):
        self.visible = prop
        return self

    def oppositeSet(self, prop: bool):
        self.opposite = prop
        return self

    def startOnTickSet(self, prop: bool):
        self.startOnTick = prop
        return self

    def endOnTickSet(self, prop: bool):
        self.endOnTick = prop
        return self

    def tickAmountSet(self, prop: int):
        self.tickAmount = prop
        return self

    def tickIntervalSet(self, prop: float):
        self.tickInterval = prop
        return self

    def crosshairSet(self, prop: AACrosshair):
        self.crosshair = prop
        return self

    def stackLabelsSet(self, prop: map):
        self.stackLabels = prop
        return self

    def tickWidthSet(self, prop: float):
        self.tickWidth = prop
        return self

    def tickLengthSet(self, prop: float):
        self.tickLength = prop
        return self

    def tickPositionSet(self, prop: str):
        self.tickPosition = prop
        return self

    def tickPositionsSet(self, prop: List):
        self.tickPositions = prop
        return self


 