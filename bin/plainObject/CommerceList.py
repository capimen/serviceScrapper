import json


class CommerceList:

    def __init__(self):
        self.CommerceList = []

    def addProduct(self, prod):
        self.CommerceList.append(prod)

    def toJson(self):

        arr = {}
        arrlist = []

        for item in self.CommerceList:

            arrlist.append(item.toList())

        arr['commerceList'] = arrlist
        return json.dumps(arr)

    def toList(self):
        arr = {}
        arrlist = []

        for item in self.CommerceList:

            arrlist.append(item.toList())

        arr['productList'] = arrlist
        return arr