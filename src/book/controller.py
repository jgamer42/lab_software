import json
import os

from cerberus import Validator

from extensions import db
from src.book import models as BookModels


class BookController:
    validator_file = open(os.getcwd() + "/src/book/validator.json", "r")
    schema = json.load(validator_file)
    validator_file.close()
    validator = Validator(schema)

    @classmethod
    def create_book(self, *args, **kwargs):
        if self.validate(kwargs):
            autor = self.create_autor(autor=kwargs["autor"])
            book = BookModels.Book.create(
                name=kwargs["name"],
                date=kwargs["date"],
                isxn=kwargs["isxn"],
                sinopsis=kwargs["sinopsis"],
            )
            self.create_ejemplar(
                editorial=kwargs["editorial"],
                number_pages=kwargs["num_pag"],
                price=kwargs["price"],
                book=book.id,
                status="DISPONIBLE",
                image=kwargs["image"],
                cuantity=kwargs["number"],
                acabado=kwargs["acabado"],
                size=kwargs["size"],
                created_at=kwargs["date"],
                language=kwargs["language"],
                weight=kwargs["weight"],
            )
            self.create_book_autor(book=book.id, autor=autor.id)
        else:
            raise AssertionError

    @classmethod
    def create_ejemplar(self, *args, **kwargs):
        BookModels.Ejemplar.create(**kwargs)

    @classmethod
    def create_book_autor(self, book: int, autor: int):
        BookModels.BookAutor.create(book=book, autor=autor)

    @classmethod
    def create_autor(self, autor: str):
        query = BookModels.Autor.query.filter_by(name=autor)
        if list(query) == []:
            autor = BookModels.Autor.create(name=autor)
        else:
            autor = query.first()
        return autor

    @classmethod
    def get_all(self):
        output = []
        data = BookModels.Ejemplar.query.all()
        for d in data:
            book = BookModels.Book.query.filter_by(id=d.book).first()
            book = book.name
            aux = {
                "id": d.id,
                "img": d.image,
                "price": d.price,
                "name": book,
                "editorial": d.editorial,
            }
            output.append(aux)
        return output

    @classmethod
    def get(self, id: int):
        data = BookModels.Ejemplar.query.filter_by(id=id).first()
        book = BookModels.Book.query.filter_by(id=data.book).first()
        autor = (
            BookModels.Autor.query.join(
                BookModels.BookAutor, BookModels.BookAutor.autor == BookModels.Autor.id
            )
            .filter(BookModels.BookAutor.book == book.id)
            .first()
        )
        output = {
            "id": data.id,
            "img": data.image,
            "price": data.price,
            "name": book.name,
            "autor": autor.name,
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
            "weight": data.weight,
            "idioma": data.language,
        }
        return output

    @classmethod
    def validate(self, new_book) -> bool:
        if self.validator.validate(new_book):
            return True
        raise ValueError

    @classmethod
    def update(self, id: int, new_data: dict):
        if self.validate(new_data):
            ejemplar_fields = [
                "editorial",
                "num_pag",
                "price",
                "status",
                "image",
                "number",
                "acabado",
                "size",
                "language",
                "weight",
            ]
            ejemplar_update_data = {
                clave: new_data[clave]
                for clave in new_data.keys()
                if clave in ejemplar_fields
            }
            book = BookModels.Book.query.filter_by(name=new_data["name"])
            if list(book) == []:
                book = BookModels.Book.create(
                    name=new_data["name"],
                    date=new_data["date"],
                    isxn=new_data["isxn"],
                    sinopsis=new_data["sinopsis"],
                )
                ejemplar_update_data["book"] = book.id
            autor = BookModels.Autor.query.filter_by(name=new_data["autor"])
            if list(autor) == []:
                autor = BookModels.Autor.create(name=new_data["autor"])
                try:
                    book_id = book.id
                except:
                    book_id = list(
                        BookModels.Book.query.filter_by(name=new_data["name"])
                    )[0].id
                try:
                    BookModels.BookAutor.filter_by(
                        autor=autor.id, book=book_id
                    ).delete()
                except:
                    print("error deleting old book_autor")
                BookModels.BookAutor.create(book=book_id, autor=autor.id)
            ejemplar_update_data["number_pages"] = ejemplar_update_data["num_pag"]
            ejemplar_update_data["cuantity"] = ejemplar_update_data["number"]
            del ejemplar_update_data["num_pag"]
            del ejemplar_update_data["number"]
            ejemplar = BookModels.Ejemplar.query.filter_by(id=id).first()
            ejemplar.update(id, ejemplar_update_data)

    @classmethod
    def delete(self, id: int):
        BookModels.Ejemplar.delete(id)
