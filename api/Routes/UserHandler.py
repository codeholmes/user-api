from flask import Flask, request, jsonify, abort, Blueprint
from api.Models.User import User

user_bp = Blueprint("user_bp", __name__)
app = Flask(__name__)


@user_bp.route("/users", methods=["POST"])
def create():
    """Only POST menthod allowed"""
    user_data = request.json
    if not user_data:
        abort(403)
    else:
        usr = User.create_user(User, user_data)
        response = jsonify({"message": "User created successfully", "data": usr})
        return response, 200


@user_bp.route("/users", methods=["GET"])
def get_all_users():
    """Only GET menthod allowed"""
    return User.get_all_users(User)


@user_bp.route("/users/<string:id>", methods=["GET"])
def get_user(id):
    """Only GET menthod allowed"""
    return User.get_user(User, id)


@user_bp.route("/users/<string:id>", methods=["PUT"])
def update_user(id):
    """Only PUT menthod allowed"""
    new_data = request.json
    return User.update_user(User, id, new_data)


@user_bp.route("/users/<string:id>", methods=["DELETE"])
def delete_user(id):
    """Only DELETE method allowed"""
    return User.delete_user(User, id)
