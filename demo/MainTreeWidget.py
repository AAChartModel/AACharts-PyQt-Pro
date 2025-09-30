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

        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)

        self.themes = {
            "light": {
                "label": "浅色主题",
                "window_bg": "#f4f6fd",
                "text_primary": "#1f2430",
                "text_secondary": "#617093",
                "frame_gradient_start": "rgba(255,255,255,0.94)",
                "frame_gradient_end": "rgba(237,241,255,0.94)",
                "frame_border": "rgba(45, 108, 223, 0.10)",
                "tree_item_selected_bg": "rgba(63,133,242,0.18)",
                "tree_item_selected_text": "#2d6cdf",
                "tree_item_hover_bg": "rgba(63,133,242,0.10)",
                "tree_primary": "#293041",
                "tree_secondary": "#6d7996",
                "input_bg": "rgba(255,255,255,0.7)",
                "input_bg_focus": "rgba(255,255,255,0.92)",
                "input_border": "rgba(45, 108, 223, 0.35)",
                "input_border_focus": "#2d6cdf",
                "accent": "#2d6cdf",
                "accent_hover": "#1f55b0",
                "accent_pressed": "#17448f",
                "accent_text": "#ffffff",
                "chart_bg": "#ffffff",
                "combo_bg": "rgba(255,255,255,0.78)",
                "combo_border": "rgba(45,108,223,0.28)",
                "combo_text": "#1f2430"
            },
            "dark": {
                "label": "深色主题",
                "window_bg": "#141823",
                "text_primary": "#e5e9f5",
                "text_secondary": "#9aa7c7",
                "frame_gradient_start": "rgba(33,39,55,0.96)",
                "frame_gradient_end": "rgba(23,28,40,0.96)",
                "frame_border": "rgba(96, 108, 150, 0.35)",
                "tree_item_selected_bg": "rgba(90,130,245,0.36)",
                "tree_item_selected_text": "#e6ecff",
                "tree_item_hover_bg": "rgba(90,130,245,0.20)",
                "tree_primary": "#f5f7ff",
                "tree_secondary": "#9aa7c7",
                "input_bg": "rgba(36,44,62,0.88)",
                "input_bg_focus": "rgba(43,51,72,0.94)",
                "input_border": "rgba(105,135,255,0.30)",
                "input_border_focus": "rgba(105,135,255,0.75)",
                "accent": "#5470ff",
                "accent_hover": "#405be0",
                "accent_pressed": "#2f48c2",
                "accent_text": "#f5f7ff",
                "chart_bg": "#1d2332",
                "combo_bg": "rgba(36,44,62,0.88)",
                "combo_border": "rgba(105,135,255,0.35)",
                "combo_text": "#e5e9f5"
            }
        }
        self.currentThemeKey = "light"

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

        headlineLabel = QtWidgets.QLabel("探索进阶数据可视化")
        headlineFont = QtGui.QFont(self.font())
        headlineFont.setPointSize(headlineFont.pointSize() + 3)
        headlineFont.setBold(True)
        headlineLabel.setFont(headlineFont)
        self.headlineLabel = headlineLabel

        self.folderTree.itemSelectionChanged.connect(self.handleTreeSelectionChanged)
        self.folderTree.expandAll()

        listContainer = QtWidgets.QFrame()
        self.listContainer = listContainer

        listLayout = QtWidgets.QVBoxLayout(listContainer)
        listLayout.setContentsMargins(18, 18, 18, 18)
        listLayout.setSpacing(12)
        headerLayout = QtWidgets.QHBoxLayout()
        headerLayout.addWidget(headlineLabel)
        headerLayout.addStretch()

        self.themeSelector = QtWidgets.QComboBox()
        for key, config in self.themes.items():
            self.themeSelector.addItem(config["label"], userData=key)
        self.themeSelector.currentIndexChanged.connect(self.handleThemeChanged)
        headerLayout.addWidget(self.themeSelector)

        listLayout.addLayout(headerLayout)
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
        self.layout.addWidget(self.backButton, alignment=QtCore.Qt.AlignRight)

        self.setWindowTitle("进阶高阶图表示例")

        self.applyTheme(force=True)


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

    def handleThemeChanged(self, index: int):
        selectedKey = self.themeSelector.itemData(index)
        if not selectedKey or selectedKey == self.currentThemeKey:
            return
        self.currentThemeKey = selectedKey
        self.applyTheme()

    def applyTheme(self, force: bool = False):
        theme = self.themes.get(self.currentThemeKey, self.themes["light"])

        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QtGui.QPalette.Window, QtGui.QColor(theme["window_bg"]))
        palette.setColor(QtGui.QPalette.Base, QtGui.QColor(theme["chart_bg"]))
        palette.setColor(QtGui.QPalette.Text, QtGui.QColor(theme["text_primary"]))
        self.setPalette(palette)

        self.headlineLabel.setStyleSheet(f"color: {theme['text_primary']};")

        treeStyle = f"""
            QTreeWidget#proChartTree {{
                border: none;
                background: transparent;
                font-size: 14px;
                color: {theme['tree_primary']};
            }}
            QTreeWidget#proChartTree::item {{
                padding: 6px 10px;
                border-radius: 6px;
                margin: 2px 4px;
            }}
            QTreeWidget#proChartTree::item:selected {{
                background: {theme['tree_item_selected_bg']};
                color: {theme['tree_item_selected_text']};
            }}
            QTreeWidget#proChartTree::item:hover:!selected {{
                background: {theme['tree_item_hover_bg']};
            }}
            QTreeWidget#proChartTree::branch:closed:has-children {{
                border-image: none;
                image: url();
            }}
            QTreeWidget#proChartTree::branch:open:has-children {{
                border-image: none;
                image: url();
            }}
        """
        self.folderTree.setStyleSheet(treeStyle)

        for sectionIndex in range(self.folderTree.topLevelItemCount()):
            sectionItem = self.folderTree.topLevelItem(sectionIndex)
            sectionItem.setForeground(0, QtGui.QBrush(QtGui.QColor(theme["text_primary"])) )
            for childIndex in range(sectionItem.childCount()):
                childItem = sectionItem.child(childIndex)
                childItem.setForeground(0, QtGui.QBrush(QtGui.QColor(theme["tree_primary"])) )
                childItem.setForeground(1, QtGui.QBrush(QtGui.QColor(theme["tree_secondary"])) )

        inputStyle = f"""
            QLineEdit {{
                border-radius: 8px;
                padding: 6px 12px;
                border: 1px solid {theme['input_border']};
                background: {theme['input_bg']};
                color: {theme['text_primary']};
            }}
            QLineEdit:focus {{
                border: 1px solid {theme['input_border_focus']};
                background: {theme['input_bg_focus']};
            }}
            QLineEdit::placeholder {{
                color: {theme['text_secondary']};
            }}
            QLineEdit QToolButton {{
                color: {theme['text_secondary']};
            }}
        """
        self.searchInput.setStyleSheet(inputStyle)

        comboStyle = f"""
            QComboBox {{
                border-radius: 8px;
                padding: 6px 12px;
                border: 1px solid {theme['combo_border']};
                background: {theme['combo_bg']};
                color: {theme['combo_text']};
            }}
            QComboBox::drop-down {{
                border: none;
            }}
            QComboBox QAbstractItemView {{
                border-radius: 8px;
                background: {theme['combo_bg']};
                color: {theme['combo_text']};
                selection-background-color: {theme['tree_item_selected_bg']};
                selection-color: {theme['tree_item_selected_text']};
            }}
        """
        self.themeSelector.setStyleSheet(comboStyle)

        self.listContainer.setStyleSheet(
            f"""
            QFrame {{
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                           stop:0 {theme['frame_gradient_start']},
                                           stop:1 {theme['frame_gradient_end']});
                border-radius: 14px;
                border: 1px solid {theme['frame_border']};
            }}
        """
        )

        self.chartView.setStyleSheet(
            f"""
            PYChartView {{
                background: {theme['chart_bg']};
                border-radius: 14px;
            }}
        """
        )

        self.backButton.setStyleSheet(
            f"""
            QPushButton {{
                padding: 8px 16px;
                border-radius: 10px;
                background: {theme['accent']};
                color: {theme['accent_text']};
                font-weight: 600;
            }}
            QPushButton:hover {{
                background: {theme['accent_hover']};
            }}
            QPushButton:pressed {{
                background: {theme['accent_pressed']};
            }}
        """
        )

        self.themeSelector.blockSignals(True)
        indexToSelect = self.themeSelector.findData(self.currentThemeKey)
        if indexToSelect >= 0 and (force or self.themeSelector.currentIndex() != indexToSelect):
            self.themeSelector.setCurrentIndex(indexToSelect)
        self.themeSelector.blockSignals(False)

        self.update()


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









