import json

from bin.plainObject.Category import Category
from bin.plainObject.CategoryList import CategoryList
from bin.database.SqlHelper import SqlHelper

class CategoryController:


    def getCategoryById(self, idCategory):

        sqlHelper = SqlHelper()
        myresultPid = sqlHelper.select_category_by_id(idCategory)

        for row in myresultPid:

            #id, name, discount, idGroup
            category = Category(row[0], row[1], row[2], row[3])

        return category


    def getAllCategories(self):

        sqlHelper = SqlHelper()
        myresultPid = sqlHelper.select_categories()
        categoryList = CategoryList()

        for row in myresultPid:

            category = Category(row[0], row[1], row[2], row[3])
            categoryList.addCategory(category)

        return categoryList


    def createCategory(self, jsonCategory):

        id = jsonCategory['id']
        name = jsonCategory['name']
        discount = jsonCategory['discount']
        idGroup = jsonCategory['idGroup']

        category = Category(id, name, discount, idGroup)

        sqlHelper = SqlHelper()
        sqlHelper.insert_category(category)


    def updateCategory(self, jsonCategory):

        category = Category.fromJson(jsonCategory)
        sqlHelper = SqlHelper()
        sqlHelper.update_category(category)

        return category