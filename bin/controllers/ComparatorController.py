import json

from bin.plainObject.Comparator import Comparator
from bin.plainObject.ComparatorList import ComparatorList
from bin.database.SqlHelper import SqlHelper

class ComparatorController:


    def getAllComparator(self, orderBy):

        sqlHelper = SqlHelper()
        myresultPid = sqlHelper.select_comparator_all(orderBy)
        comparatorList = ComparatorList()

        for row in myresultPid:

            #id_product, product_name, price_newest, price_average, price_best,
            #price_worst, discount_priceleft, discount_percent, average_safe, average_safe_worst,
            #diff_best, url, best_historical_flag, umbral, umbral_flag, reg_date
            comparator = Comparator(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],
                                    row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17])
            comparatorList.addComparator(comparator)

        return comparatorList


    def getComparatorById(self, idProduct):

        sqlHelper = SqlHelper()
        myresultPid = sqlHelper.select_comparator_by_idProduct(idProduct)

        for row in myresultPid:

            comparator = Comparator(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],
                                    row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17])

        return comparator


    def getComparatorCount(self):
        sqlHelper = SqlHelper()
        myresultPid = sqlHelper.select_comparator_count()

        for row in myresultPid:
            count = row[0]

        return count


    def deleteComparator(self, idProduct):

        sqlHelper = SqlHelper()
        sqlHelper.delete_comparator_by_idProduct(idProduct)