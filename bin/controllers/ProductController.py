import json

from bin.plainObject.Product import Product
from bin.plainObject.ProductList import ProductList
from bin.controllers.ComparatorController import ComparatorController
from bin.database.SqlHelper import SqlHelper

class ProductController:


    def getProductById(self, idProduct):
        sqlHelper = SqlHelper()
        myresultPid = sqlHelper.select_product_by_id(idProduct)

        for row in myresultPid:

            product = Product(row[0], row[1], row[2], row[3], row[4], row[5], row[6])

        return product


    def getAllProducts(self, orderBy):

        sqlHelper = SqlHelper()
        myresultPid = sqlHelper.select_product(orderBy)
        productList = ProductList()

        for row in myresultPid:
            product = Product(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            productList.addProduct(product)

        return productList


    def createProduct(self, jsonProduct):

        id = jsonProduct['id']
        name = jsonProduct['name']
        referencePrice = jsonProduct['referencePrice']
        idCategory = jsonProduct['idCategory']
        imgUrl = jsonProduct['imgUrl']
        status = jsonProduct['status']
        idCommerce = jsonProduct['idCommerce']
        priority = jsonProduct['priority']
        product = Product(id, name, referencePrice, idCategory, imgUrl, status, priority)

        sqlHelper = SqlHelper()
        sqlHelper.insert_product(product)


    def updateProduct(self, jsonProduct):
        product = Product.fromJson(jsonProduct)
        sqlHelper = SqlHelper()
        sqlHelper.update_product(product)

        #esto es para cambiar el null de la base de datos a null del codigo
        if product.imgUrl == 'null':

            product.imgUrl = None

        return product


    def deleteProduct(self, productId):
        sqlHelper = SqlHelper()
        product = self.getProductById(productId)
        product.status = False
        sqlHelper.update_product(product)

        #delete from comparator
        comparatorController = ComparatorController()
        comparatorController.deleteComparator(productId)

        return not product.status