from aacharts.aachartcreator.AASeriesElement import AASeriesElement
from aacharts.aaenum.AAEnum import AAChartType
from aacharts.aaoptionsmodel.AAChart import AAChart
from aacharts.aaoptionsmodel.AADataLabels import AADataLabels
from aacharts.aaoptionsmodel.AALegend import AALegend
from aacharts.aaoptionsmodel.AAOptions import AAOptions
from aacharts.aaoptionsmodel.AASubtitle import AASubtitle
from aacharts.aaoptionsmodel.AATitle import AATitle
from aacharts.aaoptionsmodel.AATooltip import AATooltip
from aacharts.aaoptionsmodelpro.AAColorAxis import AAColorAxis, AADataClassesElement
from aacharts.aaoptionsmodelpro.AALayoutAlgorithm import AALayoutAlgorithm
from aacharts.aaoptionsmodelpro.AALevelsElement import AALevelsElement, AAColorVariation
from aacharts.aaoptionsmodelpro.AAPackedbubble import AAPackedbubble
from aacharts.aaoptionsmodelpro.AATreemap import AATreemap
from demo.AAOptionsData import AAOptionsData
from aacharts.aaoptionsmodel.AAShadow import AAShadow
from aacharts.aaoptionsmodel.AAZonesElement import AAZonesElement
from aacharts.aatool.AAColor import AAColor
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
from demo.AAChartSymbolConstant import *

from demo.AAOptionsSeries import AAOptionsSeries


class AAOptionsProComposer:

  @staticmethod
  def sankeyChart():
    return (AAOptions()
    .titleSet(AATitle()
              .textSet("AAChartKit-Pro 桑基图"))
    .colorsSet([
        # AARgbaColor(137, 78, 36, 1.0),
        # AARgbaColor(220, 36, 30, 1.0),
        # AARgbaColor(255, 206, 0, 1.0),
        # AARgbaColor(1, 114, 41, 1.0),
        # AARgbaColor(0, 175, 173, 1.0),
        # AARgbaColor(215, 153, 175, 1.0),
        # AARgbaColor(106, 114, 120, 1.0),
        # AARgbaColor(114, 17, 84, 1.0),
        # AARgbaColor(0, 0, 0, 1.0),
        # AARgbaColor(0, 24, 168, 1.0),
        # AARgbaColor(0, 160, 226, 1.0),
        # AARgbaColor(106, 187, 170, 1.0),
               ])
    .seriesSet([
        AASeriesElement()
        .typeSet(AAChartType.sankey)
        .keysSet(["from", "to", "weight"])
        .dataSet(AAOptionsData.sankeyData),
               ]))


  @staticmethod
  def variablepieChart():
    aaChart = (AAChart()
    .typeSet(AAChartType.Variablepie))
    
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
        .dataSet(AAOptionsData.variablepieData)
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
        .typeSet(AAChartType.Treemap)
        .levelsSet([
            AALevelsElement()
            .levelSet(1)
            .layoutAlgorithmSet("sliceAndDice")
            .dataLabelsSet(AADataLabels()
                           .enabledSet(True)
                           .alignSet(AAChartAlignType.Left)
                           .verticalAlignSet(AAChartVerticalAlignType.Top)
                           # .styleSet(AAStyleColorSizeWeight(AAColor.whiteColor, 15, AAChartFontWeightTypeBold))
                           )
                   ])
        .dataSet(AAOptionsData.treemapWithLevelsData)]))


  @staticmethod
  def variwideChart():
    aaChart = (AAChart()
    .typeSet(AAChartType.Variwide))
    
    aaTitle = (AATitle()
    .textSet("2016 年欧洲各国人工成本"))
    
    aaSubtitle = (AASubtitle()
    .textSet("数据来源:EUROSTAT"))
    
    aaXAxis = (AAXAxis()
    .visibleSet(True)
    .typeSet("category")
    .titleSet(AATitle()
              .textSet(" 柱子宽度与 GDP 成正比")))
    
    aaTooltip = (AATooltip()
    .enabledSet(True)
    .pointFormatSet("人工成本： <b>€():point.y/h</b><br>' + 'GDP: <b>€():point.z 百万</b><br>"))
    
    aaLegend = (AALegend()
    .enabledSet(False))
    
    seriesElementArr = [
        AASeriesElement()
        .nameSet("人工成本")
        .dataSet(AAOptionsData.variwideData)
        .dataLabelsSet(AADataLabels()
                       .enabledSet(True)
                       .formatSet("€{point.y:.0f"))
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
    .typeSet(AAChartType.Sunburst))
    
    aaTitle = (AATitle()
    .textSet("2017 世界人口分布"))
    
    aaSubtitle = (AASubtitle()
    .textSet("数据来源:<href=""https:#en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)"">Wikipedia</a>"))
    
    aaTooltip = (AATooltip()
    .enabledSet(True)
    .pointFormatSet("<b>{point.name</b>的人口数量是：<b>{point.value</b>"))
    
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
        .dataSet(AAOptionsData.sunburstData)
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
        .typeSet(AAChartType.Dependencywheel)
        .nameSet("Dependency wheel series")
        .keysSet(["from","to","weight"])
        .dataSet(AAOptionsData.dependencywheelData)
        .dataLabelsSet(AADataLabels()
                       .enabledSet(True)
                       .colorSet("#333")
                       # .textPathSet(AATextPath()
                       #              .enabledSet(True)
                       #              .attributesSet({ "dy": 5 ))
                       .distanceSet(10))
               ]))


