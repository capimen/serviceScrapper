import json

class Category:

    def __init__(self, id, name, discount, idGroup):
        self.id = id
        self.name = name
        self.discount = discount
        self.idGroup = idGroup

    @classmethod
    def fromJson(self, jsonCategory):
        self.id = jsonCategory['id']
        self.name = jsonCategory['name']
        self.discount = jsonCategory['discount']
        self.idGroup = jsonCategory['idGroup']
        return self

    def toJson(self):
        arr = {}
        arr['id'] = self.id
        arr['name'] = self.name
        arr['discount'] = self.discount
        arr['idGroup'] = self.idGroup
        return json.dumps(arr)

    def toList(self):
        arr = {}
        arr['id'] = self.id
        arr['name'] = self.name
        arr['discount'] = self.discount
        arr['idGroup'] = self.idGroup
        return arr

    def toArray(self):
        arr = []
        arr.append(self.id)
        arr.append(self.name)
        arr.append(self.discount)
        arr.append(self.idGroup)

    def print(self):
        attrs = vars(self)
        print(', '.join("%s: %s" % item for item in attrs.items()))