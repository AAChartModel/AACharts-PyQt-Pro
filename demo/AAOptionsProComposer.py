from aacharts.aachartcreator.AASeriesElement import AASeriesElement
from aacharts.aaenum.AAEnum import AAChartType
from aacharts.aaoptionsmodel.AAChart import AAChart, AAChartEvents
from aacharts.aaoptionsmodel.AADataLabels import AADataLabels, AAFilter, AATextPath
from aacharts.aaoptionsmodel.AALegend import AALegend
from aacharts.aaoptionsmodel.AAOptions import AAOptions
from aacharts.aaoptionsmodel.AAPane import AAPane, AABackgroundElement
from aacharts.aaoptionsmodel.AAPlotBandsElement import AAPlotBandsElement
from aacharts.aaoptionsmodel.AASeries import AAEvents
from aacharts.aaoptionsmodel.AASubtitle import AASubtitle
from aacharts.aaoptionsmodel.AATitle import AATitle
from aacharts.aaoptionsmodel.AATooltip import AATooltip
from aacharts.aaoptionsmodelpro.AABulletDataElement import AABulletDataElement
from aacharts.aaoptionsmodelpro.AAColorAxis import AAColorAxis, AADataClassesElement
from aacharts.aaoptionsmodelpro.AAData import AAData
from aacharts.aaoptionsmodelpro.AAHeatmap import AAHeatmap
from aacharts.aaoptionsmodelpro.AALayoutAlgorithm import AALayoutAlgorithm
from aacharts.aaoptionsmodelpro.AALevelsElement import AALevelsElement, AAColorVariation
from aacharts.aaoptionsmodelpro.AAPackedbubble import AAPackedbubble
from aacharts.aaoptionsmodelpro.AAParallelAxes import AAParallelAxes
from aacharts.aaoptionsmodelpro.AASolidgauge import AASolidgauge
from aacharts.aaoptionsmodelpro.AASolidgaugeDataElement import AASolidgaugeDataElement
from aacharts.aaoptionsmodelpro.AATreemap import AATreemap
from aacharts.aatool.AAStringPurer import AAStringPurer
from demo.AAOptionsCSV import AAOptionsCSV
from demo.AAOptionsData import AAOptionsData
from aacharts.aaoptionsmodel.AAShadow import AAShadow
from aacharts.aaoptionsmodel.AAZonesElement import AAZonesElement
from aacharts.aatool.AAColor import AAColor, AARgbaColor
from aacharts.aatool.AAGradientColor import AAGradientColor
from aacharts.aachartcreator.AASeriesElement import AASeriesElement
from aacharts.aachartcreator.AAChartModel import AAChartModel, AAChartSymbolStyleType, AAChartSymbolType, AAChartType
from aacharts.aatool.AAGradientColor import AAGradientColor
from aacharts.aachartcreator.AASeriesElement import AASeriesElement
from aacharts.aachartcreator.AAChartModel import *
from aacharts.aaoptionsmodel.AAMarker import AAMarker, AAMarkerStates, AAMarkerHover
from aacharts.aaoptionsmodel.AADataElement import AADataElement
from aacharts.aaoptionsmodel.AADataLabels import AADataLabels
from aacharts.aaoptionsmodel.AAStates import AAStates, AAHover, AAHalo, AAInactive, AASelect
from aacharts.aatool.AAGradientColor import AALinearGradientDirection
from aacharts.aaoptionsmodel.AAPlotOptions import AAColumn
# from demo.AAChartSymbolConstant import *

from demo.AAOptionsSeries import AAOptionsSeries


