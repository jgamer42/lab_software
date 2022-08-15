import os
import sys

sys.path.append(os.getcwd())
from sqlalchemy import Column, Integer, String

from extensions import db


class User(db.Model):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
