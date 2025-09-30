from PySide6 import QtWidgets, QtCore, QtGui

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
        testChartModel = AAOptionsProComposer.sankeyChart()
        self.chartView.aa_drawChartWithChartOptions(testChartModel)



        # https://gist.github.com/fredrikaverpil/1fa4f3360ffdb1e69507
        folderTree = QtWidgets.QTreeWidget()
        folderTree.setObjectName("proChartTree")
        folderTree.setColumnCount(2)
        folderTree.setHeaderLabels(["Chart", "Description"])
        folderTree.header().setDefaultAlignment(QtCore.Qt.AlignLeft)
        folderTree.header().setStretchLastSection(True)
        folderTree.setAlternatingRowColors(True)
        folderTree.setIndentation(16)
        folderTree.setExpandsOnDoubleClick(False)
        folderTree.setAnimated(True)
        folderTree.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        folderTree.setUniformRowHeights(False)
        folderTree.setStyleSheet(
            """
            QTreeWidget#proChartTree {
                border: none;
                background: transparent;
                font-size: 14px;
            }
            QTreeWidget#proChartTree::item {
                padding: 6px 10px;
                border-radius: 6px;
            }
            QTreeWidget#proChartTree::item:selected {
                background: rgba(63, 133, 242, 0.18);
                color: #2d6cdf;
            }
            QTreeWidget#proChartTree::item:hover:!selected {
                background: rgba(63, 133, 242, 0.1);
            }
            QTreeWidget#proChartTree::branch:closed:has-children {
                border-image: none;
                image: url();
            }
            QTreeWidget#proChartTree::branch:open:has-children {
                border-image: none;
                image: url();
            }
            """
        )


        sectionTitleArr = [
            "Pro Types Chart --- Pro类型图表",
        ]

        chartTypeTitleArr = [
            ["sankeyChart---桑基图",
             "variablepieChart---可变宽度的饼图🍪",
             "treemapChart---树形图🌲",
             "variwideChart---可变宽度的柱形图📊",
             "sunburstChart---旭日图🌞",
             "dependencywheelChart---和弦图🎸",
             "heatmapChart---热力图🔥",
             "packedbubbleChart---气泡填充图🎈",
             "packedbubbleSplitChart---圆堆积图🎈",
             "vennChart---韦恩图",
             "dumbbellChart---哑铃图🏋",
             "lollipopChart---棒棒糖图🍭",
             "streamgraphChart---流图🌊",
             "columnpyramidChart---角锥柱形图△",
             "tilemapChart---砖块图🧱||蜂巢图🐝",
             "simpleTreemapChart---简单矩形树图🌲",
             "drilldownTreemapChart---可下钻的矩形树图🌲",
             "xrangeChart---X轴范围图||甘特图||条码图☰☲☱☴☵☶☳☷",
             "vectorChart---向量图🏹",
             "bellcurveChart---贝尔曲线图",
             "timelineChart---时序图⌚️",
             "itemChart---议会项目图",
             "windbarbChart---风羽图",
             "networkgraphChart---力导关系图✢✣✤✥",
             "wordcloudChart---词云️图☁️",
             "eulerChart---欧拉图",
             "organizationChart---组织结构图",
             "arcdiagramChart1---弧形图1",
             "arcdiagramChart2---弧形图2",
             "arcdiagramChart3---弧形图3",
             "flameChart---火焰🔥图",
             "packedbubbleSpiralChart---渐进变化的气泡🎈图",
             "solidgaugeChart---活动图🏃️",
             "largeDataHeatmapChart---大数据量热力图",
             "parallelCoordinatesSplineChart---平行坐标曲线图",
             "parallelCoordinatesLineChart---平行坐标折线图📈",
             "bulletChart---子弹图💣",
             "histogramChart---直方图📊",
             ]
        ]

        primaryTitleFont = QtGui.QFont(self.font())
        primaryTitleFont.setPointSize(primaryTitleFont.pointSize() + 1)
        primaryTitleFont.setBold(True)

        secondaryTitleFont = QtGui.QFont(self.font())
        secondaryTitleFont.setPointSize(secondaryTitleFont.pointSize() - 1)

        for sectionIndex, sectionTitleStr in enumerate(sectionTitleArr):
            sectionRoot = QtWidgets.QTreeWidgetItem(folderTree, [sectionTitleStr, ""])
            sectionRoot.setFirstColumnSpanned(True)
            sectionRoot.setFlags(sectionRoot.flags() & ~QtCore.Qt.ItemIsSelectable)
            sectionRoot.setFont(0, primaryTitleFont)
            sectionRoot.setData(0, QtCore.Qt.UserRole, sectionIndex)

            singleSectionChartTypeTitleArr = chartTypeTitleArr[sectionIndex]
            for rowIndex, chartTypeStr in enumerate(singleSectionChartTypeTitleArr):
                rawParts = chartTypeStr.split("---", maxsplit=1)
                primaryTitle = rawParts[0].strip()
                secondaryTitle = rawParts[1].strip() if len(rawParts) > 1 else ""
                secondaryTitle = secondaryTitle.replace("||", " · ")

                displayPrimary = f"{rowIndex + 1:02d}. {primaryTitle}"
                displaySecondary = secondaryTitle

                rowRoot = QtWidgets.QTreeWidgetItem(sectionRoot, [displayPrimary, displaySecondary])
                rowRoot.setFont(0, primaryTitleFont)
                rowRoot.setFont(1, secondaryTitleFont)
                rowRoot.setData(0, QtCore.Qt.UserRole, sectionIndex)
                rowRoot.setData(0, QtCore.Qt.UserRole + 1, rowIndex)
                rowRoot.setData(0, QtCore.Qt.UserRole + 2, chartTypeStr)
                rowRoot.setToolTip(0, chartTypeStr)
                rowRoot.setToolTip(1, chartTypeStr)

        self.folderTree = folderTree

        self.searchInput = QtWidgets.QLineEdit()
        self.searchInput.setPlaceholderText("搜索或筛选图表类型…")
        self.searchInput.textChanged.connect(self.filterTreeItems)
        self.searchInput.setClearButtonEnabled(True)
        self.searchInput.setStyleSheet(
            """
            QLineEdit {
                border-radius: 8px;
                padding: 6px 12px;
                border: 1px solid rgba(45, 108, 223, 0.35);
                background: rgba(255, 255, 255, 0.6);
            }
            QLineEdit:focus {
                border-color: #2d6cdf;
                background: rgba(255, 255, 255, 0.85);
            }
            """
        )

        headlineLabel = QtWidgets.QLabel("探索进阶数据可视化")
        headlineFont = QtGui.QFont(self.font())
        headlineFont.setPointSize(headlineFont.pointSize() + 3)
        headlineFont.setBold(True)
        headlineLabel.setFont(headlineFont)
        headlineLabel.setStyleSheet("color: #2d2f36;")

        self.folderTree.itemSelectionChanged.connect(self.handleTreeSelectionChanged)
        self.folderTree.expandAll()

        listContainer = QtWidgets.QFrame()
        listContainer.setStyleSheet(
            """
            QFrame {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                           stop:0 rgba(255,255,255,0.92),
                                           stop:1 rgba(237,241,255,0.92));
                border-radius: 14px;
                border: 1px solid rgba(45, 108, 223, 0.08);
            }
            """
        )

        listLayout = QtWidgets.QVBoxLayout(listContainer)
        listLayout.setContentsMargins(18, 18, 18, 18)
        listLayout.setSpacing(12)
        listLayout.addWidget(headlineLabel)
        listLayout.addWidget(self.searchInput)
        listLayout.addWidget(self.folderTree)

        splitter = QtWidgets.QSplitter(QtCore.Qt.Vertical)
        splitter.addWidget(self.chartView)
        splitter.addWidget(listContainer)
        splitter.setSizes([480, 280])
        splitter.setStretchFactor(0, 3)
        splitter.setStretchFactor(1, 2)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(18, 18, 18, 18)
        self.layout.setSpacing(16)
        self.layout.addWidget(splitter)

        self.backButton = QtWidgets.QPushButton("返回示例总览")
        self.backButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backButton.setStyleSheet(
            """
            QPushButton {
                padding: 8px 16px;
                border-radius: 10px;
                background: #2d6cdf;
                color: white;
                font-weight: 600;
            }
            QPushButton:hover {
                background: #1f55b0;
            }
            QPushButton:pressed {
                background: #17448f;
            }
            """
        )
        self.layout.addWidget(self.backButton, alignment=QtCore.Qt.AlignRight)

        self.setWindowTitle("进阶高阶图表示例")


    @QtCore.Slot()
    def handleTreeSelectionChanged(self):
        currentItem = self.folderTree.currentItem()
        if currentItem is None:
            return

        rowIndex = currentItem.data(0, QtCore.Qt.UserRole + 1)
        if rowIndex is None:
            return

        aaOptions = self.chartConfigurationWithSelectedIndex(rowIndex)
        if aaOptions is not None:
            self.chartView.aa_drawChartWithChartOptions(aaOptions)

    def filterTreeItems(self, keyword: str):
        keyword = keyword.strip().lower()
        matchAll = keyword == ""

        for sectionIndex in range(self.folderTree.topLevelItemCount()):
            sectionItem = self.folderTree.topLevelItem(sectionIndex)
            sectionHasMatch = False

            for rowIndex in range(sectionItem.childCount()):
                childItem = sectionItem.child(rowIndex)
                sourceText = childItem.data(0, QtCore.Qt.UserRole + 2) or ""
                itemMatches = matchAll or any(
                    keyword in text
                    for text in [childItem.text(0).lower(), childItem.text(1).lower(), sourceText.lower()]
                )
                childItem.setHidden(not itemMatches)
                if itemMatches:
                    sectionHasMatch = True

            sectionItem.setHidden(not sectionHasMatch and not matchAll)
            sectionItem.setExpanded(True)


    # https://www.highcharts.com/demo
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









