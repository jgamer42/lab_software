import os
import sys

sys.path.append(os.getcwd())
from sqlalchemy import Column, ForeignKey, Integer, String

from extensions import db


class Payments(db.Model):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True)
    value = Column(Integer)
    payment_method = Column(Integer, ForeignKey("card.id"))
    date = Column(String(30))


class Card(db.Model):
    __tablename__ = "card"
    id = Column(Integer, primary_key=True)
    amount = Column(Integer)
    owner = Column(String(100), ForeignKey("app_users.id"))
    name = Column(String(30))
