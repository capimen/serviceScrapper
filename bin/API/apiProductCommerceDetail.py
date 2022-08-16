from flask import jsonify
from bin.controllers.ProductCommerceDetailController import ProductCommerceDetailController


def getPCDByIdProduct(idProduct):

    if idProduct == None:

        return jsonify({'error': 'data not found'})

    productController = ProductController()
    product = productController.getProductById(idProduct)
    return jsonify(product.toList())


def getPCDByIdCommerce(idProduct):

    if idProduct == None:

        return jsonify({'error': 'data not found'})

    productController = ProductController()
    product = productController.getProductById(idProduct)
    return jsonify(product.toList())