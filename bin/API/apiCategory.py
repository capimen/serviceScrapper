from flask import jsonify
from bin.controllers.CategoryController import CategoryController

categoryController = CategoryController()
#TODO crear la logica de category

def getAllCategory():

    categoryList = categoryController.getAllCategories()
    return jsonify(categoryList.toList())


def getCategoryById(idCategory):

    if idCategory == None:

        return jsonify({'error': 'data not found'})

    category = categoryController.getCategoryById(idCategory)
    return jsonify(category.toList())


def createCategory(jsonCategory):

    category = categoryController.createCategory(jsonCategory)
    return jsonify(category.toList())


def updateCategory(jsonCommerce):

    category = categoryController.updateCategory(jsonCommerce)
    return jsonify(category.toList(category))