import json

class Historical:

    def __init__(self, id, idProduct, idCommerce, idProductCommerceDetail, price, regDate):
        self.id = id
        self.idProduct = idProduct
        self.idCommerce = idCommerce
        self.idProductCommerceDetail = idProductCommerceDetail
        self.price = price
        self.regDate = regDate


    @classmethod
    def fromJson(self, jsonHistorical):
        self.id = jsonHistorical['id']
        self.idProduct = jsonHistorical['idProduct']
        self.idCommerce = jsonHistorical['idCommerce']
        self.idProductCommerceDetail = jsonHistorical['idProductCommerceDetail']
        self.price = jsonHistorical['price']
        self.regDate = jsonHistorical['regDate']
        return self

    def toJson(self):
        arr = {}
        arr['id'] = self.id
        arr['idProduct'] = self.idProduct
        arr['idCommerce'] = self.idCommerce
        arr['idProductCommerceDetail'] = self.idProductCommerceDetail
        arr['price'] = self.price
        arr['regDate'] = self.regDate
        return json.dumps(arr)

    def toList(self):
        arr = {}
        arr['id'] = self.id
        arr['idProduct'] = self.idProduct
        arr['idCommerce'] = self.idCommerce
        arr['idProductCommerceDetail'] = self.idProductCommerceDetail
        arr['price'] = self.price
        arr['regDate'] = self.regDate
        return arr

    def toArray(self):
        arr = []
        arr.append(self.id)
        arr.append(self.idProduct)
        arr.append(self.idCommerce)
        arr.append(self.idProductCommerceDetail)
        arr.append(self.price)
        arr.append(self.regDate)
        return arr


    def print(self):
        attrs = vars(self)
        print(', '.join("%s: %s" % item for item in attrs.items()))

