#!/usr/bin/env python3
from flask import Flask, jsonify, request

app = Flask(__name__)

# Users dictionary (məlumat bazası rolunda)
users = {}

# Root endpoint
@app.route("/")
def home():
    return "Welcome to the Flask API!"

# /data endpoint – istifadəçi adlarının siyahısı
@app.route("/data")
def get_data():
    return jsonify(list(users.keys()))

# /status endpoint
@app.route("/status")
def status():
    return "OK"

# /users/<username> endpoint – dinamik istifadəçi məlumatı
@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# /add_user endpoint – POST sorğusu ilə yeni istifadəçi əlavə etmək
@app.route("/add_user", methods=["POST"])
def add_user():
    try:
        data = request.get_json(force=True)
    except:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Yeni istifadəçini əlavə edirik
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201

# Serveri işə salmaq
if __name__ == "__main__":
    app.run()
