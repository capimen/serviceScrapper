#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, request, jsonify

from bin.API import apiProduct
from bin.controllers.ProductController import ProductController

app = Flask(__name__)




@app.route('/product/<id>', methods=['GET'])
def get_Product(id):
    return apiProduct.getProductById(id)


@app.route('/product/', methods=['GET'])
def get_AllProducts():

    return apiProduct.getAllProduct()


@app.route('/product/', methods=['POST'])
def create_product():

# hay que corregir esta opcion, ya que la logica no deberia
# ser guarda un producto sin tener en cuenta la pagina,
# por lo mismo, acá debería funcionar con la logica del proceso
# almacenado y simplificar la inserción
    productJson = json.loads(request.data)
    return apiProduct.createProduct(productJson)


@app.route('/product/', methods=['PUT'])
def update_record():

    productJson = json.loads(request.data)
    return apiProduct.updateProduct(productJson)

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