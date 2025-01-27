from flask import Flask, jsonify
from routes.products import products_blueprint
from routes.users import users_blueprint

app = Flask(__name__)

# Register blueprints
app.register_blueprint(products_blueprint, url_prefix='/api/products')
app.register_blueprint(users_blueprint, url_prefix='/api/users')

@app.route('/')
def index():
    return jsonify({"message": "Welcome to the Flask eCommerce Platform!"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

