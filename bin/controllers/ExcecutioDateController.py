import json

from bin.database.SqlHelper import SqlHelper
from bin.plainObject.ExcecutionDate import ExcecutionDate

class ExcecutionDateController:

    def getLastExcecution(self):
        sqlHelper = SqlHelper()
        myresultPid = sqlHelper.select_newest_excecution()

        for row in myresultPid:

            lastExcecution = ExcecutionDate(row[0])

        return lastExcecution