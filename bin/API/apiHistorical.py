from flask import jsonify
from bin.controllers.HistoricalController import HistoricalController


historicalController = HistoricalController()

def getAllHistorical():

    historicalList = historicalController.getAllHistorical()
    return jsonify(historicalList.toList())


def getHistoricalById(idProduct):

    if idProduct == None:

        return jsonify({'error': 'data not found'})

    historicalList = historicalController.getHistoricalByIdProduct(idProduct)
    return jsonify(historicalList.toList())


