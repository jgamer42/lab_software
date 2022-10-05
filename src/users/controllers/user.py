import base64
import hashlib
import json
import os

from cerberus import Validator

from src.users.models import User as UserModel


class User:
    manager = UserModel
    is_active = None
    validator_file = open(os.getcwd() + "/src/users/validators/user.json", "r")
    schema = json.load(validator_file)
    validator_file.close()
    validator = Validator(schema)

    def __init__(self):
        raise Exception("Constructor blocked")

    @classmethod
    def login(self, username: str, password: str) -> object:
        hashed_password = self.handle_password(password)
        return self.manager.query.filter_by(
            password=hashed_password, user=username
        ).first()

    @classmethod
    def build(self, id: int):
        if self.manager.query.get(id) is not None:
            self.is_active = True
        else:
            self.is_active = False
        return self

    @classmethod
    def create(self, **kwargs):
        if self.validator.validate(kwargs):
            kwargs["password"] = self.handle_password(kwargs["password"])
            kwargs["role"] = 1
            self.manager.create(**kwargs)
            return True
        else:
            return False

    @property
    def is_authenticated(self):
        return self.is_active

    @staticmethod
    def handle_password(password):
        decoded_password: bytes = base64.b64decode(password.encode("utf-8"))
        hashed_password: str = hashlib.md5(decoded_password).hexdigest()
        return hashed_password
