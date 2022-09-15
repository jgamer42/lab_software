import os
import sys

sys.path.append(os.getcwd())
from sqlalchemy import Column, ForeignKey, Integer, String

from extensions import db


class Topics(db.Model):
    __tablename__ = "topics"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    description = Column(String(30))


class Transaction(db.Model):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True)
    status = Column(String(30))
    last_update = Column(String(30))
    expiration_date = Column(String(30))
    type = Column(Integer, ForeignKey("transaction_types.id"))
    payment = Column(Integer, ForeignKey("payments.id"))
    validator = Column(String(255))


class TransactionTypes(db.Model):
    __tablename__ = "transaction_types"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))


class OutStock(db.Model):
    __tablename__ = "out_of_stock"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    date = Column(String(30))
