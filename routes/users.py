from flask import Blueprint, jsonify, request
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token

users_blueprint = Blueprint('users', __name__)

bcrypt = Bcrypt()

# Dummy users database
USERS = [
    {"id": 1, "username": "admin", "password": bcrypt.generate_password_hash("admin").decode('utf-8')}
]

@users_blueprint.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = next((u for u in USERS if u["username"] == username), None)
    if not user or not bcrypt.check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid username or password"}), 401

    access_token = create_access_token(identity=user["id"])
    return jsonify({"access_token": access_token})
