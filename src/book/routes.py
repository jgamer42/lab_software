import datetime

from flask import Blueprint, jsonify, make_response, request, session
from flask_login import current_user, login_required, login_user, logout_user

from src.users.controllers.user import User

books_blueprint = Blueprint("books_blueprint", __name__)


@books_blueprint.route("/create")
def create():
    return "creando libro"


@books_blueprint.route("/update")
def update():
    return "editando libro"


@books_blueprint.route("/delete")
def delete():
    return "eliminando libro"
