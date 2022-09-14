import os
import sys
from email.policy import strict

sys.path.append(os.getcwd())
from sqlalchemy import Column, ForeignKey, Integer, String

from extensions import db


class Autor(db.Model):
    __tablename__ = "autor"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))


class Book(db.Model):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    date_publication = Column(String(30))


class BookAutor(db.Model):
    __tablename__ = "book_autor"
    id = Column(Integer, primary_key=True)
    book = Column(Integer, ForeignKey("book.id"))
    autor = Column(Integer, ForeignKey("autor.id"))


class Ejemplar(db.Model):
    __tablename__ = "ejemplar"
    id = Column(Integer, primary_key=True)
    editorial = Column(String(30))
    number_pages = Column(Integer)
    status = Column(String(10))
    price = Column(Integer)
    book = Column(Integer, ForeignKey("book.id"))


class EjemplarTransaction(db.Model):
    __tablename__ = "ejemplar_transaccion"
    id = Column(Integer, primary_key=True)
    transaccion = Column(Integer, ForeignKey("transaction.id"))
    ejemplar = Column(Integer, ForeignKey("ejemplar.id"))


class BookTopics:
    __tablename__ = "book_topic"
    id = Column(Integer, primary_key=True)
    book = Column(Integer, ForeignKey("book.id"))
    topic = Column(Integer, ForeignKey("topic.id"))
