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
    """Root endpoint."""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """Returns a list of all usernames."""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Returns the API status."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Returns the full user object for a given username."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Adds a new user to the users dictionary."""
    data = request.get_json()

    # Check if data is valid JSON
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")

    # Check if username is provided
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Check if username already exists
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    # Add user and return confirmation
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
