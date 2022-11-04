import json
import os

from cerberus import Validator
from flask import Blueprint, jsonify, make_response, request, session
from flask_login import current_user, login_required

from src.book.controller import Book, Ejemplar

books_blueprint = Blueprint("books_blueprint", __name__)


@books_blueprint.route("/")
def read():
    output = []
    data = Ejemplar.query.all()
    for d in data:
        book = Book.query.filter_by(id=d.book).first()
        book = book.name
        aux = {
            "id": d.id,
            "img": d.image,
            "price": d.price,
            "name": book,
            "editorial": d.editorial,
        }
        output.append(aux)
    return make_response(jsonify({"message": "Success", "books": output}), 200)


@books_blueprint.route("/<id>")
def read_one(id):
    data = Ejemplar.query.filter_by(id=id).first()
    book = Book.query.filter_by(id=data.book).first()
    output = {
        "id": data.id,
        "img": data.image,
        "price": data.price,
        "name": book.name,
        "editorial": data.editorial,
        "number_pages": data.number_pages,
        "quantity": data.cuantity,
        "acabado": data.acabado,
        "size": data.size,
        "created_at": data.created_at,
        "stocked_at": data.stocked_at,
        "publication_date": book.date_publication,
        "isxn": book.isxn,
        "sinopsis": book.sinopsis,
    }
    return make_response(jsonify({"message": "Success", "book": output}), 200)


@books_blueprint.route("/create", methods=["POST"])
@login_required
def create():
    if current_user.auth_helper.can_access_crud_books():
        try:
            validator_file = open(os.getcwd() + "/src/book/validator.json", "r")
            schema = json.load(validator_file)
            validator_file.close()
            validator = Validator(schema)
            if validator.validate(request.json):
                new_book = Book.create(**request.json)
                return make_response(
                    jsonify({"message": "book created"}),
                    201,
                )
            else:
                return make_response(
                    jsonify({"message": "wrong request"}),
                    406,
                )
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
