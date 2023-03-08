from flask import jsonify
from bin.controllers.ProductController import ProductController

def getAllProduct(orderBy):
    productController = ProductController()
    productList = productController.getAllProducts(orderBy)
    return jsonify(productList.toList())



def getProductById(idProduct):

    if idProduct == None:

        return jsonify({'error': 'data not found'})

    productController = ProductController()
    product = productController.getProductById(idProduct)
    return jsonify(product.toList())


def createProduct(jsonProduct):

    productController = ProductController()
    product = productController.createProduct(jsonProduct)
    return jsonify(product.toList())

def updateProduct(jsonProduct):

    productController = ProductController()
    product = productController.updateProduct(jsonProduct)
    return jsonify(product.toList(product))

def deleteProduct(idProduct):

    if idProduct == None:

        return jsonify({'error': 'data not found'})

    productController = ProductController()
    status = productController.deleteProduct(idProduct)
    return status