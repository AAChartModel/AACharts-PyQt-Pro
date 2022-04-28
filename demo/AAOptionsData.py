import json
import random


class AAOptionsData:
    @staticmethod
    def variablepieData():
        return AAOptionsData.getJsonDataWithJsonFileName("variablepieData")

    @staticmethod
    def variwideData():
        return AAOptionsData.getJsonDataWithJsonFileName("variwideData")

    @staticmethod
    def heatmapData():
        return AAOptionsData.getJsonDataWithJsonFileName("heatmapData")

    @staticmethod
    def columnpyramidData():
        return AAOptionsData.getJsonDataWithJsonFileName("columnpyramidData")

    @staticmethod
    def treemapWithColorAxisData():
        return AAOptionsData.getJsonDataWithJsonFileName("treemapWithColorAxisData")

    @staticmethod
    def drilldownTreemapData():
        return AAOptionsData.getJsonDataWithJsonFileName("drilldownTreemapData")

    @staticmethod
    def sankeyData():
        return AAOptionsData.getJsonDataWithJsonFileName("sankeyData")

    @staticmethod
    def dependencywheelData():
        return AAOptionsData.getJsonDataWithJsonFileName("dependencywheelData")

    @staticmethod
    def sunburstData():
        return AAOptionsData.getJsonDataWithJsonFileName("sunburstData")

    @staticmethod
    def dumbbellData():
        return AAOptionsData.getJsonDataWithJsonFileName("dumbbellData")

    @staticmethod
    def vennData():
        return AAOptionsData.getJsonDataWithJsonFileName("vennData")

    @staticmethod
    def lollipopData():
        return AAOptionsData.getJsonDataWithJsonFileName("lollipopData")

    @staticmethod
    def tilemapData():
        return AAOptionsData.getJsonDataWithJsonFileName("tilemapData")

    @staticmethod
    def treemapWithLevelsData():
        return AAOptionsData.getJsonDataWithJsonFileName("treemapWithLevelsData")

    @staticmethod
    def bellcurveData():
        return AAOptionsData.getJsonDataWithJsonFileName("bellcurveData")

    @staticmethod
    def timelineData():
        return AAOptionsData.getJsonDataWithJsonFileName("timelineData")

    @staticmethod
    def itemData():
        return AAOptionsData.getJsonDataWithJsonFileName("itemData")

    @staticmethod
    def windbarbData():
        return AAOptionsData.getJsonDataWithJsonFileName("windbarbData")

    @staticmethod
    def networkgraphData():
        return AAOptionsData.getJsonDataWithJsonFileName("networkgraphData")

    @staticmethod
    def wordcloudData():
        return AAOptionsData.getJsonDataWithJsonFileName("wordcloudData")

    @staticmethod
    def eulerData():
        return AAOptionsData.getJsonDataWithJsonFileName("eulerData")

    @staticmethod
    def organizationData():
        return AAOptionsData.getJsonDataWithJsonFileName("organizationData")

    @staticmethod
    def organizationNodesData():
        return AAOptionsData.getJsonDataWithJsonFileName("organizationNodesData")

    @staticmethod
    def arcdiagram1Data():
        return AAOptionsData.getJsonDataWithJsonFileName("arcdiagram1Data")

    @staticmethod
    def arcdiagram2Data():
        return AAOptionsData.getJsonDataWithJsonFileName("arcdiagram2Data")

    @staticmethod
    def arcdiagram3Data():
        return AAOptionsData.getJsonDataWithJsonFileName("arcdiagram3Data")

    @staticmethod
    def flameData():
        return AAOptionsData.getJsonDataWithJsonFileName("flameData")

    @staticmethod
    def sunburst2Data():
        return AAOptionsData.getJsonDataWithJsonFileName("sunburst2Data")

    #     public class var xrangeData: [Any] {
    #     func getSingleGroupCategoryDataElementArrayWithY(_ y: Int) -> [Any] {
    #         var dataArr = [Any]()
            
    #         var x = 0
    #         var x2 = x + Int(arc4random()) % 10
    #         for _ in 0 ..< 50 {
    #             var dataElementDic = [String:Any]()
    #             dataElementDic["x"] = x
    #             dataElementDic["x2"] = x2
    #             dataElementDic["y"] = y
    #             dataArr.append(dataElementDic)
    #             x = x2 + Int(arc4random()) % 1000
    #             x2 = x + Int(arc4random()) % 2000
    #         }
    #         return dataArr
    #     }
        
    #     var dataArr = [Any]()
    #     for y in 0 ..< 20 {
    #         let data = getSingleGroupCategoryDataElementArrayWithY(y)
    #         for dataElement in data {
    #             dataArr.append(dataElement)
    #         }
    #     }
    #     return dataArr
    # }

    @staticmethod
    def getSingleGroupCategoryDataElementArrayWithY(y: int):
        dataArr = list()
        x = 0
        x2 = x + random.randint(0, 9)

        for num in range(0, 50):
            dataElementDic = dict()
            dataElementDic["x"] = x
            dataElementDic["x2"] = x2
            dataElementDic["y"] = y
            dataArr.append(dataElementDic)
            x = x2 + random.randint(0, 1000) 
            x2 = x + random.randint(0, 2000)  
        
        return dataArr


    @staticmethod
    def xrangeData():
        dataArr = list()
        for y in range(0, 20):
            data = AAOptionsData.getSingleGroupCategoryDataElementArrayWithY(y)
            for dataElement in data:
                dataArr.append(dataElement)

        return dataArr


    @staticmethod
    def vectorData():
        return AAOptionsData.getJsonDataWithJsonFileName("vectorData")


    # to do
    # https://blog.csdn.net/m0_37693335/article/details/81474995
    # python 相对路径打开文件夹
    @staticmethod
    def getJsonDataWithJsonFileName(jsonFileName: str):
        # /Users/admin/Documents/GitHub/AACharts-PyQt-Pro/demo/datajson/arcdiagram1Data.json
        print("正在读取文件" + jsonFileName + "😊")
        filePath = "/Users/admin/Documents/GitHub/AACharts-PyQt-Pro/demo/datajson/" + jsonFileName + ".json"
        # 打开一个json文件
        data = open(filePath, encoding='utf-8')
        # 转换为python对象
        strJson = json.load(data)
        return strJson