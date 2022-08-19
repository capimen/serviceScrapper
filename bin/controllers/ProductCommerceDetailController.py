import json

from bin.plainObject.ProductCommerceDetail import ProductCommerceDetail
from bin.database.SqlHelper import SqlHelper

class ProductCommerceDetailController:


    def getPCDByIdProduct(self, idProduct):

        sqlHelper = SqlHelper()
        myresultPid = sqlHelper.select_product_commerce_detail_by_idProduct(idProduct)

        for row in myresultPid:

            productCommerceDetail = ProductCommerceDetail(row[0], row[1], row[2], row[3])

        return productCommerceDetail


    def getPCDByIdCommerce(self, idCommerce):

        sqlHelper = SqlHelper()
        myresultPid = sqlHelper.select_product_commerce_detail_by_idCommerce(idCommerce)

        for row in myresultPid:

            productCommerceDetail = ProductCommerceDetail(row[0], row[1], row[2], row[3])

        return productCommerceDetail


    def createProductCommerceDetail(self, pdcJson):

        id = pdcJson['id']
        idProduct = pdcJson['idProduct']
        idCommerce = pdcJson['idCommerce']
        url = pdcJson['url']
        productCommerceDetail = ProductCommerceDetail(id, idProduct, idCommerce, url)

        sqlHelper = SqlHelper()
        sqlHelper.insert_product_commerce_detail(productCommerceDetail)
