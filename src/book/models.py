import os
import sys

sys.path.append(os.getcwd())
from sqlalchemy import Column, ForeignKey, Integer, String

from extensions import db


class Autor(db.Model):
    __tablename__ = "autor"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))

    @classmethod
    def create(self, **kwargs):
        try:
            new_autor = Autor(**kwargs)
            db.session.add(new_autor)
            db.session.commit()
        except:
            print(f"we could insert the new {self.__tablename__}")


class Book(db.Model):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    date_publication = Column(String(30))

    @classmethod
    def create(self, **kwargs):
        try:
            new_book = Book(**kwargs)
            db.session.add(new_book)
            db.session.commit()
        except:
            print(f"we could insert the new {self.__tablename__}")


class BookAutor(db.Model):
    __tablename__ = "book_autor"
    id = Column(Integer, primary_key=True)
    book = Column(Integer, ForeignKey("book.id"))
    autor = Column(Integer, ForeignKey("autor.id"))

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
    status = Column(String(10))
    price = Column(Integer)
    book = Column(Integer, ForeignKey("book.id"))
    image = Column(String(50))

    @classmethod
    def create(self, **kwargs):
        try:
            new_ejemplar = Ejemplar(**kwargs)
            db.session.add(new_ejemplar)
            db.session.commit()
        except:
            print(f"we could insert the new {self.__tablename__}")


class EjemplarTransaction(db.Model):
    __tablename__ = "ejemplar_transaccion"
    id = Column(Integer, primary_key=True)
    transaccion = Column(Integer, ForeignKey("transactions.id"))
    ejemplar = Column(Integer, ForeignKey("ejemplar.id"))

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
    book = Column(Integer, ForeignKey("book.id"))
    topic = Column(Integer, ForeignKey("topic.id"))

    @classmethod
    def create(self, **kwargs):
        try:
            new_book_topics = BookTopics(**kwargs)
            db.session.add(new_book_topics)
            db.session.commit()
        except:
            print(f"we could insert the new {self.__tablename__}")
