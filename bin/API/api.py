#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, request, jsonify

from bin.API import apiProduct
from bin.API import apiCommerce
app = Flask(__name__)



#PRODUCT
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


#COMMERCE
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



#CATEGORY
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

#PRODUCTCOMMERCEDETAIL
#TODO crear logica de productCommerceDetail

@app.route('/pcd/product/<id>', methods=['GET'])
def get_productCommerceDetail_by_product_id(id):
    return apiProductCommerceDetail.getPCDByIdProduct(id)

@app.route('/pcd/commerce/<id>', methods=['GET'])
def get_productCommerceDetail_by_commerce_id(id):
    return apiProductCommerceDetail.getPCDByIdCommerce(id)
'''
de acá en abajo son ejemplos
https://codigofacilito.com/articulos/api-flask
'''

'''
@app.route('/', methods=['PUT'])
def create_record():
    record = json.loads(request.data)
    with open('/home/capi/PycharmProjects/serviceScrapper/bin/API/tmp/data.txt', 'r') as f:
        data = f.read()
    if not data:
        records = [record]
    else:
        records = json.loads(data)
        records.append(record)
    with open('/home/capi/PycharmProjects/serviceScrapper/bin/API/tmp/data.txt', 'w') as f:
        f.write(json.dumps(records, indent=2))
    return jsonify(record)


@app.route('/', methods=['POST'])
def update_record():
    record = json.loads(request.data)
    new_records = []
    with open('/tmp/data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
    for r in records:
        if r['name'] == record['name']:
            r['email'] = record['email']
        new_records.append(r)
    with open('/tmp/data.txt', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)


@app.route('/', methods=['DELETE'])
def delete_record():
    record = json.loads(request.data)
    new_records = []
    with open('/tmp/data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for r in records:
            if r['name'] == record['name']:
                continue
            new_records.append(r)
    with open('/tmp/data.txt', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)
'''

app.run(debug=True)