#!/usr/bin/python3
"""
A simple Flask API providing user management endpoints.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user storage
users = {}


@app.route("/")
def home():
    """Root endpoint: Welcome message."""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """Returns a list of all usernames stored in the API."""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Returns the API status."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Returns the full object for a specific username."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Adds a new user to the storage.
    Handles JSON validation, missing fields, and duplicates.
    """
    # 1. JSON-un mövcudluğunu və doğruluğunu yoxla
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    # 2. Username sahəsini yoxla
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # 3. Dublikat istifadəçi yoxlaması (409 Conflict)
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # 4. İstifadəçini əlavə et və 201 Created qaytar
    users[username] = data
    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run()
