#!/usr/bin/env python3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret-key'  # Güclü secret key seçin

# Basic Auth
auth = HTTPBasicAuth()

# Users dictionary (username: {password_hash, role})
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

# Basic Auth verification
@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return user

# Basic Auth protected route
@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

# JWT setup
jwt = JWTManager(app)

# JWT Login route
@app.route("/login", methods=["POST"])
def login():
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    user = users.get(username, None)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Bad username or password"}), 401

    # JWT token yaratmaq
    access_token = create_access_token(identity={"username": username, "role": user["role"]})
    return jsonify(access_token=access_token), 200

# JWT Protected route
@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

# Role-based protected route (admin only)
@app.route("/admin-only")
@jwt_required()
def admin_only():
    identity = get_jwt_identity()
    if identity["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

# Custom error handlers for JWT
@jwt.unauthorized_loader
def handle_unauthorized(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token(err):
    return jsonify({"error": "Token has expired"}), 401

if __name__ == "__main__":
    app.run()
