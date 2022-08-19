import json


class CategoryList:

    def __init__(self):
        self.CategoryList = []


    def addCategory(self, category):
        self.CategoryList.append(category)


    def toJson(self):

        arr = {}
        arrlist = []

        for item in self.CategoryList:

            arrlist.append(item.toList())

        arr['categoryList'] = arrlist
        return json.dumps(arr)


    def toList(self):

        arr = {}
        arrlist = []

        for item in self.CategoryList:

            arrlist.append(item.toList())

        arr['categoryList'] = arrlist
        return arr