class AAOptionsProComposer:

  @staticmethod
  def sankeyChart():
    return (AAOptions()
    .titleSet(AATitle()
              .textSet("AAChartKit-Pro 桑基图"))
    .colorsSet([
        AARgbaColor(137, 78, 36, 1.0),
        AARgbaColor(220, 36, 30, 1.0),
        AARgbaColor(255, 206, 0, 1.0),
        AARgbaColor(1, 114, 41, 1.0),
        AARgbaColor(0, 175, 173, 1.0),
        AARgbaColor(215, 153, 175, 1.0),
        AARgbaColor(106, 114, 120, 1.0),
        AARgbaColor(114, 17, 84, 1.0),
        AARgbaColor(0, 0, 0, 1.0),
        AARgbaColor(0, 24, 168, 1.0),
        AARgbaColor(0, 160, 226, 1.0),
        AARgbaColor(106, 187, 170, 1.0),
               ])
    .seriesSet([
        AASeriesElement()
        .typeSet(AAChartType.sankey)
        .keysSet(["from", "to", "weight"])
        .dataSet(AAOptionsData.sankeyData()),
               ]))


  @staticmethod
  def variablepieChart():
    aaChart = (AAChart()
    .typeSet(AAChartType.variablepie))

    aaTitle = (AATitle()
    .textSet("不同国家人口密度及面积对比"))

    aaSubtitle = (AASubtitle()
    .textSet("扇区长度（圆周方法）表示面积，宽度（纵向）表示人口密度"))

    aaTooltip = (AATooltip()
    .enabledSet(True)
    .headerFormatSet("")
    .pointFormatSet("<span style=""color:{point.color"">\u25CF</span> <b>():point.name</b><br/>""面积 (平方千米): <b>{point.y</b><br/>""人口密度 (每平方千米人数): <b>{point.z</b><br/>"""))

    aaOptions = (AAOptions()
    .chartSet(aaChart)
    .titleSet(aaTitle)
    .subtitleSet(aaSubtitle)
    .tooltipSet(aaTooltip)
    .seriesSet([
        AASeriesElement()
        .nameSet("countries")
        .innerSizeSet("20%")
        .dataLabelsSet(AADataLabels()
                       .enabledSet(False))
        .dataSet(AAOptionsData.variablepieData())
               ]))

    return aaOptions


  @staticmethod
  def treemapWithLevelsData():
    return (AAOptions()
    .titleSet(AATitle()
              .textSet("Fruit Consumption Situation"))
    .legendSet(AALegend()
               .enabledSet(False))
    .seriesSet([
        AASeriesElement()
        .typeSet(AAChartType.treemap)
        .levelsSet([
            AALevelsElement()
            .levelSet(1)
            .layoutAlgorithmSet("sliceAndDice")
            .dataLabelsSet(AADataLabels()
                           .enabledSet(True)
                           .alignSet(AAChartAlignType.left)
                           .verticalAlignSet(AAChartVerticalAlignType.top)
                           # .styleSet(AAStyleColorSizeWeight(AAColor.whiteColor, 15, AAChartFontWeightTypeBold))
                           )
                   ])
        .dataSet(AAOptionsData.treemapWithLevelsData())]))


  @staticmethod
  def variwideChart():
    aaChart = (AAChart()
    .typeSet(AAChartType.variwide))

    aaTitle = (AATitle()
    .textSet("2016 年欧洲各国人工成本"))

    aaSubtitle = (AASubtitle()
    .textSet("数据来源:EUROSTAT"))

    aaXAxis = (AAXAxis()
    .visibleSet(True)
    .typeSet(AAChartAxisType.category)
    .titleSet(AATitle()
              .textSet(" 柱子宽度与 GDP 成正比")))

    aaTooltip = (AATooltip()
    .enabledSet(True)
    .pointFormatSet("人工成本： <b>€ {point.y}/h</b><br>' + 'GDP: <b>€ {point.z} 百万</b><br>"))

    aaLegend = (AALegend()
    .enabledSet(False))

    seriesElementArr = [
        AASeriesElement()
        .nameSet("人工成本")
        .dataSet(AAOptionsData.variwideData())
        .dataLabelsSet(AADataLabels()
                       .enabledSet(True)
                       .formatSet("€{point.y:.0f}"))
        .colorByPointSet(True)]

    aaOptions = (AAOptions()
    .chartSet(aaChart)
    .titleSet(aaTitle)
    .subtitleSet(aaSubtitle)
    .xAxisSet(aaXAxis)
    .tooltipSet(aaTooltip)
    .legendSet(aaLegend)
    .seriesSet(seriesElementArr))

    return aaOptions


  @staticmethod
  def sunburstChart():
    aaChart = (AAChart()
    .typeSet(AAChartType.sunburst))

    aaTitle = (AATitle()
    .textSet("2017 世界人口分布"))

    aaSubtitle = (AASubtitle()
    .textSet("数据来源:<href=""https:#en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)"">Wikipedia</a>"))

    aaTooltip = (AATooltip()
    .enabledSet(True)
    .pointFormatSet("<b>{point.name}</b>的人口数量是：<b>{point.value}</b>"))

    aaLegend = (AALegend()
    .enabledSet(False))

    seriesElementArr = [
        AASeriesElement()
        .allowDrillToNodeSet(True)
        .levelsSet([
            AALevelsElement()
            .levelSet(2)
            .colorByPointSet(True)
            .layoutAlgorithmSet("sliceAndDice")
            ,
            AALevelsElement()
            .levelSet(3)
            .colorVariationSet(AAColorVariation()
                               .keySet("brightness")
                               .toSet(-0.5))
            ,
            AALevelsElement()
            .levelSet(4)
            .colorVariationSet(AAColorVariation()
                               .keySet("brightness")
                               .toSet(0.5))

                   ])
        .dataSet(AAOptionsData.sunburstData())
    ]

    aaOptions = (AAOptions()
    .chartSet(aaChart)
    .titleSet(aaTitle)
    .subtitleSet(aaSubtitle)
    .tooltipSet(aaTooltip)
    .legendSet(aaLegend)
    .seriesSet(seriesElementArr))

    return aaOptions


  @staticmethod
  def dependencywheelChart():
    return (AAOptions()
    .chartSet(AAChart()
              .marginLeftSet(20)
              .marginRightSet(20))
    .titleSet(AATitle()
              .textSet("AAChartKit-Pro 和弦图"))
    .seriesSet([
        AASeriesElement()
        .typeSet(AAChartType.dependencywheel)
        .nameSet("Dependency wheel series")
        .keysSet(["from", "to", "weight"])
        .dataSet(AAOptionsData.dependencywheelData())
        .dataLabelsSet(AADataLabels()
                       .enabledSet(True)
                       .colorSet("#333")
                       .textPathSet(AATextPath()
                                    .enabledSet(True)
                                    .attributesSet({"dy": 5}))
                       .distanceSet(10))
               ]))


