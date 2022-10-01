import os
import sys

from flask_login import UserMixin
from sqlalchemy import Column, ForeignKey, Integer, String

sys.path.append(os.getcwd())
from extensions import db


class User(UserMixin, db.Model):
    __tablename__ = "app_users"
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
