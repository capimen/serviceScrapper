import json

class PublishedURL:

    def __init__(self):
        self.text = 'clase para exponer las URL publicas'
        self.getComparatorAll = 'http://127.0.0.1:5000/comparator/'
        self.getComparatorCount = 'http://127.0.0.1:5000/comparator/count'



    def toJson(self):

        urlarr = {}
        comparatorURL = {}
        comparatorURL['getComparatorAll']  =  self.getComparatorAll
        comparatorURL['getComparatorCount'] = self.getComparatorCount
        urlarr['comparator'] = comparatorURL
        return json.dumps(urlarr)

    def toList(self):
        urlarr = {}
        comparatorURL = {}
        comparatorURL['getComparatorAll'] = self.getComparatorAll
        comparatorURL['getComparatorCount'] = self.getComparatorCount
        urlarr['comparator'] = comparatorURL
        return urlarr

    def toArray(self):
        #por construir
        arr = []
        arr.append(self.getComparatorAll)

    def print(self):
        attrs = vars(self)
        print(', '.join("%s: %s" % item for item in attrs.items()))