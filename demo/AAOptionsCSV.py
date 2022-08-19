import json
import os


class AAOptionsCSV:
    @staticmethod
    def csvData():
        return AAOptionsCSV.getJsonDataWithJsonFileName("bigHeatmapData")


    @staticmethod
    def getJsonDataWithJsonFileName(jsonFileName: map):
        # /Users/admin/Documents/GitHub/AACharts-PyQt-Pro/demo/datajson/arcdiagram1Data.json
        print("正在读取文件" + jsonFileName + "😊")
        # filePath = "/Users/admin/Documents/GitHub/AACharts-PyQt-Pro/demo/datajson/" + jsonFileName + ".json"

        cwd = os.getcwd()
        localJsonPath = cwd + "/demo/datajson/" + jsonFileName + ".json"
        print("本地文件路径" + localJsonPath)

        # 打开一个json文件
        data = open(localJsonPath, encoding='utf-8')
        # 转换为python对象
        strJson = json.load(data)
        return strJson