from PySide6 import QtWidgets

from aacharts.aachartcreator.PYChartView import PYChartView
from demo.AAOptionsProComposer import AAOptionsProComposer


class OfficialChartSampleView(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QtWidgets.QVBoxLayout(self)

        self.label = QtWidgets.QLabel("This is the second view")
        layout.addWidget(self.label)

        # self.gridLayout = QtWidgets.QGridLayout()
        # for i in range(3):
        #     for j in range(3):
        #         button = QtWidgets.QPushButton(f"Button {i*3 + j + 1}")
        #         chartView = PYChartView()
        #         testChartModel = AAOptionsProComposer.lollipopChart()
        #         self.gridLayout.addWidget(chartView, i, j)
        #         chartView.aa_drawChartWithChartOptions(testChartModel)
        #
        #
        # layout.addLayout(self.gridLayout)

        layout.addWidget(CustomCollectionView())


        self.backButton = QtWidgets.QPushButton("Back to First View")
        layout.addWidget(self.backButton)


class CustomCollectionView(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QtWidgets.QVBoxLayout(self)

        # self.label = QtWidgets.QLabel("This is the second view")
        # layout.addWidget(self.label)

        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        # self.scrollArea.setFixedHeight(400)  # 设置固定高度
        self.gridWidget = QtWidgets.QWidget()
        self.gridLayout = QtWidgets.QGridLayout(self.gridWidget)
        self.scrollArea.setWidget(self.gridWidget)
        for i in range(12):
            for j in range(3):
                button = QtWidgets.QPushButton(f"Button {i*3 + j + 1}")
                chartView = PYChartView()
                chartView.setFixedHeight(300)  # 设置固定高度

                testChartModel = self.chartConfigurationWithSelectedIndex(i * 3 + j)
                # testChartModel = AAOptionsProComposer.bulletChart()
                self.gridLayout.addWidget(chartView, i, j)
                chartView.aa_drawChartWithChartOptions(testChartModel)


        # layout.addLayout(self.gridLayout)
        layout.addWidget(self.scrollArea)
        # self.backButton = QtWidgets.QPushButton("Back to First View")
        # layout.addWidget(self.backButton)

    def chartConfigurationWithSelectedIndex(self, selectedIndex):
        if selectedIndex   == 0:  return AAOptionsProComposer.sankeyChart()
        elif selectedIndex ==  1: return AAOptionsProComposer.bulletChart()
        elif selectedIndex ==  2: return AAOptionsProComposer.treemapWithLevelsData()
        elif selectedIndex ==  3: return AAOptionsProComposer.variwideChart()
        elif selectedIndex ==  4: return AAOptionsProComposer.sunburstChart()
        elif selectedIndex ==  5: return AAOptionsProComposer.dependencywheelChart()
        elif selectedIndex ==  6: return AAOptionsProComposer.heatmapChart()
        elif selectedIndex ==  7: return AAOptionsProComposer.packedbubbleChart()
        elif selectedIndex ==  8: return AAOptionsProComposer.packedbubbleSplitChart()
        elif selectedIndex ==  9: return AAOptionsProComposer.vennChart()
        elif selectedIndex == 10: return AAOptionsProComposer.dumbbellChart()
        elif selectedIndex == 11: return AAOptionsProComposer.lollipopChart()
        elif selectedIndex == 12: return AAOptionsProComposer.streamgraphChart()
        elif selectedIndex == 13: return AAOptionsProComposer.columnpyramidChart()
        elif selectedIndex == 14: return AAOptionsProComposer.tilemapChart()
        elif selectedIndex == 15: return AAOptionsProComposer.treemapWithColorAxisData()
        elif selectedIndex == 16: return AAOptionsProComposer.drilldownTreemapChart()
        elif selectedIndex == 17: return AAOptionsProComposer.xrangeChart()
        elif selectedIndex == 18: return AAOptionsProComposer.vectorChart()
        elif selectedIndex == 19: return AAOptionsProComposer.bellcurveChart()
        elif selectedIndex == 20: return AAOptionsProComposer.timelineChart()
        elif selectedIndex == 21: return AAOptionsProComposer.itemChart()
        elif selectedIndex == 22: return AAOptionsProComposer.windbarbChart()
        elif selectedIndex == 23: return AAOptionsProComposer.networkgraphChart()
        elif selectedIndex == 24: return AAOptionsProComposer.wordcloudChart()
        elif selectedIndex == 25: return AAOptionsProComposer.eulerChart()
        elif selectedIndex == 26: return AAOptionsProComposer.organizationChart()
        elif selectedIndex == 27: return AAOptionsProComposer.arcdiagramChart1()
        elif selectedIndex == 28: return AAOptionsProComposer.arcdiagramChart2()
        elif selectedIndex == 29: return AAOptionsProComposer.arcdiagramChart3()
        elif selectedIndex == 30: return AAOptionsProComposer.flameChart()
        elif selectedIndex == 31: return AAOptionsProComposer.packedbubbleSpiralChart()
        elif selectedIndex == 32: return AAOptionsProComposer.solidgaugeChart()
        elif selectedIndex == 33: return AAOptionsProComposer.largeDataHeatmapChart()
        elif selectedIndex == 34: return AAOptionsProComposer.parallelCoordinatesSplineChart()
        elif selectedIndex == 35: return AAOptionsProComposer.parallelCoordinatesLineChart()
        elif selectedIndex == 36: return AAOptionsProComposer.bulletChart()
        elif selectedIndex == 37: return AAOptionsProComposer.histogramChart()
