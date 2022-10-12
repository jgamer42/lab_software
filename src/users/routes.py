import datetime

from flask import Blueprint, jsonify, make_response, request, session
from flask_login import current_user, login_required, login_user, logout_user

from src.users.controllers.user import User

users_blueprint = Blueprint("users_blueprint", __name__)


@users_blueprint.route("/login", methods=["POST"])
def login():
    try:
        data = request.json

        user = User.login(data["username"], data["password"])
        if user is not None:
            login_user(user, duration=datetime.timedelta(minutes=1))
            session.permanent = True
            return make_response(jsonify({"message": "succesfull login"}), 200)
        else:
            return make_response(
                jsonify({"message": "wrong password or username"}), 203
            )
    except Exception as e:
        return make_response(jsonify({"message": "something was wrong"}), 500)


@users_blueprint.route("/logged")
@login_required
def logout():
    logout_user()
    return make_response(jsonify({"message": "logged out"}), 200)


@users_blueprint.route("/register", methods=["POST"])
def register():
    try:
        new_user_data = request.json
        registred = User.create(**new_user_data)
        if registred:
            user = User.login(new_user_data["user"], new_user_data["password"])
            login_user(user, duration=datetime.timedelta(minutes=1))
            session.permanent = True
            return "succesfull register"
        else:
            return "we could not create your user try again"

    except Exception as E:
        return "wops something wrong"
