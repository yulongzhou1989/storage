from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
from flask_cors import CORS, cross_origin

from db import DB
import json

app = FlaskAPI(__name__)

@app.route("/fetchAllProducts", methods=['GET'])
@cross_origin()
def getAllProducts():
    db = DB()
    products = db.getAllProducts()
    return json.dumps(products), 200

@app.route("/addProduct", methods=['POST'])
@cross_origin()
def addProduct():
    db = DB()
    product = Product(request.json)
    res = db.addProduct(product)
    return json.dumps(res), 200

if __name__ == "__main__":
    app.run(debug=True)