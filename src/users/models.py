import os
import sys

from flask_login import UserMixin
from sqlalchemy import Column, ForeignKey, Integer, String, Text, update

sys.path.append(os.getcwd())
from extensions import db


class User(UserMixin, db.Model):
    __tablename__ = "app_users"
    id = Column(String(100), primary_key=True)
    name = Column(String(100))
    birth_date = Column(String(30))
    gender = Column(String(30))
    email = Column(String(100), unique=True)
    user = Column(String(30))
    password = Column(String(100))
    role = Column(Integer, ForeignKey("role.id", ondelete="CASCADE"))
    messaging_addres = Column(String(100))
    birth_place = Column(String(50))
    phone_number = Column(String(80))

    def serialize(self):
        output = {}
        fields = [
            "id",
            "name",
            "user",
            "birth_date",
            "gender",
            "email",
            "user",
            "messaging_addres",
            "birth_place",
            "phone_number",
        ]
        for field in fields:
            output[field] = getattr(self, field)
        return output

    @classmethod
    def create(self, **kwargs):
        try:
            new_user = User(**kwargs)
            db.session.add(new_user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("we could insert the new user")

    @classmethod
    def update(self, id, new_data):
        try:
            target = update(self)
            target = target.values(new_data)
            target = target.where(self.id == id)
            db.session.execute(target)
            db.session.commit()
        except:
            db.session.rollback()
            print("fallo actualizando libro")


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
    role = Column(Integer, ForeignKey("role.id", ondelete="CASCADE"))
    permission = Column(Integer, ForeignKey("permission.id", ondelete="CASCADE"))
