import json

class ExcecutionDate:

    def __init__(self, excecutionDate):
        self.excecutionDate = excecutionDate

    @classmethod
    def fromJson(self, jsonExcecutionDate):
        self.excecutionDate = jsonProduct['excecutionDate']
        return self

    def toJson(self):
        arr = {}
        arr['excecutionDate'] = self.excecutionDate
        return json.dumps(arr)

    def toList(self):
        arr = {}
        arr['excecutionDate'] = self.excecutionDate
        return arr

    def toArray(self):
        arr = []
        arr.append(self.excecutionDate)
        return arr

    def print(self):
        attrs = vars(self)
        print(', '.join("%s: %s" % item for item in attrs.items()))