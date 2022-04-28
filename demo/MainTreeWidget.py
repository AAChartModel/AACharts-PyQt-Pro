from random import random

from PySide6 import QtWidgets, QtCore

from aacharts.aachartcreator.AAChartModel import AAChartModel
from aacharts.aachartcreator.AASeriesElement import AASeriesElement
from aacharts.aachartcreator.PYChartView import PYChartView
from aacharts.aaenum.AAEnum import AAChartType, AAChartAnimationType, AAChartStackingType
from aacharts.aatool.AAColor import AAColor
from demo.AAOptionsProComposer import AAOptionsProComposer


class MainTreeWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.chartView = PYChartView()
        testChartModel = self.configureColorfulBarChart()
        self.chartView.aa_drawChartWithChartModel(testChartModel)


        # https://gist.github.com/fredrikaverpil/1fa4f3360ffdb1e69507
        folderTree = QtWidgets.QTreeWidget()


        sectionTitleArr = [
            "Pro Types Chart --- Pro类型图表",
        ]


        chartTypeTitleArr = [
            # Pro types chart
           [  "sankeyChart---桑基图",
              "variablepieChart---可变宽度的饼图",
              "treemapChart---树形图",
              "variwideChart---可变宽度的柱形图",
              "sunburstChart---旭日图",
              "dependencywheelChart---和弦图",
              "heatmapChart---热力图",
              "packedbubbleChart---气泡🎈填充图",
              "packedbubbleSplitChart---圆🎈堆积图",
              "vennChart---韦恩图",
              "dumbbellChart---哑铃图",
              "lollipopChart---棒棒糖🍭图",
              "streamgraphChart---流图",
              "columnpyramidChart---角锥柱形图",
              "tilemapChart---砖块图🧱||蜂巢图🐝",
              "simpleTreemapChart---简单矩形树🌲图",
              "drilldownTreemapChart---可下钻的矩形树🌲图",
              "xrangeChart---X轴范围图||甘特图||条码图",
              "vectorChart---向量图🏹",
              "bellcurveChart---贝尔曲线图",
              "timelineChart---时序图⌚️",
              "itemChart---议会项目图",
              "windbarbChart---风羽图",
              "networkgraphChart---力导关系图",
              "wordcloudChart---词云图",
              "eulerChart---欧拉图",
              "organizationChart---组织结构图",
              "arcdiagramChart1---弧形图1",
              "arcdiagramChart2---弧形图2",
              "arcdiagramChart3---弧形图3",
              "flameChart---火焰🔥图",
              "packedbubbleSpiralChart---渐进变化的气泡🎈图"
            ],
        ]

        for sectionIndex in range(len(sectionTitleArr)):
            sectionTitleStr = sectionTitleArr[sectionIndex]
            sectionIndexStr = f"{sectionIndex + 1}"
            sectionRoot = QtWidgets.QTreeWidgetItem(folderTree, [sectionIndexStr + "  " + sectionTitleStr])
            sectionRoot.setData(1, QtCore.Qt.EditRole, sectionIndexStr)

            singleSectionChartTypeTitleArr = chartTypeTitleArr[sectionIndex]
            for rowIndex in range(len(singleSectionChartTypeTitleArr)):
                rowIndexStr = f"{rowIndex + 1}"
                chartTypeStr = singleSectionChartTypeTitleArr[rowIndex]
                rowRoot = QtWidgets.QTreeWidgetItem(sectionRoot, [rowIndexStr + "  " + chartTypeStr])
                rowRoot.setData(1, QtCore.Qt.EditRole, sectionIndexStr)  # Data set to column 2, which is not visible
                rowRoot.setData(2, QtCore.Qt.EditRole, rowIndexStr)  # Data set to column 2, which is not visible

        def printer(treeItem):
            foldername = treeItem.text(0)
            sectionIndex = treeItem.text(1)
            rowIndexStr = treeItem.text(2)
            # treeItem.indexOfChild()
            print(foldername + ': ' + f"(Section Index: {sectionIndex})" + f"(Row Index: {rowIndex})")

            if len(rowIndexStr) > 0:
                sectionIndexValue = int(sectionIndex)
                rowIndexValue = int(rowIndexStr) - 1
                if sectionIndexValue == 1:
                   aaOptions = self.chartConfigurationWithSelectedIndex(rowIndexValue)
                   self.chartView.aa_drawChartWithChartOptions(aaOptions)


        folderTree.itemClicked.connect(lambda: printer(folderTree.currentItem()))

        folderTree.currentColumn()
        # Qt如何使QTreeWidget始终保持展开？https://blog.csdn.net/can3981132/article/details/52273800
        folderTree.setItemsExpandable(False)
        folderTree.expandAll()

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.chartView)
        self.layout.addWidget(folderTree)

        self.setWindowTitle("你好世界")

    def printer(treeItem):
        foldername = treeItem.text(0)
        comment = treeItem.text(1)
        data = treeItem.text(2)
        print(foldername + ': ' + comment + ' (' + data + ')')


    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

    def configureColorfulBarChart(self):
        colorsNameArr = [
            "red",
            "orange",
            "yellow",
            "green",
            "cyan",
            "blue",
            "purple",
            "gray",
            "darkGray",
            "lightGray",
            "magenta",
            "brown",
            "black"
        ]

        colorsArr = [
            AAColor.red,
            AAColor.orange,
            AAColor.yellow,
            AAColor.green,
            AAColor.cyan,
            AAColor.blue,
            AAColor.purple,
            AAColor.gray,
            AAColor.darkGray,
            AAColor.lightGray,
            AAColor.magenta,
            AAColor.brown,
            AAColor.black
        ]

        return (AAChartModel()
            .chartTypeSet(AAChartType.bar)
            .animationTypeSet(AAChartAnimationType.bounce)
            .titleSet("Colorful Chart")
            .subtitleSet("use AAColor to get color string")
            .dataLabelsEnabledSet(False)
            .categoriesSet(colorsNameArr)
            .colorsThemeSet(colorsArr)
            .stackingSet(AAChartStackingType.percent)
            .seriesSet([
            AASeriesElement()
                .nameSet("Tokyo")
                .dataSet([7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6])
                .colorByPointSet(True)
        ]))


    # https://www.highcharts.com/demo
    def chartConfigurationWithSelectedIndex(self, selectedIndex):
        if selectedIndex ==  0: return AAOptionsProComposer.sankeyChart()
        elif selectedIndex ==  1: return AAOptionsProComposer.variablepieChart()
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