# # https:#jshare.com.cn/demos/hhhhiz
  @staticmethod
  def heatmapChart():
    return (AAOptions()
    .chartSet(AAChart()
              .typeSet(AAChartType.Heatmap))
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
               .alignSet(AAChartAlignType.Right)
               .layoutSet(AAChartLayoutType.Vertical)
               .verticalAlignSet(AAChartVerticalAlignType.Top)
               .ySet(25))
    .tooltipSet(AATooltip()
                .enabledSet(True)
                .formatterSet("""
        AAJSFunc(function ()():
                    return '<b>' + this.series.xAxis.categories[this.point.x] + '</b> sold <br><b>' +
                        this.point.value + '</b> items on <br><b>' + this.series.yAxis.categories[this.point.y] + '</b>'
                ))
                """)
    .seriesSet([
        AASeriesElement()
        .nameSet("Sales")
        .borderWidthSet(1)
        .dataSet(AAOptionsData.heatmapData)
        .dataLabelsSet(AADataLabels()
                       .enabledSet(True)
                       .colorSet(AAColor.red))
               ]))



# # https:#www.highcharts.com.cn/demo/highcharts/packed-bubble
  @staticmethod
  def packedbubbleChart():
    return (AAOptions()
    .chartSet(AAChart()
              .typeSet(AAChartType.Packedbubble))
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
                                                         .gravitationalConstantSet(0.02)
                                                         .splitSeriesSet(False))
                                     .dataLabelsSet(AADataLabels()
                                                    .enabledSet(True)
                                                    .formatSet("{point.name")
                                                    # .filterSet(AAFilter()
                                                    #            .propertySet("y")
                                                    #            .operatorSet(">")
                                                    #            .valueSet(250))
                                                    )))
    .seriesSet(AAOptionsSeries.packedbubbleSeries))


