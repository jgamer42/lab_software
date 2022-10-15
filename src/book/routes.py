from flask import Blueprint, jsonify, make_response, request, session
from flask_login import current_user, login_required

from src.book.controller import Book

books_blueprint = Blueprint("books_blueprint", __name__)


@books_blueprint.route("/")
def read():
    return "lista libros"


@books_blueprint.route("/create", methods=["POST"])
@login_required
def create():
    if current_user.auth_helper.can_access_crud_books():
        try:
            new_book = Book({})
            return make_response(jsonify({"message": "book created"}), 201)
        except ValueError:
            return make_response(
                jsonify({"message": "something wrong with your request"}), 400
            )
    else:
        return make_response(jsonify({"message": "not allowed for your user"}), 403)


@books_blueprint.route("/update")
@login_required
def update():
    return "editando libro"


@books_blueprint.route("/delete")
@login_required
def delete():
    return "eliminando libro"
