import json

from bin.plainObject.Product import Product
from bin.plainObject.ProductList import ProductList
from bin.plainObject.ProductCommerceDetail import ProductCommerceDetail
from bin.plainObject.Commerce import Commerce
from bin.database.SqlHelper import SqlHelper

class CommerceController:



    def getCommerceById(self, idCommerce):

        sqlHelper = SqlHelper()
        myresultPid = sqlHelper.select_commerce_by_id(idCommerce)

        for row in myresultPid:

            commerce = Commerce(row[0], row[1], row[2], row[3], row[4], row[5])

        return commerce
