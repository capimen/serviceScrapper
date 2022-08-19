#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, request

from bin.API import apiProduct
from bin.API import apiCommerce
from bin.API import apiCategory
from bin.API import apiProductCommerceDetail
from bin.API import apiHistorical
from bin.API import apiComparator
app = Flask(__name__)


# PRODUCT
@app.route('/product/<id>', methods=['GET'])
def get_product(id):
    return apiProduct.getProductById(id)

@app.route('/product/', methods=['GET'])
def get_allProducts():

    return apiProduct.getAllProduct()

@app.route('/product/', methods=['POST'])
def create_product():

    productJson = json.loads(request.data)
    return apiProduct.createProduct(productJson)

@app.route('/product/', methods=['PUT'])
def update_product():

    productJson = json.loads(request.data)
    return apiProduct.updateProduct(productJson)

@app.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
    status = apiProduct.deleteProduct(id)
    resp = False
    httpStatus = 401
    if status == True:
        resp = True
        httpStatus = 200
    return resp, httpStatus


# COMMERCE
@app.route('/commerce/<id>', methods=['GET'])
def get_commerce(id):
    return apiCommerce.getCommerceById(id)

@app.route('/commerce/', methods=['GET'])
def get_allCommerce():

    return apiCommerce.getAllCommerce()

@app.route('/commerce/', methods=['POST'])
def create_commerce():

    commerceJson = json.loads(request.data)
    return apiCommerce.createCommerce(commerceJson)

@app.route('/commerce/', methods=['PUT'])
def update_commerce():

    commerceJson = json.loads(request.data)
    return apiCommerce.updateCommerce(commerceJson)



# CATEGORY
@app.route('/category/<id>', methods=['GET'])
def get_category(id):
    return apiCategory.getCategoryById(id)

@app.route('/category/', methods=['GET'])
def get_allCategory():

    return apiCategory.getAllCategory()

@app.route('/category/', methods=['POST'])
def create_category():

    categoryJson = json.loads(request.data)
    return apiCategory.createCategory(categoryJson)

@app.route('/category/', methods=['PUT'])
def update_category():

    categoryJson = json.loads(request.data)
    return apiCategory.updateCategory(categoryJson)


# PRODUCTCOMMERCEDETAIL
@app.route('/pcd/product/<id>', methods=['GET'])
def get_productCommerceDetail_by_product_id(id):
    return apiProductCommerceDetail.getPCDByIdProduct(id)

@app.route('/pcd/commerce/<id>', methods=['GET'])
def get_productCommerceDetail_by_commerce_id(id):
    return apiProductCommerceDetail.getPCDByIdCommerce(id)

@app.route('/pcd/', methods=['POST'])
def create_productCommerceDetail():
    pdcJson = json.loads(request.data)
    return apiProductCommerceDetail.createProductCommerceDetail(pdcJson)


# HISTORICAL
@app.route('/historical/product/<id>', methods=['GET'])
def get_historical(id):
    return apiHistorical.getHistoricalById(id)


@app.route('/historical/deprecated', methods=['GET'])
def get_allHistorical():
    return apiHistorical.getAllHistorical()

@app.route('/comparator/', methods=['GET'])
def get_comparator():
    return apiComparator.getAllComparator()

@app.route('/comparator/count', methods=['GET'])
def get_comparatorCount():
    return apiComparator.getComparatorCount()

@app.route('/comparator/<id>', methods=['GET'])
def get_comparatorById(id):
    return apiComparator.getComparatorById(id)

app.run(debug=True)