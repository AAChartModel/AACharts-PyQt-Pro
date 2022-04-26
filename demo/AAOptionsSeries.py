class AAOptionsSeries:
    @staticmethod
    def variablepieData():
        return AAOptionsSeries.getJsonDataWithJsonFileName("variablepieData")

    @staticmethod
    def variwideData():
        return AAOptionsSeries.getJsonDataWithJsonFileName("variwideData")

    @staticmethod
    def getJsonDataWithJsonFileName(jsonFileName: str):
        return ""