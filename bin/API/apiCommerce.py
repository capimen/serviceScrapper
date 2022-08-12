from flask import jsonify
from bin.controllers.CommerceController import CommerceController

commerceController = CommerceController()

def getAllCommerce():

    commerceList = commerceController.getAllCommerce()
    return jsonify(commerceList.toList())


def getCommerceById(idCommerce):

    if idCommerce == None:

        return jsonify({'error': 'data not found'})

    commerce = commerceController.getCommeceById(idCommerce)
    return jsonify(commerce.toList())


def createCommerce(jsonCommerce):

    commerce = commerceController.createCommerce(jsonCommerce)
    return jsonify(commerce.toList())

def updateCommerce(jsonCommerce):

    commerce = commerceController.updateCommerce(jsonCommerce)
    return jsonify(commerce.toList(commerce))