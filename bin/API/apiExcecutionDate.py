from flask import jsonify
from bin.controllers.ExcecutioDateController import ExcecutionDateController

def getExcecutionDate():

    excecutionDateController = ExcecutionDateController()
    excutionDate = excecutionDateController.getLastExcecution()
    return jsonify(excutionDate.toList())