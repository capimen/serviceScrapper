import json

class Product:

    def __init__(self, id, name, referencePrice, idCategory, imgUrl, status):
        self.id = id
        self.name = name
        self.referencePrice = referencePrice
        self.idCategory = idCategory
        self.imgUrl = imgUrl
        self.status = status

    @classmethod
    def fromJson(self, jsonProduct):
        self.id = jsonProduct['id']
        self.name = jsonProduct['name']
        self.referencePrice = jsonProduct['referencePrice']
        self.idCategory = jsonProduct['idCategory']
        self.imgUrl = jsonProduct['imgUrl']
        self.status = jsonProduct['status']
        return self

    def toJson(self):
        arr = {}
        arr['id'] = self.id
        arr['name'] = self.name
        arr['referencePrice'] = self.referencePrice
        arr['idCategory'] = self.idCategory
        arr['imgUrl'] = self.imgUrl
        arr['status'] = self.status
        return json.dumps(arr)

    def toList(self):
        arr = {}
        arr['id'] = self.id
        arr['name']= self.name
        arr['referencePrice'] = self.referencePrice
        arr['idCategory'] = self.idCategory
        arr['imgUrl'] = self.imgUrl
        arr['status'] = self.status
        return arr

    def toArray(self):
        arr = []
        arr.append(self.id)
        arr.append(self.name)
        arr.append(self.referencePrice)
        arr.append(self.idCategory)
        arr.append(self.imgUrl)
        arr.append(self.status)
        return arr


    def print(self):
        attrs = vars(self)
        print(', '.join("%s: %s" % item for item in attrs.items()))

