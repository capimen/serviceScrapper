import json

from bin.plainObject.Historical import Historical
from bin.plainObject.HistoricalList import HistoricalList
from bin.database.SqlHelper import SqlHelper

class HistoricalController:


    def getHistoricalByIdProduct(self, idProduct):

        sqlHelper = SqlHelper()
        myresultPid = sqlHelper.select_historical_by_idProduct(idProduct,"desc")
        historicalList = HistoricalList()

        for row in myresultPid:

            historical = Historical(row[0], row[1], row[2], row[3], row[4], row[5])
            historicalList.addHistorical(historical)

        return historicalList


    def getAllHistorical(self):

        sqlHelper = SqlHelper()
        myresultPid = sqlHelper.select_historical("asc")
        historicalList = HistoricalList()

        for row in myresultPid:

            historical = Historical(row[0], row[1], row[2], row[3], row[4], row[5])
            historicalList.addHistorical(historical)

        return historicalList
