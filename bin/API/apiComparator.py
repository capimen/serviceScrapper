from flask import jsonify
from bin.controllers.ComparatorController import ComparatorController


comparatorController = ComparatorController()


def getAllComparator():
    comparatorList = comparatorController.getAllComparator()
    return jsonify(comparatorList.toList())


def getComparatorById(idProduct):

    if idProduct == None:

        return jsonify({'error': 'data not found'})

    comparator = comparatorController.getComparatorById(idProduct)
    return jsonify(comparator.toList())


def getComparatorCount():

    count = comparatorController.getComparatorCount()
    return jsonify({'total_comparators': int(count)})

