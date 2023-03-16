from flask import Flask, request, make_response, jsonify, abort, Blueprint
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
        usr = User.create_user(user_data)
        print("Data added", usr)
        response = jsonify("status : successfull")
        return make_response(response, 200)
