import json

from bin.plainObject.Commerce import Commerce
from bin.plainObject.CommerceList import CommerceList
from bin.database.SqlHelper import SqlHelper

class CommerceController:


    def getCommerceById(self, idCommerce):

        sqlHelper = SqlHelper()
        print(idCommerce)
        myresultPid = sqlHelper.select_commerce_by_id(idCommerce)

        for row in myresultPid:

            commerce = Commerce(row[0], row[1], row[2], row[3], row[4], row[5])

        return commerce


    def getAllCommerce(self):

        sqlHelper = SqlHelper()
        myresultPid = sqlHelper.select_commerce()
        commerceList = CommerceList()

        for row in myresultPid:

            commerce = Commerce(row[0], row[1], row[2], row[3], row[4], row[5])
            commerceList.addCommerce(commerce)

        return commerceList


    def createCommerce(self, jsonCommerce):

        id = jsonCommerce['id']
        name = jsonCommerce['name']
        priceclass = jsonCommerce['priceclass']
        pricetag = jsonCommerce['pricetag']
        nameclass = jsonCommerce['nameclass']
        nametag = jsonCommerce['nametag']
        commerce = Commerce(id, name, priceclass, pricetag, nameclass, nametag)

        sqlHelper = SqlHelper()
        sqlHelper.insert_commerce(commerce)



    def updateCommerce(self, jsonCommerce):

        commerce = Commerce.fromJson(jsonCommerce)
        sqlHelper = SqlHelper()
        sqlHelper.update_commerce(commerce)

        return commerce