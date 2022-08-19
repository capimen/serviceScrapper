import json


class HistoricalList:

    def __init__(self):
        self.historicalList = []


    def addHistorical(self, prod):
        self.historicalList.append(prod)


    def toJson(self):

        arr = {}
        arrlist = []

        for item in self.historicalList:

            arrlist.append(item.toList())

        arr['historicalList'] = arrlist
        return json.dumps(arr)


    def toList(self):

        arr = {}
        arrlist = []

        for item in self.historicalList:

            arrlist.append(item.toList())

        arr['historicalList'] = arrlist
        return arr