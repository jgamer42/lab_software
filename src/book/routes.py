from cerberus import Validator
from flask import Blueprint, jsonify, make_response, request, session
from flask_login import current_user, login_required

from src.book.controller import BookController

books_blueprint = Blueprint("books_blueprint", __name__)


@books_blueprint.route("/")
def read():
    output = BookController.get_all()
    return make_response(jsonify({"message": "Success", "books": output}), 200)


@books_blueprint.route("/<id>")
def read_one(id):
    output = BookController.get(id)
    return make_response(jsonify({"message": "Success", "book": output}), 200)


@books_blueprint.route("/create", methods=["POST"])
@login_required
def create():
    if current_user.auth_helper.can_access_crud_books():
        try:
            BookController.create_book(**request.json)
            return make_response(
                jsonify({"message": "book created"}),
                201,
            )
        except AssertionError:
            return make_response(jsonify({"message": "wrong request"}), 400)
        except ValueError:
            return make_response(
                jsonify({"message": "something wrong with your request"}), 400
            )
    else:
        return make_response(jsonify({"message": "not allowed for your user"}), 403)


@books_blueprint.route("/update/<id>", methods=["PUT"])
@login_required
def update(id):
    if current_user.auth_helper.can_access_crud_books():
        try:
            BookController.update(id, request.json)
            return make_response(jsonify({"message": "book created"}), 201)

        except ValueError as E:
            return make_response(
                jsonify({"message": "something wrong with your request"}), 400
            )
    else:
        return make_response(jsonify({"message": "not allowed for your user"}), 403)


@books_blueprint.route("/delete/<id>", methods=["DELETE"])
@login_required
def delete(id):
    if current_user.auth_helper.can_access_crud_books():
        try:
            BookController.delete(id)
            return make_response(jsonify({"message": "book created"}), 201)

        except ValueError as E:
            return make_response(
                jsonify({"message": "something wrong with your request"}), 400
            )
    else:
        return make_response(jsonify({"message": "not allowed for your user"}), 403)
