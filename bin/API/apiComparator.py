from flask import jsonify
from bin.controllers.ComparatorController import ComparatorController
from bin.plainObject.PublishedURL import PublishedURL


comparatorController = ComparatorController()


def getAllComparator(orderBy):
    comparatorList = comparatorController.getAllComparator(orderBy)
    publishedURL = PublishedURL()
    listURL = publishedURL.toList()
    listComparator = comparatorList.toList()
    print(listURL)
    joinedList = listURL.update(listComparator)
    #print(joinedList)

    return jsonify(listURL)
    #return jsonify(resp)

def getComparatorById(idProduct):

    if idProduct == None:

        return jsonify({'error': 'data not found'})

    comparator = comparatorController.getComparatorById(idProduct)
    return jsonify(comparator.toList())


def getComparatorCount():

    count = comparatorController.getComparatorCount()
    return jsonify({'total_comparators': int(count)})