# # https:#jshare.com.cn/demos/hhhhiz
  @staticmethod
  def heatmapChart():
    return (AAOptions()
        .chartSet(AAChart()
              .typeSet(AAChartType.heatmap))
    .titleSet(AATitle()
              .textSet("Sales per employee per weekday"))
    .xAxisSet(AAXAxis()
              .visibleSet(True)
              .categoriesSet([
                  "Alexander", "Marie", "Maximilian", "Sophia",
                  "Lukas", "Maria", "Leon", "Anna", "Tim", "Laura"
                             ]))
    .yAxisSet(AAYAxis()
              .visibleSet(True)
              .categoriesSet(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
              .titleSet(AATitle()
                        .textSet("")))
    .colorAxisSet(AAColorAxis()
                  .minSet(0)
                  .minColorSet(AAColor.white)
                  .maxColorSet("#7cb5ec"))
    .legendSet(AALegend()
               .enabledSet(True)
               .alignSet(AAChartAlignType.right)
               .layoutSet(AAChartLayoutType.vertical)
               .verticalAlignSet(AAChartVerticalAlignType.top)
               .ySet(25))
    .tooltipSet(AATooltip()
                .enabledSet(True)
                .formatterSet("""
            function () {
                    return '<b>' + this.series.xAxis.categories[this.point.x] + '</b> sold <br><b>' +
                        this.point.value + '</b> items on <br><b>' + this.series.yAxis.categories[this.point.y] + '</b>'
                    }
                """)
                )
    .seriesSet([
        AASeriesElement()
        .nameSet("Sales")
        .borderWidthSet(1)
        .dataSet(AAOptionsData.heatmapData())
        .dataLabelsSet(AADataLabels()
                       .enabledSet(True)
                       .colorSet(AAColor.red))
               ]))

# # https:#www.highcharts.com.cn/demo/highcharts/packed-bubble
  @staticmethod
  def packedbubbleChart():
    return (AAOptions()
    .chartSet(AAChart()
              .typeSet(AAChartType.packedbubble))
    .titleSet(AATitle()
              .textSet("2014 年世界各地碳排放量"))
    .tooltipSet(AATooltip()
                .enabledSet(True)
                .useHTMLSet(True)
                .pointFormatSet("<b>{point.name}:</b> {point.y}m CO<sub>2</sub>"))
    .plotOptionsSet(AAPlotOptions()
                    .packedbubbleSet(AAPackedbubble()
                                     .minSizeSet("30%")
                                     .maxSizeSet("120%")
                                     .zMinSet(0)
                                     .zMaxSet(1000)
                                     .layoutAlgorithmSet(AALayoutAlgorithm() #packedbubbleChart 和 packedbubbleSplitChart 只有layoutAlgorithm这一段不一样
                                                         .gravitationalConstantSet(0.02)
                                                         .splitSeriesSet(False))
                                     .dataLabelsSet(AADataLabels()
                                                    .enabledSet(True)
                                                    .formatSet("{point.name}")
                                                    .filterSet(AAFilter()
                                                               .propertySet("y")
                                                               .operatorSet(">")
                                                               .valueSet(250))
                                                    )))
    .seriesSet(AAOptionsSeries.packedbubbleSeries()))


# https:#www.highcharts.com.cn/demo/highcharts/packed-bubble-split
  @staticmethod
  def packedbubbleSplitChart():
    return (AAOptions()
    .chartSet(AAChart()
              .typeSet(AAChartType.packedbubble))
    .titleSet(AATitle()
              .textSet("2014 年世界各地碳排放量"))
    .tooltipSet(AATooltip()
                .enabledSet(True)
                .useHTMLSet(True)
                .pointFormatSet("<b>{point.name:</b>():point.ym CO<sub>2</sub>"))
    .plotOptionsSet(AAPlotOptions()
                    .packedbubbleSet(AAPackedbubble()
                                     .minSizeSet("30%")
                                     .maxSizeSet("120%")
                                     .zMinSet(0)
                                     .zMaxSet(1000)
                                     .layoutAlgorithmSet(AALayoutAlgorithm() #packedbubbleChart 和 packedbubbleSplitChart 只有layoutAlgorithm这一段不一样
                                                         .gravitationalConstantSet(0.05)
                                                         .splitSeriesSet(True)
                                                         .seriesInteractionSet(False)
                                                         .dragBetweenSeriesSet(True)
                                                         .parentNodeLimitSet(True))
                                     .dataLabelsSet(AADataLabels()
                                                    .enabledSet(True)
                                                    .formatSet("{point.name}")
                                                    .filterSet(AAFilter()
                                                               .propertySet("y")
                                                               .operatorSet(">")
                                                               .valueSet(250))
                                                    )))
    .seriesSet(AAOptionsSeries.packedbubbleSeries()))



  @staticmethod
  def vennChart():
    return (AAOptions()
    .titleSet(AATitle()
              .textSet("The Unattainable Triangle"))
    .seriesSet([
        AASeriesElement()
        .typeSet(AAChartType.venn)
        .dataSet(AAOptionsData.vennData())]))


  @staticmethod
  def dumbbellChart():
    aaChart = (AAChart()
    .typeSet(AAChartType.dumbbell)
    .invertedSet(True))

    aaTitle = (AATitle()
    .textSet("各国预期寿命变化"))

    aaSubtitle = (AASubtitle()
    .textSet("1960 vs 2018"))

    aaXAxis = (AAXAxis()
    .visibleSet(True)
    .typeSet(AAChartAxisType.category))

    aaYAxis = (AAYAxis()
    .visibleSet(True)
    .titleSet(AATitle()
              .textSet("Life Expectancy (years)")))

    aaTooltip = (AATooltip()
    .enabledSet(True))

    aaLegend = (AALegend()
    .enabledSet(False))

    seriesElementArr = [
        AASeriesElement()
        .nameSet("各国预期寿命变化")
        .dataSet(AAOptionsData.dumbbellData())
    ]

    aaOptions = (AAOptions()
    .chartSet(aaChart)
    .titleSet(aaTitle)
    .subtitleSet(aaSubtitle)
    .xAxisSet(aaXAxis)
    .yAxisSet(aaYAxis)
    .tooltipSet(aaTooltip)
    .legendSet(aaLegend)
    .seriesSet(seriesElementArr))

    return aaOptions


  @staticmethod
  def lollipopChart():
    aaChart = (AAChart()
    .typeSet(AAChartType.lollipop))

    aaTitle = (AATitle()
    .textSet("世界十大人口国家"))

    aaSubtitle = (AASubtitle()
    .textSet("2018"))

    aaXAxis = (AAXAxis()
    .visibleSet(True)
    .typeSet(AAChartAxisType.category))

    aaYAxis = (AAYAxis()
    .visibleSet(True)
    .titleSet(AATitle()
              .textSet("人口")))

    aaTooltip = (AATooltip()
    .enabledSet(True))

    aaLegend = (AALegend()
    .enabledSet(False))

    seriesElementArr = [
        AASeriesElement()
        .nameSet("Population")
        .dataSet(AAOptionsData.lollipopData())
    ]

    aaOptions = (AAOptions()
    .chartSet(aaChart)
    .titleSet(aaTitle)
    .subtitleSet(aaSubtitle)
    .xAxisSet(aaXAxis)
    .yAxisSet(aaYAxis)
    .tooltipSet(aaTooltip)
    .legendSet(aaLegend)
    .seriesSet(seriesElementArr))

    return aaOptions


  @staticmethod
  def streamgraphChart():
    return (AAOptions()
    .chartSet(AAChart()
              .typeSet(AAChartType.streamgraph))
    .colorsSet([
        "#7cb5ec","#434348","#90ed7d","#f7a35c","#8085e9",
        "rgb(255,143,179)","rgb(255,117,153)",
        "#f15c80","#e4d354","#2b908f","#f45b5b","#91e8e1","#7cb5ec","#434348","#f7a35c",
        "rgb(119,212,100)","rgb(93,186,74)","rgb(68,161,49)"
               ])
    .titleSet(AATitle()
              .textSet("冬季奥运会奖牌分布"))
    .subtitleSet(AASubtitle()
                 .textSet("1924-2014"))
    .xAxisSet(AAXAxis()
              .visibleSet(True)
              .typeSet(AAChartAxisType.category)
              .categoriesSet([
                  "", "1924", "1928", "1932", "1936", "1940", "1944", "1948", "1952", "1956", "1960",
                  "1964", "1968", "1972", "1976", "1980", "1984", "1988", "1992", "1994", "1998",
                  "2002", "2006", "2010", "2014"
                             ]))
    .yAxisSet(AAYAxis()
              .visibleSet(False))
    .tooltipSet(AATooltip()
                .enabledSet(True))
    .legendSet(AALegend()
               .enabledSet(False))
    .seriesSet(AAOptionsSeries.streamgraphSeries()))


  @staticmethod
  def columnpyramidChart():
    return (AAOptions()
    .chartSet(AAChart()
              .typeSet(AAChartType.columnpyramid))
    .titleSet(AATitle()
              .textSet("世界 5 大金字塔"))
    .xAxisSet(AAXAxis()
              .visibleSet(True)
              .typeSet(AAChartAxisType.category))
    .yAxisSet(AAYAxis()
              .visibleSet(True)
              .titleSet(AATitle()
                        .textSet("高度 (m)")))
    .tooltipSet(AATooltip()
                .enabledSet(True)
                .valueSuffixSet(" m"))
    .seriesSet([
        AASeriesElement()
        .nameSet("Height")
        .colorByPointSet(True)
        .dataSet(AAOptionsData.columnpyramidData())
               ]))


  @staticmethod
  def tilemapChart():
    return (AAOptions()
    .chartSet(AAChart()
              .typeSet(AAChartType.tilemap))
    .titleSet(AATitle()
              .textSet("U.S. states by population in 2016"))
    .xAxisSet(AAXAxis()
              .visibleSet(False))
    .yAxisSet(AAYAxis()
              .visibleSet(False))
    .colorAxisSet(AAColorAxis()
                  .dataClassesSet([
                    AADataClassesElement()
                        .fromSet(0)
                        .toSet(1000000)
                        .colorSet("#F9EDB3")
                        .nameSet("< 1M"),
                    AADataClassesElement()
                        .fromSet(1000000)
                        .toSet(5000000)
                        .colorSet("#FFC428")
                        .nameSet("1M - 5M"),
                    AADataClassesElement()
                        .fromSet(5000000)
                        .toSet(20000000)
                        .colorSet("#F9EDB3")
                        .nameSet("5M - 20M"),
                    AADataClassesElement()
                        .fromSet(20000000)
                        .colorSet("#FF2371")
                        .nameSet("> 20M"),
                  ]))
    .tooltipSet(AATooltip()
                .enabledSet(True)
                .headerFormatSet("")
                .valueSuffixSet("The population of <b> {point.name}</b> is <b>{point.value}</b>"))
    .plotOptionsSet(AAPlotOptions()
                    .seriesSet(AASeries()
                               .dataLabelsSet(AADataLabels()
                                              .enabledSet(True)
                                              .formatSet("{point.hc-a2}")
                                              .colorSet(AAColor.white)
                                              .styleSet(AAStyle()
                                                        .textOutlineSet("none")))))
    .seriesSet([
        AASeriesElement()
        .nameSet("Height")
        .colorByPointSet(True)
        .dataSet(AAOptionsData.tilemapData())
               ]))


  @staticmethod
  def treemapWithColorAxisData():
    return (AAOptions()
    .chartSet(AAChart()
              .typeSet(AAChartType.treemap))
    .titleSet(AATitle()
              .textSet("矩形树图"))
    .colorAxisSet(AAColorAxis()
                  .minColorSet(AAColor.white)
                  .maxColorSet(AAColor.red))
    .seriesSet([
        AASeriesElement()
        .dataSet(AAOptionsData.treemapWithColorAxisData())
               ]))


  @staticmethod
  def drilldownTreemapChart():
    return (AAOptions()
    .chartSet(AAChart()
              .typeSet(AAChartType.treemap))
    .titleSet(AATitle()
              .textSet("2012年，全球每10w人口死亡率"))
    .subtitleSet(AASubtitle()
                 .textSet("点击下钻"))
    .plotOptionsSet(AAPlotOptions()
                    .treemapSet(AATreemap()
                                .allowTraversingTreeSet(True)
                                .layoutAlgorithmSet("squarified")))
    .seriesSet([
        AASeriesElement()
        .typeSet(AAChartType.treemap)
        .levelsSet([
            AALevelsElement()
            .levelSet(1)
            .dataLabelsSet(AADataLabels()
                           .enabledSet(True))
            .borderWidthSet(3)
                   ])
        .dataSet(AAOptionsData.drilldownTreemapData())
               ]))


  @staticmethod
  def xrangeChart():
    return (AAOptions()
    .chartSet(AAChart()
              .typeSet(AAChartType.xrange))
    .colorsSet([
        "#7cb5ec","#434348","#90ed7d","#f7a35c","#8085e9",
        "rgb(255,143,179)","rgb(255,117,153)",
        "#f15c80","#e4d354","#2b908f","#f45b5b","#91e8e1","#7cb5ec","#434348","#f7a35c",
        "rgb(119,212,100)","rgb(93,186,74)","rgb(68,161,49)"
               ])
    .titleSet(AATitle()
              .textSet(""))
    .yAxisSet(AAYAxis()
              .visibleSet(True)
              .titleSet(AATitle()
                        .textSet(""))
              .reversedSet(True)
              .categoriesSet(["原型","开发","测试","上线"])
              .gridLineWidthSet(0))
    .legendSet(AALegend()
               .enabledSet(False))
    .plotOptionsSet(AAPlotOptions()
                    .seriesSet(AASeries()
                               .pointPaddingSet(0)
                               .groupPaddingSet(0)))
    .seriesSet([
        AASeriesElement()
        .borderRadiusSet(2)
        .dataSet(AAOptionsData.xrangeData())
               ]))


  @staticmethod
  def vectorChart():
    return (AAOptions()
    .chartSet(AAChart()
              .typeSet(AAChartType.vector))
    .colorsSet(["red"])
    .titleSet(AATitle()
              .textSet("AAChartKit-Pro Vector plot"))
    .seriesSet([
        AASeriesElement()
        .nameSet("Sample vector field")
        .dataSet(AAOptionsData.vectorData())
               ]))


  @staticmethod
  def bellcurveChart():
    return (AAOptions()
    .titleSet(AATitle()
              .textSet("Bell curve"))
    .xAxisSet([
        AATitle()
        .textSet("Data"),
        AATitle()
        .textSet("Bell curve")
                  ])
    .yAxisSet([
        AATitle()
        .textSet("Data"),
        AATitle()
        .textSet("Bell curve")
                  ])
    .seriesSet([
        AASeriesElement()
        .nameSet("Bell curve")
        .typeSet(AAChartType.bellcurve)
        .xAxisSet(1)
        .yAxisSet(1)
        .baseSeriesSet(1)
        .zIndexSet(-1)
        ,
        AASeriesElement()
        .nameSet("Data")
        .typeSet(AAChartType.scatter)
        .markerSet(AAMarker()
                   .fillColorSet(AAColor.white)#点的填充色(用来设置折线连接点的填充色)
                   .lineWidthSet(2)#外沿线的宽度(用来设置折线连接点的轮廓描边的宽度)
                   .lineColorSet(""))#外沿线的颜色(用来设置折线连接点的轮廓描边颜色，当值为空字符串时，默认取数据点或数据列的颜色))
        .dataSet(AAOptionsData.bellcurveData())
               ]))


  @staticmethod
  def timelineChart():
    return (AAOptions()
    .chartSet(AAChart()
              .typeSet(AAChartType.timeline))
    .titleSet(AATitle()
              .textSet("人类太空探索时间表"))
    .subtitleSet(AASubtitle()
                 .textSet("数据来源: https:#en.wikipedia.org/wiki/Timeline_of_space_exploration"))
    .yAxisSet(AAYAxis()
              .visibleSet(False))
    .seriesSet([
        AASeriesElement()
        .dataSet(AAOptionsData.timelineData())
               ]))


  @staticmethod
  def itemChart():
    return (AAOptions()
    .chartSet(AAChart()
              .typeSet(AAChartType.item))
    .titleSet(AATitle()
              .textSet("AAChartKit-Pro item chart"))
    .subtitleSet(AASubtitle()
                 .textSet("Parliament visualization"))
    .legendSet(AALegend()
               .enabledSet(False))
    .seriesSet([
        AASeriesElement()
        .nameSet("Representatives")
        .keysSet(["name","y","color","label"])
        .dataSet(AAOptionsData.itemData())
        .dataLabelsSet(AADataLabels()
                       .enabledSet(False))
        .sizeSet("170%")
               ]))


  @staticmethod
  def windbarbChart():
    return (AAOptions()
    .titleSet(AATitle()
              .textSet("AAChartKit-Pro Wind Barbst"))
    .xAxisSet(AAXAxis()
              .offsetSet(40))
    .seriesSet([
        AASeriesElement()
        .typeSet(AAChartType.windbarb)
        .nameSet("Wind")
        .dataSet(AAOptionsData.windbarbData()),
        AASeriesElement()
        .typeSet(AAChartType.area)
        .nameSet("Wind speed")
        .dataSet(AAOptionsData.windbarbData())
        .keysSet(["y"])
        .markerSet(AAMarker()
                   .fillColorSet(AAColor.white)#点的填充色(用来设置折线连接点的填充色)
                   .lineWidthSet(5)#外沿线的宽度(用来设置折线连接点的轮廓描边的宽度)
                   .lineColorSet(""))#外沿线的颜色(用来设置折线连接点的轮廓描边颜色，当值为空字符串时，默认取数据点或数据列的颜色))
               ]))


  @staticmethod
  def networkgraphChart():
    return (AAOptions()
    .chartSet(AAChart()
              .typeSet(AAChartType.networkgraph))
    .titleSet(AATitle()
              .textSet("The Indo-European Laungauge Tree"))
    .subtitleSet(AASubtitle()
                 .textSet("A Force-Directed Network Graph in Highcharts"))
    .seriesSet([
        AASeriesElement()
        .dataLabelsSet(AADataLabels()
                       .enabledSet(False))
        .dataSet(AAOptionsData.networkgraphData()),
               ]))


  @staticmethod
  def wordcloudChart():
    return (AAOptions()
    .chartSet(AAChart()
              .typeSet(AAChartType.wordcloud))
    .titleSet(AATitle()
              .textSet("词云图"))
    .seriesSet([
        AASeriesElement()
        .dataSet(AAOptionsData.wordcloudData()),
               ]))


  @staticmethod
  def eulerChart():
    return (AAOptions()
    .chartSet(AAChart()
              .typeSet(AAChartType.venn))
    .titleSet(AATitle()
              .textSet("欧拉图和韦恩图的关系"))
    .tooltipSet(AATooltip()
                .enabledSet(True)
                .headerFormatSet(AAStringPurer.pureJSString("<span style=\"color:{point.color}\">○</span>" +
                                  "<span style=\"font-size: 14px\"> {point.point.name}</span><br/>"))
                .pointFormatSet(AAStringPurer.pureJSString("{point.description}<br><span style=\"font-size: 10px\">Source: Wikipedia</span>")))
    .seriesSet([
        AASeriesElement()
        .dataSet(AAOptionsData.eulerData()),
               ]))


  @staticmethod
  def organizationChart():
    return (AAOptions()
        .chartSet(AAChart()
#            .heightSet(600)
            .invertedSet(True))
        .titleSet(AATitle()
            .textSet("Highsoft 公司组织结构"))
        .seriesSet([
            AASeriesElement()
                .typeSet(AAChartType.organization)
                .nameSet("Highsoft")
                .keysSet(["from", "to"])
                .dataSet(AAOptionsData.organizationData())
                .levelsSet([
                    AALevelsElement()
                        .levelSet(0)
                        .colorSet("silver")
                        .dataLabelsSet(AADataLabels()
                            .colorSet(AAColor.black))
                        .heightSet(25)
                    ,
                    AALevelsElement()
                        .levelSet(1)
                        .colorSet("silver")
                        .dataLabelsSet(AADataLabels()
                            .colorSet(AAColor.black))
                        .heightSet(25)
                    ,
                    AALevelsElement()
                        .levelSet(2)
                        .colorSet("#980104")
                    ,
                    AALevelsElement()
                        .levelSet(4)
                        .colorSet("#359154")
                ])
                .nodesSet(AAOptionsData.organizationNodesData())
                .colorByPointSet(False)
                .colorSet("#007ad0")
                .dataLabelsSet(AADataLabels()
                    .colorSet(AAColor.white))
                .borderColorSet(AAColor.white)
                .nodeWidthSet(65)
            ])
        .tooltipSet(AATooltip()
            # .outsideSet(True)
                    ))


#https:#www.highcharts.com/docs/chart-and-series-types/arc-diagram
  @staticmethod
  def arcdiagramChart1():
    return (AAOptions()
        .colorsSet(["#293462", "#a64942", "#fe5f55", "#fff1c1", "#5bd1d7", "#ff502f", "#004d61", "#ff8a5c", "#fff591", "#f5587b", "#fad3cf", "#a696c8", "#5BE7C4", "#266A2E", "#593E1A"])
        .titleSet(AATitle()
            .textSet("Main train connections in Europe"))
        .seriesSet([
            AASeriesElement()
                .keysSet(["from", "to", "weight"])
                .typeSet(AAChartType.arcdiagram)
                .nameSet("Train connections")
                .linkWeightSet(1)
                .centeredLinksSet(True)
                .dataLabelsSet(AADataLabels()
                    .rotationSet(90)
                    .ySet(30)
                    .alignSet(AAChartAlignType.left)
                    .colorSet(AAColor.black))
                .offsetSet("65%")
                .dataSet(AAOptionsData.arcdiagram1Data())
            ]))


  @staticmethod
  def arcdiagramChart2():
    return (AAOptions()
        .titleSet(AATitle()
            .textSet("Highcharts Arc Diagram"))
        .subtitleSet(AASubtitle()
            .textSet("Arc Diagram with marker symbols"))
        .seriesSet([
            AASeriesElement()
                .linkWeightSet(1)
                .keysSet(["from", "to", "weight", ])
                .typeSet(AAChartType.arcdiagram)
                .markerSet(AAMarker()
                    .symbolSet(AAChartSymbolType.triangle.value)
                    .lineWidthSet(2)
                    .lineColorSet(AAColor.white))
                .centeredLinksSet(True)
                .dataLabelsSet(AADataLabels()
                    .formatSet("{point.fromNode.name} → {point.toNode.name}")
                    .nodeFormatSet("{point.name}")
                    .colorSet(AAColor.black)
                    .linkTextPathSet(AATextPath()
                        .enabledSet(True))
            )
                .dataSet(AAOptionsData.arcdiagram2Data())
            ]))


  @staticmethod
  def arcdiagramChart3():
    return (AAOptions()
        .chartSet(AAChart()
            .invertedSet(True))
        .titleSet(AATitle()
            .textSet("Highcharts Inverted Arc Diagram"))
        .seriesSet([
            AASeriesElement()
                .keysSet(["from", "to", "weight", ])
#                .centerPosSet("50%")
                .typeSet(AAChartType.arcdiagram)
                .dataLabelsSet(AADataLabels()
                    .alignSet(AAChartAlignType.right)
                    .xSet(-20)
                    .ySet(-2)
                    .colorSet("#333333")
                    .overflowSet("allow")
                    .paddingSet(0)
            )
                .offsetSet("60%")
                .dataSet(AAOptionsData.arcdiagram3Data())
            ]))


  @staticmethod
  def flameChart():
    return (AAOptions()
        .chartSet(AAChart()
            .invertedSet(True))
        .titleSet(AATitle()
            .alignSet(AAChartAlignType.left)
            .textSet("Flame chart (layout: flame)"))
        .subtitleSet(AASubtitle()
            .alignSet(AAChartAlignType.left)
            .textSet("Highcharts chart rendering process"))
        .legendSet(AALegend()
            .enabledSet(False))
        .xAxisSet([
            AAXAxis()
                .visibleSet(False),
            AAXAxis()
                .visibleSet(False)
                .startOnTickSet(False)
                .endOnTickSet(False)
                .minPaddingSet(0)
                .maxPaddingSet(0)
            ])
        .yAxisSet([
            AAYAxis()
                .visibleSet(False),
            AAYAxis()
                .visibleSet(False)
                .minSet(0)
                .maxPaddingSet(0)
                .startOnTickSet(False)
                .endOnTickSet(False)
            ])
        .seriesSet([
            AASeriesElement()
                .typeSet(AAChartType.flame)
                .dataSet(AAOptionsData.flameData())
                .yAxisSet(1)
                .xAxisSet(1),
            AASeriesElement()
                .visibleSet(False)
                .sizeSet("100%")
                .typeSet(AAChartType.sunburst)
                .dataSet(AAOptionsData.sunburst2Data())
                .allowDrillToNodeSet(True)
                .cursorSet("pointer")
                .levelsSet([
                    AALevelsElement()
                        .levelSet(1)
                       # .levelIsConstantSet(False)
                        .dataLabelsSet(AADataLabels()
                            .enabledSet(False))
                    ])
                .dataLabelsSet(AADataLabels()
                    .textPathSet(AATextPath()
                        .attributesSet({"dy": 5})
                        .enabledSet(True))
                               )
            ])
        .tooltipSet(AATooltip()
            .headerFormatSet("")
            .pointFormatSet("selfSize of {point.name} is {point.value}")))


  @staticmethod
  def packedbubbleSpiralChart():
    return (AAOptions()
        .chartSet(AAChart()
            .typeSet(AAChartType.packedbubble)
#            .heightSet("100%")
                  )
        .titleSet(AATitle()
            .textSet("Carbon emissions around the world (2014)"))
        .tooltipSet(AATooltip()
            .useHTMLSet(True)
            .pointFormatSet("{point.name}: {point.y}m CO2"))
        .plotOptionsSet(AAPlotOptions()
            .packedbubbleSet(AAPackedbubble()
                .useSimulationSet(False)
                .minSizeSet("20%")
                .maxSizeSet("80%")
                .dataLabelsSet(AADataLabels()
                    .enabledSet(True)
                    .formatSet("{point.name}")
                    .filterSet(AAFilter()
                        .propertySet("y")
                        .operatorSet(">")
                        .valueSet(250))
                    .styleSet(AAStyle()
                        .colorSet(AAColor.black)
                        .textOutlineSet("none")
                        .fontWeightSet(AAChartFontWeightType.regular)))))
        .seriesSet(AAOptionsSeries.packedbubbleSeries()))



  @staticmethod
  def solidgaugeChart():
      return (AAOptions()
      .chartSet(AAChart()
                .typeSet(AAChartType.solidgauge)
                # .heightSet("110%")
                 .eventsSet(AAChartEvents()
                 .loadSet("""
                 function () {
                if (!this.series[0].icon) {
                    this.series[0].icon = this.renderer.path(['M', -8, 0, 'L', 8, 0, 'M', 0, -8, 'L', 8, 0, 0, 8])
                        .attr({
                            stroke: '#303030',
                            'stroke-linecap': 'round',
                            'stroke-linejoin': 'round',
                            'stroke-width': 2,
                            zIndex: 10
                        })
                        .add(this.series[2].group);
                }
                this.series[0].icon.translate(
                    this.chartWidth / 2 - 10,
                    this.plotHeight / 2 - this.series[0].points[0].shapeArgs.innerR -
                        (this.series[0].points[0].shapeArgs.r - this.series[0].points[0].shapeArgs.innerR) / 2
                );

                if (!this.series[1].icon) {
                    this.series[1].icon = this.renderer.path(
                        ['M', -8, 0, 'L', 8, 0, 'M', 0, -8, 'L', 8, 0, 0, 8,
                            'M', 8, -8, 'L', 16, 0, 8, 8]
                    )
                        .attr({
                            stroke: '#ffffff',
                            'stroke-linecap': 'round',
                            'stroke-linejoin': 'round',
                            'stroke-width': 2,
                            zIndex: 10
                        })
                        .add(this.series[2].group);
                }
                this.series[1].icon.translate(
                    this.chartWidth / 2 - 10,
                    this.plotHeight / 2 - this.series[1].points[0].shapeArgs.innerR -
                        (this.series[1].points[0].shapeArgs.r - this.series[1].points[0].shapeArgs.innerR) / 2
                );

                if (!this.series[2].icon) {
                    this.series[2].icon = this.renderer.path(['M', 0, 8, 'L', 0, -8, 'M', -8, 0, 'L', 0, -8, 8, 0])
                        .attr({
                            stroke: '#303030',
                            'stroke-linecap': 'round',
                            'stroke-linejoin': 'round',
                            'stroke-width': 2,
                            zIndex: 10
                        })
                        .add(this.series[2].group);
                }

                this.series[2].icon.translate(
                    this.chartWidth / 2 - 10,
                    this.plotHeight / 2 - this.series[2].points[0].shapeArgs.innerR -
                        (this.series[2].points[0].shapeArgs.r - this.series[2].points[0].shapeArgs.innerR) / 2
                );
                }
                 """))
      )
      .titleSet(AATitle()
                .textSet("Activity")
                .styleSet(AAStyle()
                          .fontSizeSet(24)))
      .tooltipSet(AATooltip()
                  .borderWidthSet(0)
                  .backgroundColorSet("none")
                  .shadowSet(False)
                  .styleSet(AAStyle()
                            .fontSizeSet(16)
                            .textOutlineSet("3px"))
                  .valueSuffixSet("%")
                  .pointFormatSet("{series.name}{point.y}")
                  .positionerSet("""
                  function(labelWidth) {
                    let position = {};
                    position["x"] = (this.chart.chartWidth - labelWidth) / 2 - 100;
                    position["y"] = (this.chart.plotHeight / 2) + 15;
                    return position;
                }
                  """))
      .paneSet(AAPane()
               .startAngleSet(0)
               .endAngleSet(360)
               .backgroundSet([
                   AABackgroundElement()
                   .outerRadiusSet("112%")
                   .innerRadiusSet("88%")
                   .backgroundColorSet("rgba(124,181,236,0.3)")
                   .borderWidthSet(0),
                   AABackgroundElement()
                   .outerRadiusSet("87%")
                   .innerRadiusSet("63%")
                   .backgroundColorSet("rgba(67,67,72,0.3)")
                   .borderWidthSet(0),
                   AABackgroundElement()
                   .outerRadiusSet("62%")
                   .innerRadiusSet("38%")
                   .backgroundColorSet("rgba(144,237,125,0.3)")
                   .borderWidthSet(0)
               ]))
      .yAxisSet(AAYAxis()
                .minSet(0)
                .maxSet(100)
                .lineWidthSet(0)
                .tickPositionsSet([]))
      .plotOptionsSet(AAPlotOptions()
                      .solidgaugeSet(AASolidgauge()
                                     .dataLabelsSet(AADataLabels()
                                                    .enabledSet(False))
                                     .linecapSet("round")
                                     .stickyTrackingSet(False)
                                     .roundedSet(True)))
      .seriesSet([
          AASeriesElement()
          .nameSet("Move")
          .dataSet([
              AASolidgaugeDataElement()
              .colorSet("#7cb5ec")
              .radiusSet("112%")
              .innerRadiusSet("88%")
              .ySet(80)
          ]),
          AASeriesElement()
          .nameSet("Exercise")
          .dataSet([
              AASolidgaugeDataElement()
              .colorSet("#434348")
              .radiusSet("87%")
              .innerRadiusSet("63%")
              .ySet(65)
          ]),
          AASeriesElement()
          .nameSet("Stand")
          .dataSet([
              AASolidgaugeDataElement()
              .colorSet("#90ed7d")
              .radiusSet("62%")
              .innerRadiusSet("39%")
              .ySet(50)
          ]),
          AASeriesElement()
          .nameSet("Move")
          .dataSet([
              AASolidgaugeDataElement()
              .colorSet("#f7a35c")
              .radiusSet("38%")
              .innerRadiusSet("28%")
              .ySet(80)
          ]),
          AASeriesElement()
          .nameSet("Exercise")
          .dataSet([
              AASolidgaugeDataElement()
              .colorSet("#8085e9")
              .radiusSet("27%")
              .innerRadiusSet("17%")
              .ySet(65)
          ]),
          AASeriesElement()
          .nameSet("Stand")
          .dataSet([
              AASolidgaugeDataElement()
              .colorSet("#f15c80")
              .radiusSet("16%")
              .innerRadiusSet("6%")
              .ySet(50)
          ])
      ]))

  @staticmethod
  def largeDataHeatmapChart():
      csvMap: map = (AAOptionsCSV.csvData())
      csvStr = csvMap["csv"]
      return (AAOptions()
              .dataSet(AAData()
                       .csvSet(AAStringPurer.pureJSString2(csvStr))
      .parsedSet("""
      function () {
          start = +new Date();
                 }
      """))
      .chartSet(AAChart()
                .typeSet(AAChartType.heatmap)
                .marginSet([60, 10, 80, 50]))
      .titleSet(AATitle()
                .textSet("大型热力图")
                .alignSet(AAChartAlignType.left)
                .xSet(40))
      .subtitleSet(AASubtitle()
                   .textSet("2013每天每小时的热力变化")
                   .alignSet(AAChartAlignType.left)
                   .xSet(40))
      .xAxisSet(AAXAxis()
                .typeSet(AAChartAxisType.datetime)
                .minSet(1356998400000)
                .maxSet(1388534400000)
                .labelsSet(AALabels()
                           .alignSet(AAChartAlignType.left)
                           .xSet(5)
                           .ySet(14)
                           .formatSet("{value:%B}"))
                #            .showLastLabelSet(False)
                .tickLengthSet(16))
      .yAxisSet(AAYAxis()
                .titleSet(AATitle()
                          .textSet(None))
                .labelsSet(AALabels()
                           .formatSet("{value}:00"))
                .minPaddingSet(0)
                .maxPaddingSet(0)
                .startOnTickSet(False)
                .endOnTickSet(False)
                .tickPositionsSet([0, 6, 12, 18, 24])
                .tickWidthSet(1)
                .minSet(0)
                .maxSet(23)
                .reversedSet(True))
      .colorAxisSet(AAColorAxis()
                    .stopsSet([
          [0, "#3060cf", ],
          [0.5, "#fffbbc", ],
          [0.9, "#c4463a", ],
          [1, "#c4463a", ]
      ])
                    .minSet(-15)
                    .maxSet(25)
                    .startOnTickSet(False)
                    .endOnTickSet(False)
                    .labelsSet(AALabels()
                               .formatSet("{value}℃"))
                    )
      .seriesSet([
          AAHeatmap()
          .borderWidthSet(0)
          .colsizeSet(86400000)
          .tooltipSet(AATooltip()
                      .headerFormatSet("Temperature")
                      #                    .pointFormatSet("{point.x:%e %b, %Y} {point.y}:00: {point.value} ℃")
                      )
          .turboThresholdSet(1.7976931348623157e+308)
      ]))

  @staticmethod
  def parallelCoordinatesSplineChart():
      marathonDataArr = AAOptionsData.marathonData()
      seriesArr = []
      for i in range(len(marathonDataArr)):
          aaSeriesElement = (AASeriesElement()
          .nameSet("Runner")
          .dataSet(marathonDataArr[i])
          .shadowSet(False))
          seriesArr.append(aaSeriesElement)

      return (AAOptions()
              .chartSet(AAChart()
                        .typeSet(AAChartType.spline)
                        .parallelCoordinatesSet(True)
                        .parallelAxesSet(AAParallelAxes()
                                         .lineWidthSet(2)))
              .titleSet(AATitle()
                        .textSet("Marathon set"))
              .plotOptionsSet(AAPlotOptions()
                              .seriesSet(AASeries()
                                         .animationSet(False)
                                         .markerSet(AAMarker()
                                                    .enabledSet(False)
                                                    .statesSet(AAMarkerStates()
                                                               .hoverSet(AAMarkerHover()
                                                                         .enabledSet(False))))
                                         .statesSet(AAStates()
                                                    .hoverSet(AAHover()
                                                              .haloSet(AAHalo()
                                                                       .sizeSet(0))))
                                         .eventsSet(AAEvents()
                                                    .mouseOverSet(""))))
              .tooltipSet(AATooltip()
                          .pointFormatSet("●{series.name}: {point.formattedValue}"))
              .xAxisSet(AAXAxis()
                        .categoriesSet([
          "Training date",
          "Miles for training run",
          "Training time",
          "Shoe brand",
          "Running pace per mile",
          "Short or long",
          "After 2004",
      ])
                        .offsetSet(10))
              .yAxisSet([
          AAYAxis()
          .typeSet(AAChartAxisType.datetime)
          .tooltipValueFormatSet("{value:%Y-%m-%d}"),
          AAYAxis()
          .minSet(0)
          .tooltipValueFormatSet("{value} mile(s)"),
          AAYAxis()
          .typeSet(AAChartAxisType.datetime)
          .minSet(0)
          .labelsSet(AALabels()
                     .formatSet("{value:%H:%M}")),
          AAYAxis()
          .categoriesSet([
              "Other",
              "Adidas",
              "Mizuno",
              "Asics",
              "Brooks",
              "New Balance",
              "Izumi",
          ]),
          AAYAxis()
          .typeSet(AAChartAxisType.datetime),
          AAYAxis()
          .categoriesSet([
              "> 5miles",
              "< 5miles",
          ]),
          AAYAxis()
          .categoriesSet([
              "Before",
              "After",
          ])
      ])
              .colorsSet([AARgbaColor(255, 0, 0, 0.1), ])
              .seriesSet(seriesArr))

  @staticmethod
  def parallelCoordinatesLineChart():
      aaOptions = AAOptionsProComposer.parallelCoordinatesSplineChart()
      aaOptions.chart.typeSet(AAChartType.line)
      aaOptions.colorsSet([AAGradientColor.linearGradient2(
          AALinearGradientDirection.toRight,
          [
              [0.00, "#febc0f0F"],#颜色字符串设置支持十六进制类型和 rgba 类型
              [0.25, "#FF14d4E6"],
              [0.50, "#0bf8f5E6"],
              [0.75, "#F33c52E6"],
              [1.00, "#1904ddE6"],
          ])])
      return aaOptions

  @staticmethod
  def bulletChart():
      return (AAOptions()
              .chartSet(AAChart()
                        .marginTopSet(40)
                        .invertedSet(True)
                        #            .marginLeftSet(135)
                        .heightSet(200)
                        .typeSet(AAChartType.bullet))
              .titleSet(AATitle()
                        .textSet("2017 年公司运营情况"))
              .xAxisSet(AAXAxis()
                        .categoriesSet(["营收千美元", ]))
              .yAxisSet(AAYAxis()
                        .gridLineWidthSet(0)
                        .plotBandsSet([
          AAPlotBandsElement()
          .fromSet(0)
          .toSet(150)
          .colorSet("#666"),
          AAPlotBandsElement()
          .fromSet(150)
          .toSet(225)
          .colorSet("#999"),
          AAPlotBandsElement()
          .fromSet(225)
          .toSet(9000000000)
          .colorSet("#bbb")
      ])
              .titleSet(None))
              .plotOptionsSet(AAPlotOptions()
                              .seriesSet(AASeries()
                                         .pointPaddingSet(0.25)
                                         .borderWidthSet(0)
                                         #                .colorSet("#000")
                                         #                .targetOptionsSet(AATargetOptions()
                                         #                    .widthSet("200%"))
                                         ))
              .legendSet(AALegend()
                         .enabledSet(False))
              .seriesSet([
          AASeriesElement()
          .dataSet([
              AABulletDataElement()
              .ySet(275)
              .targetSet(250)
          ])
      ])
              .tooltipSet(AATooltip()
                          .pointFormatSet("{point.y} （目标值 {point.target}）")))

  @staticmethod
  def histogramChart():
      return (AAOptions()
      .titleSet(AATitle()
                .textSet("AAChartKit-Pro Histogram"))
      .xAxisSet([
          AAXAxis()
          .titleSet(AATitle()
                    .textSet("Data")),
          AAXAxis()
          .titleSet(AATitle()
                    .textSet("Histogram"))
          .oppositeSet(True)
      ])
      .yAxisSet([
          AAYAxis()
          .titleSet(AATitle()
                    .textSet("Data")),
          AAYAxis()
          .titleSet(AATitle()
                    .textSet("Histogram"))
          .oppositeSet(True)
      ])
      .seriesSet([
          AASeriesElement()
          .nameSet("Histogram")
          .typeSet(AAChartType.histogram)
          .xAxisSet(1)
          .yAxisSet(1)
          .baseSeriesSet("s1")
          .zIndexSet(-1),
          AASeriesElement()
          .nameSet("Data")
          .typeSet(AAChartType.scatter)
          .dataSet(AAOptionsData.bellcurveData())
          .idSet("s1")
          .markerSet(AAMarker()
                     .fillColorSet(AAColor.white)  # 点的填充色(用来设置折线连接点的填充色)
                     .lineWidthSet(2)  # 外沿线的宽度(用来设置折线连接点的轮廓描边的宽度)
                     .lineColorSet(""))  # 外沿线的颜色(用来设置折线连接点的轮廓描边颜色，当值为空字符串时，默认取数据点或数据列的颜色))
      ]))

