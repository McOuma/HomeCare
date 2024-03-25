from flask import jsonify, request

from app import db
from app.api_v1 import api
from app.auth import login_required
from app.models import User


@api.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data or not data.get("username") or not data.get("password"):
        return jsonify({"message": "Username or password is missing"}), 400

    username = data["username"]
    password = data["password"]
    user = User.query.filter_by(username=username).first()

    if not user or not user.check_password(password):
        return jsonify({"message": "Invalid username or password"}), 401

    token = user.generate_token()
    return jsonify({"message": "Login successful", "token": token}), 200




@api.route("/logout", methods=["POST"])
@login_required
def logout():
    user = request.user
    user.token = None
    db.session.commit()
    return jsonify({"message": "Logout successful"}), 200
