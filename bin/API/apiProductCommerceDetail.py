from flask import jsonify
from bin.controllers.ProductCommerceDetailController import ProductCommerceDetailController

productCommerceDetailController = ProductCommerceDetailController()


def getPCDByIdProduct(idProduct):

    if idProduct == None:

        return jsonify({'error': 'data not found'})


    productCommerceDetail = productCommerceDetailController.getPCDByIdProduct(idProduct)
    return jsonify(productCommerceDetail.toList())


def getPCDByIdCommerce(idCommerce):

    if idCommerce == None:

        return jsonify({'error': 'data not found'})

    productCommerceDetail = productCommerceDetailController.getPCDByIdCommerce(idCommerce)
    return jsonify(productCommerceDetail.toList())


def createProductCommerceDetail(pdcJson):

    productCommerceDetail = productCommerceDetailController.createProductCommerceDetail(pdcJson)
    return jsonify(productCommerceDetail.toList())