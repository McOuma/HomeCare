import json

import requests
from flask import jsonify, request

from app import db
from app.api_v1 import api
from app.auth import login_required
from app.models import User

# # Send login request
# url = "http://127.0.0.1:5000/login"
# data = {
#     "username": "muga",
#     "password": "cat"
# }
# headers = {
#     "Content-Type": "application/json"
# }
# response = requests.post(url, data=json.dumps(data), headers=headers)


@api.route("/users", methods=["GET"])
def get_all_users():
    users = User.query.all()
    users_list = []
    for user in users:
        user_data = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "created_on": user.created_on.strftime(
                "%Y-%m-%d %H:%M:%S"
            ),  # Convert datetime to string
        }
        users_list.append(user_data)
    return jsonify(users_list), 200


@api.route("/users/", methods=["POST"])
def create_user():
    data = request.json
    if (
        not data
        or not data.get("username")
        or not data.get("email")
        or not data.get("password")
    ):
        return jsonify({"message": "Missing required fields"}), 400
    username = data["username"]
    email = data["email"]
    password = data["password"]
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({"message": "User with this email already exists"}), 409
    new_user = User(username=username, email=email)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully"}), 201


# Route for updating a user
@api.route("/users/<int:user_id>/", methods=["PUT"])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404
    data = request.json
    if not data:
        return jsonify({"message": "No data provided for update"}), 400
    if "username" in data:
        user.username = data["username"]
    if "email" in data:
        user.email = data["email"]
    db.session.commit()
    return jsonify({"message": "User updated successfully"}), 200


# Route for deleting a user
@api.route("/users/<int:user_id>/", methods=["DELETE"])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully"}), 200


@api.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404
    return (
        jsonify(
            {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "created_on": user.created_on.strftime("%Y-%m-%d %H:%M:%S"),
            }
        ),
        200,
    )


@api.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data or not data.get("username") or not data.get("password"):
        return jsonify({"message": "Username or password is missing"}), 400
    username = data["username"]
    password = data["password"]
    user = User.query.filter_by(username=username).first()
    if not user or not user.verify_password(password):
        return jsonify({"message": "Invalid username or password"}), 401
    token = user.generate_token()
    return jsonify({"message": "Login successful", "token": token.decode("utf-8")}), 200


@api.route("/logout", methods=["POST"])
@login_required
def logout():
    user = request.user
    return jsonify({"message": "Logout successful"}), 200
