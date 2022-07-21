import json


class ProductList:

    def __init__(self):
        self.productList = []

    def addProduct(self, prod):
        self.productList.append(prod)

    def toJson(self):

        arr = {}
        arrlist = []

        for item in self.productList:

            arrlist.append(item.toList())

        arr['products'] = arrlist
        return json.dumps(arr)

    def toList(self):
        arr = {}
        arrlist = []

        for item in self.productList:

            arrlist.append(item.toList())

        arr['products'] = arrlist
        return arr