# https:#www.highcharts.com.cn/demo/highcharts/packed-bubble-split
  @staticmethod
  def packedbubbleSplitChart():
    return (AAOptions()
    .chartSet(AAChart()
              .typeSet(AAChartType.Packedbubble))
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
                                                    .formatSet("{point.name")
                                                    # .filterSet(AAFilter()
                                                    #            .propertySet("y")
                                                    #            .operatorSet(">")
                                                    #            .valueSet(250))
                                                    )))
    .seriesSet(AAOptionsSeries.packedbubbleSeries))



  @staticmethod
  def vennChart():
    return (AAOptions()
    .titleSet(AATitle()
              .textSet("The Unattainable Triangle"))
    .seriesSet([
        AASeriesElement()
        .typeSet(AAChartType.Venn)
        .dataSet(AAOptionsData.vennData)]))


  @staticmethod
  def dumbbellChart():
    aaChart = (AAChart()
    .typeSet(AAChartType.Dumbbell)
    .invertedSet(True))
    
    aaTitle = (AATitle()
    .textSet("各国预期寿命变化"))
    
    aaSubtitle = (AASubtitle()
    .textSet("1960 vs 2018"))
    
    aaXAxis = (AAXAxis()
    .visibleSet(True)
    .typeSet(AAChartAxisTypeCategory))
    
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
        .dataSet(AAOptionsData.dumbbellData)
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
    .typeSet(AAChartType.Lollipop))
    
    aaTitle = (AATitle()
    .textSet("世界十大人口国家"))
    
    aaSubtitle = (AASubtitle()
    .textSet("2018"))
    
    aaXAxis = (AAXAxis()
    .visibleSet(True)
    .typeSet(AAChartAxisTypeCategory))
    
    aaYAxis = (AAYAxis()
    .visibleSet(True)
    .titleSet(AAAxisTitle()
              .textSet("人口")))
    
    aaTooltip = (AATooltip()
    .enabledSet(True))
    
    aaLegend = (AALegend()
    .enabledSet(False))
    
    seriesElementArr = [
        AASeriesElement()
        .nameSet("Population")
        .dataSet(AAOptionsData.lollipopData)
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
              .typeSet(AAChartType.Streamgraph))
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
              .typeSet("category")
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
    .seriesSet(AAOptionsSeries.streamgraphSeries))


  @staticmethod
  def columnpyramidChart():
    return (AAOptions()
    .chartSet(AAChart()
              .typeSet(AAChartType.Columnpyramid))
    .titleSet(AATitle()
              .textSet("世界 5 大金字塔"))
    .xAxisSet(AAXAxis()
              .visibleSet(True)
              .typeSet(AAChartAxisTypeCategory))
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
        .dataSet(AAOptionsData.columnpyramidData)
               ]))


  @staticmethod
  def tilemapChart():
    return (AAOptions()
    .chartSet(AAChart()
              .typeSet(AAChartType.Tilemap))
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
                .valueSuffixSet("The population of <b>():point.name</b> is <b>{point.value</b>"))
    .plotOptionsSet(AAPlotOptions()
                    .seriesSet(AASeries()
                               .dataLabelsSet(AADataLabels()
                                              .enabledSet(True)
                                              .formatSet("{point.hc-a2")
                                              .colorSet(AAColor.white)
                                              .styleSet(AAStyle()
                                                        .textOutlineSet("none")))))
    .seriesSet([
        AASeriesElement()
        .nameSet("Height")
        .colorByPointSet(True)
        .dataSet(AAOptionsData.tilemapData)
               ]))


  @staticmethod
  def treemapWithColorAxisData():
    return (AAOptions()
    .chartSet(AAChart()
              .typeSet(AAChartType.Treemap))
    .titleSet(AATitle()
              .textSet("矩形树图"))
    .colorAxisSet(AAColorAxis()
                  .minColorSet(AAColor.white)
                  .maxColorSet(AAColor.red))
    .seriesSet([
        AASeriesElement()
        .dataSet(AAOptionsData.treemapWithColorAxisData)
               ]))


  @staticmethod
  def drilldownTreemapChart():
    return (AAOptions()
    .chartSet(AAChart()
              .typeSet(AAChartType.Treemap))
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
        .typeSet(AAChartType.Treemap)
        .levelsSet([
            AALevelsElement()
            .levelSet(1)
            .dataLabelsSet(AADataLabels()
                           .enabledSet(True))
            .borderWidthSet(3)
                   ])
        .dataSet(AAOptionsData.drilldownTreemapData)
               ]))


  @staticmethod
  def xrangeChart():
    return (AAOptions()
    .chartSet(AAChart()
              .typeSet(AAChartType.Xrange))
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
        .dataSet(AAOptionsData.xrangeData)
               ]))


  @staticmethod
  def vectorChart():
    return (AAOptions()
    .chartSet(AAChart()
              .typeSet(AAChartType.Vector))
    .colorsSet(["red"])
    .titleSet(AATitle()
              .textSet("AAChartKit-Pro Vector plot"))
    .seriesSet([
        AASeriesElement()
        .nameSet("Sample vector field")
        .dataSet(AAOptionsData.vectorData)
               ]))


  @staticmethod
  def bellcurveChart():
    return (AAOptions()
    .titleSet(AATitle()
              .textSet("Bell curve"))
    .xAxisSet((id)[
        AATitle()
        .textSet("Data"),
        AATitle()
        .textSet("Bell curve")
                  ])
    .yAxisSet((id)[
        AATitle()
        .textSet("Data"),
        AATitle()
        .textSet("Bell curve")
                  ])
    .seriesSet([
        AASeriesElement()
        .nameSet("Bell curve")
        .typeSet(AAChartType.Bellcurve)
        .xAxisSet(1)
        .yAxisSet(1)
        .baseSeriesSet(1)
        .zIndexSet(-1)
        ,
        AASeriesElement()
        .nameSet("Data")
        .typeSet(AAChartType.Scatter)
        .markerSet(AAMarker()
                   .fillColorSet(AAColor.white)#点的填充色(用来设置折线连接点的填充色)
                   .lineWidthSet(2)#外沿线的宽度(用来设置折线连接点的轮廓描边的宽度)
                   .lineColorSet(""))#外沿线的颜色(用来设置折线连接点的轮廓描边颜色，当值为空字符串时，默认取数据点或数据列的颜色))
        .dataSet(AAOptionsData.bellcurveData)
               ]))


  @staticmethod
  def timelineChart():
    return (AAOptions()
    .chartSet(AAChart()
              .typeSet(AAChartType.Timeline))
    .titleSet(AATitle()
              .textSet("人类太空探索时间表"))
    .subtitleSet(AASubtitle()
                 .textSet("数据来源: https:#en.wikipedia.org/wiki/Timeline_of_space_exploration"))
    .yAxisSet(AAYAxis()
              .visibleSet(False))
    .seriesSet([
        AASeriesElement()
        .dataSet(AAOptionsData.timelineData)
               ]))


  @staticmethod
  def itemChart():
    return (AAOptions()
    .chartSet(AAChart()
              .typeSet(AAChartType.Item))
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
        .dataSet(AAOptionsData.itemData)
        .dataLabelsSet(AADataLabels()
                       .enabledSet(False))
        .sizeSet((id)"170%")
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
        .typeSet(AAChartType.Windbarb)
        .nameSet("Wind")
        .dataSet(AAOptionsData.windbarbData),
        AASeriesElement()
        .typeSet(AAChartType.Area)
        .nameSet("Wind speed")
        .dataSet(AAOptionsData.windbarbData)
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
              .typeSet(AAChartType.Networkgraph))
    .titleSet(AATitle()
              .textSet("The Indo-European Laungauge Tree"))
    .subtitleSet(AASubtitle()
                 .textSet("A Force-Directed Network Graph in Highcharts"))
    .seriesSet([
        AASeriesElement()
        .dataLabelsSet(AADataLabels()
                       .enabledSet(False))
        .dataSet(AAOptionsData.networkgraphData),
               ]))


  @staticmethod
  def wordcloudChart():
    return (AAOptions()
    .chartSet(AAChart()
              .typeSet(AAChartType.Wordcloud))
    .titleSet(AATitle()
              .textSet("词云图"))
    .seriesSet([
        AASeriesElement()
        .dataSet(AAOptionsData.wordcloudData),
               ]))


  @staticmethod
  def eulerChart():
    return (AAOptions()
    .chartSet(AAChart()
              .typeSet(AAChartType.Venn))
    .titleSet(AATitle()
              .textSet("欧拉图和韦恩图的关系"))
    .tooltipSet(AATooltip()
                .enabledSet(True)
                # .headerFormatSet([NSString stringWithFormat:"%%",
                #                   "<span style=""color:{point.color"">\u2022</span>",
                #                   "<span style=""font-size: 14px"">():point.point.name</span><br/>"])
                .pointFormatSet("{point.description<br><span style=""font-size: 10px"">Source: Wikipedia</span>"))
    .seriesSet([
        AASeriesElement()
        .dataSet(AAOptionsData.eulerData),
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
                .typeSet(AAChartType.Organization)
                .nameSet("Highsoft")
                .keysSet(["from", "to"])
                .dataSet(AAOptionsData.organizationData)
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
                .nodesSet(AAOptionsData.organizationNodesData)
                .colorByPointSet(False)
                .colorSet("#007ad0")
                .dataLabelsSet(AADataLabels()
                    .colorSet(AAColor.white))
                .borderColorSet(AAColor.white)
                .nodeWidthSet(65)
            ])
        .tooltipSet(AATooltip()
            .outsideSet(True)))


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
                .typeSet(AAChartType.Arcdiagram)
                .nameSet("Train connections")
                .linkWeightSet(1)
                .centeredLinksSet(True)
                .dataLabelsSet(AADataLabels()
                    .rotationSet(90)
                    .ySet(30)
                    .alignSet(AAChartAlignType.Left)
                    .colorSet(AAColor.black))
                .offsetSet("65%")
                .dataSet(AAOptionsData.arcdiagram1Data)
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
                .typeSet(AAChartType.Arcdiagram)
                .markerSet(AAMarker()
                    .symbolSet(AAChartSymbolType.Triangle)
                    .lineWidthSet(2)
                    .lineColorSet(AAColor.white))
                .centeredLinksSet(True)
                .dataLabelsSet(AADataLabels()
                    .formatSet("{point.fromNode.name →():point.toNode.name")
                    .nodeFormatSet("{point.name")
                    .colorSet(AAColor.black)
                    # .linkTextPathSet(AATextPath()
                    #     .enabledSet(True))
            )
                .dataSet(AAOptionsData.arcdiagram2Data)
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
                .typeSet(AAChartType.Arcdiagram)
                .dataLabelsSet(AADataLabels()
                    .alignSet(AAChartAlignType.Right)
                    .xSet(-20)
                    .ySet(-2)
                    .colorSet("#333333")
                    .overflowSet("allow")
                    .paddingSet(0)
            )
                .offsetSet("60%")
                .dataSet(AAOptionsData.arcdiagram3Data)
            ]))


  @staticmethod
  def flameChart():
    return (AAOptions()
        .chartSet(AAChart()
            .invertedSet(True))
        .titleSet(AATitle()
            .alignSet(AAChartAlignType.Left)
            .textSet("Flame chart (layout: flame)"))
        .subtitleSet(AASubtitle()
            .alignSet(AAChartAlignType.Left)
            .textSet("Highcharts chart rendering process"))
        .legendSet(AALegend()
            .enabledSet(False))
        .xAxisSet((id)[
            AAXAxis()
                .visibleSet(False),
            AAXAxis()
                .visibleSet(False)
                .startOnTickSet(False)
                .endOnTickSet(False)
                .minPaddingSet(0)
                .maxPaddingSet(0)
            ])
        .yAxisSet((id)[
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
                .typeSet(AAChartType.Flame)
                .dataSet(AAOptionsData.flameData)
                .yAxisSet(1)
                .xAxisSet(1),
            AASeriesElement()
                .visibleSet(False)
                .sizeSet((id)"100%")
                .typeSet(AAChartType.Sunburst)
                .dataSet(AAOptionsData.sunburst2Data)
                .allowDrillToNodeSet(True)
                .cursorSet("pointer")
                .levelsSet([
                    AALevelsElement()
                        .levelSet(1)
#                        .levelIsConstantSet(False)
                        .dataLabelsSet(AADataLabels()
                            .enabledSet(False))
                    ])
                .dataLabelsSet(AADataLabels()
                    # .textPathSet(AATextPath()
                    #     .attributesSet({"dy": 5)
                    #     .enabledSet(True))
                               )
            ])
        .tooltipSet(AATooltip()
            .headerFormatSet("")
            .pointFormatSet("selfSize of():point.name is():point.value")))


  @staticmethod
  def packedbubbleSpiralChart():
    return (AAOptions()
        .chartSet(AAChart()
            .typeSet(AAChartType.Packedbubble)
#            .heightSet("100%")
                  )
        .titleSet(AATitle()
            .textSet("Carbon emissions around the world (2014)"))
        .tooltipSet(AATooltip()
            .useHTMLSet(True)
            .pointFormatSet("{point.name:():point.ym CO2"))
        .plotOptionsSet(AAPlotOptions()
            .packedbubbleSet(AAPackedbubble()
                .useSimulationSet(False)
                .minSizeSet("20%")
                .maxSizeSet("80%")
                .dataLabelsSet(AADataLabels()
                    .enabledSet(True)
                    .formatSet("{point.name")
                    .filterSet(AAFilter()
                        .propertySet("y")
                        .operatorSet(">")
                        .valueSet(250))
                    .styleSet(AAStyle()
                        .colorSet(AAColor.black)
                        .textOutlineSet("none")
                        .fontWeightSet("normal")))))
        .seriesSet(AAOptionsSeries.packedbubbleSeries))


