import json


class AAOptionsSeries:
    @staticmethod
    def packedbubbleSeries():
        return AAOptionsSeries.getJsonDataWithJsonFileName("packedbubbleSeries")

    @staticmethod
    def streamgraphSeries():
        return AAOptionsSeries.getJsonDataWithJsonFileName("streamgraphSeries")

    @staticmethod
    def getJsonDataWithJsonFileName(jsonFileName: str):
        # /Users/admin/Documents/GitHub/AACharts-PyQt-Pro/demo/datajson/arcdiagram1Data.json
        print("正在读取文件" + jsonFileName + "😊")
        filePath = "/Users/admin/Documents/GitHub/AACharts-PyQt-Pro/demo/seriesjson/" + jsonFileName + ".json"
        # 打开一个json文件
        data = open(filePath, encoding='utf-8')
        # 转换为python对象
        strJson = json.load(data)
        return strJson