import json

class ProductCommerceDetail:

    def __init__(self, id, idProduct, idCommerce, url):
        self.id = id
        self.idProduct = idProduct
        self.idCommerce = idCommerce
        self.url = url

    def fromJson(self, jsonProductCommerceDetail):
        self.id = jsonProductCommerceDetail['id']
        self.idProduct = jsonProductCommerceDetail['idProduct']
        self.idCommerce = jsonProductCommerceDetail['idCommerce']
        self.url = jsonProductCommerceDetail['url']
        return self

    def toJson(self):
        arr = {}
        arr['id'] = self.id
        arr['idProduct'] = self.idProduct
        arr['idCommerce'] = self.idCommerce
        arr['url'] = self.url
        return json.dumps(arr)

    def toList(self):
        arr = {}
        arr['id'] = self.id
        arr['idProduct'] = self.idProduct
        arr['idCommerce'] = self.idCommerce
        arr['url'] = self.url
        return arr

    def toArray(self):
        arr = []
        arr.append(self.id)
        arr.append(self.idProduct)
        arr.append(self.idCommerce)
        arr.append(self.url)
        return arr

    def print(self):
        attrs = vars(self)
        print(', '.join("%s: %s" % item for item in attrs.items()))