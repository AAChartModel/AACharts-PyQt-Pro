class AAOptionsSeries:
    @staticmethod
    def packedbubbleSeries():
        return AAOptionsSeries.getJsonDataWithJsonFileName("variablepieData")

    @staticmethod
    def streamgraphSeries():
        return AAOptionsSeries.getJsonDataWithJsonFileName("variwideData")

    @staticmethod
    def getJsonDataWithJsonFileName(jsonFileName: str):
        return ""