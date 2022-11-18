import datetime
import os
import sys

sys.path.append(os.getcwd())
from sqlalchemy import Column, ForeignKey, Integer, String, Text

from extensions import db


class Autor(db.Model):
    __tablename__ = "autor"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))

    @classmethod
    def create(self, **kwargs):
        try:
            new_autor = Autor(**kwargs)
            db.session.add(new_autor)
            db.session.commit()
            return new_autor
        except Exception as E:
            print(f"we could insert the new {self.__tablename__}")


class Book(db.Model):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    date_publication = Column(String(30))
    isxn = Column(String(100))
    sinopsis = Column(Text)

    @classmethod
    def get_newest(self):
        try:
            output = Ejemplar.query()
            print(output)
        except:
            print(f"we could not insert the new {self.__tablename__}")

    @classmethod
    def create(self, **kwargs):
        try:
            autor = Autor.query.filter_by(name=kwargs["autor"])
            if list(autor) == []:
                autor = Autor.create(name=kwargs["autor"])
            else:
                autor = autor.first()
            sanity_check = self.query.filter_by(name=kwargs["name"])
            if list(sanity_check) == []:
                book = Book(
                    name=kwargs["name"],
                    date_publication=kwargs["date"],
                    isxn=kwargs["isxn"],
                    sinopsis=kwargs["sinopsis"],
                )
                db.session.add(book)
                db.session.commit()
                book = list(Book.query.all())[-1]
                book_autor = BookAutor(book=book.id, autor=autor.id)
                db.session.add(book_autor)
                db.session.commit()
            else:
                book = sanity_check.first()
            ejemplar = Ejemplar.query.filter_by(
                editorial=kwargs["editorial"], book=book.id
            )
            if list(ejemplar) == []:
                ejemplar = Ejemplar.create(
                    editorial=kwargs["editorial"],
                    book=book.id,
                    price=kwargs["price"],
                    cuantity=kwargs["number"],
                    status="AVAILABLE",
                    size=kwargs["size"],
                    acabado=kwargs["acabado"],
                    image=kwargs["image"],
                    created_at=str(datetime.datetime.now()),
                    stocked_at=str(datetime.datetime.now()),
                )
        except Exception as e:
            print(f"we could not insert the new {self.__tablename__}")


class BookAutor(db.Model):
    __tablename__ = "book_autor"
    id = Column(Integer, primary_key=True)
    book = Column(Integer, ForeignKey("book.id", ondelete="CASCADE"))
    autor = Column(Integer, ForeignKey("autor.id", ondelete="CASCADE"))

    @classmethod
    def create(self, **kwargs):
        try:
            new_book = BookAutor(**kwargs)
            db.session.add(new_book)
            db.session.commit()
        except:
            print(f"we could insert the new {self.__tablename__}")


class Ejemplar(db.Model):
    __tablename__ = "ejemplar"
    id = Column(Integer, primary_key=True)
    editorial = Column(String(30))
    number_pages = Column(Integer)
    status = Column(String(30))
    price = Column(Integer)
    book = Column(Integer, ForeignKey("book.id", ondelete="CASCADE"))
    image = Column(Text)
    cuantity = Column(Integer)
    acabado = Column(String(50))
    size = Column(String(50))
    created_at = Column(String(100))
    stocked_at = Column(String(100))

    @classmethod
    def create(self, **kwargs):
        new_ejemplar = Ejemplar(**kwargs)
        db.session.add(new_ejemplar)
        db.session.commit()


class EjemplarTransaction(db.Model):
    __tablename__ = "ejemplar_transaccion"
    id = Column(Integer, primary_key=True)
    transaccion = Column(Integer, ForeignKey("transactions.id", ondelete="CASCADE"))
    ejemplar = Column(Integer, ForeignKey("ejemplar.id", ondelete="CASCADE"))

    @classmethod
    def create(self, **kwargs):
        try:
            new_ejemplar_transaction = EjemplarTransaction(**kwargs)
            db.session.add(new_ejemplar_transaction)
            db.session.commit()
        except:
            print(f"we could insert the new {self.__tablename__}")


class BookTopics:
    __tablename__ = "book_topic"
    id = Column(Integer, primary_key=True)
    book = Column(Integer, ForeignKey("book.id", ondelete="CASCADE"))
    topic = Column(Integer, ForeignKey("topic.id", ondelete="CASCADE"))

    @classmethod
    def create(self, **kwargs):
        try:
            new_book_topics = BookTopics(**kwargs)
            db.session.add(new_book_topics)
            db.session.commit()
        except:
            print(f"we could insert the new {self.__tablename__}")
