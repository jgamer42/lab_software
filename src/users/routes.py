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
    except:
        return make_response(jsonify({"message": "something was wrong"}), 500)


@users_blueprint.route("/logged")
@login_required
def test_login():
    logout_user()
    return "logg out"
