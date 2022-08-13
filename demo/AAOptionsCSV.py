import json


class AAOptionsCSV:
    @staticmethod
    def csvData():
        return AAOptionsCSV.getJsonDataWithJsonFileName("bigHeatmapData")


    @staticmethod
    def getJsonDataWithJsonFileName(jsonFileName: map):
        # /Users/admin/Documents/GitHub/AACharts-PyQt-Pro/demo/datajson/arcdiagram1Data.json
        print("正在读取文件" + jsonFileName + "😊")
        filePath = "/Users/admin/Documents/GitHub/AACharts-PyQt-Pro/demo/datajson/" + jsonFileName + ".json"
        # 打开一个json文件
        data = open(filePath, encoding='utf-8')
        # 转换为python对象
        strJson = json.load(data)
        return strJson