import json


class CommerceList:

    def __init__(self):
        self.CommerceList = []

    def addCommerce(self, commerce):
        self.CommerceList.append(commerce)

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

        arr['commerceList'] = arrlist
        return arr