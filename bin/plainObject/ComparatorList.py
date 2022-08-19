import json


class ComparatorList:

    def __init__(self):
        self.ComparatorList = []


    def addComparator(self, comparator):
        self.ComparatorList.append(comparator)


    def toJson(self):

        arr = {}
        arrlist = []

        for item in self.ComparatorList:

            arrlist.append(item.toList())

        arr['comparatorList'] = arrlist
        return json.dumps(arr)


    def toList(self):

        arr = {}
        arrlist = []

        for item in self.ComparatorList:

            arrlist.append(item.toList())

        arr['comparatorList'] = arrlist
        return arr