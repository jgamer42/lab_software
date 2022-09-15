import os
import sys

sys.path.append(os.getcwd())
from sqlalchemy import Column, ForeignKey, Integer, String

from extensions import db


class User(db.Model):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    last_name = Column(String(30))
    birth_date = Column(String(30))
    gender = Column(String(30))
    email = Column(String(30))
    user = Column(String(30))
    password = Column(String(100))
    role = Column(Integer, ForeignKey("role.id"))
    messaging_addres = Column(String(50))
    birth_place = Column(String(50))


class Role(db.Model):
    __tablename__ = "role"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))


class Permission(db.Model):
    __tablename__ = "permission"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    description = Column(String(125))


class PermissionRole(db.Model):
    __tablename__ = "permission_role"
    id = Column(Integer, primary_key=True)
    role = Column(Integer, ForeignKey("role.id"))
    permission = Column(Integer, ForeignKey("permission.id"))
