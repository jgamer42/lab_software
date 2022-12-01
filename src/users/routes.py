import datetime

from flask import Blueprint, jsonify, make_response, request, session
from flask_login import login_required, login_user, logout_user

from src.users.controllers.user import User

users_blueprint = Blueprint("users_blueprint", __name__)


@users_blueprint.route("/login", methods=["POST"])
def login():
    data = request.json
    user_to_login, user_information = User.login(data["username"], data["password"])
    if user_to_login is not None:
        login_user(user_to_login, duration=datetime.timedelta(hours=1))
        session.permanent = True
        return make_response(
            jsonify({"message": "succesfull login", "data": user_information}), 200
        )
    else:
        return make_response(jsonify({"message": "wrong password or username"}), 403)


@users_blueprint.route("/loggout", methods=["POST", "GET"])
@login_required
def logout():
    logout_user()
    return make_response(jsonify({"message": "logged out"}), 200)


@users_blueprint.route("/user/<id>", methods=["GET"])
@login_required
def info(id):
    user_information = User.get_user_info(id)
    return make_response(jsonify({"data": user_information}), 200)


@users_blueprint.route("/update/<id>", methods=["PUT"])
@login_required
def update(id):
    User.update_data(id, request.json)
    return make_response(jsonify({"message": "succesfull update"}), 200)


@users_blueprint.route("/register", methods=["POST"])
def register():
    new_user_data = request.json
    registred = User.create(**new_user_data)
    if registred:
        user_to_login, user_information = User.login(
            new_user_data["user"], new_user_data["password"]
        )
        login_user(user_to_login, duration=datetime.timedelta(minutes=1))
        session.permanent = True
        return make_response(
            jsonify({"message": "succesfull register", "data": user_information}), 201
        )
    else:
        return make_response(
            jsonify({"message": "we not could create your user try again"}), 400
        )
