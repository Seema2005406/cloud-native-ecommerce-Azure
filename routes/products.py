from flask import Blueprint, jsonify, request

products_blueprint = Blueprint('products', __name__)

# Dummy data
PRODUCTS = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Smartphone", "price": 499.99}
]

@products_blueprint.route('/', methods=['GET'])
def get_products():
    return jsonify(PRODUCTS)

@products_blueprint.route('/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in PRODUCTS if p["id"] == product_id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product)
