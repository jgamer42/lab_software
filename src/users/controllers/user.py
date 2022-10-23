import base64
import hashlib
import json
import os
from typing import Union

from cerberus import Validator
from flask_login import current_user

from src.users.controllers.auth import AuthHelper
from src.users.models import User as UserModel


class User:
    manager = UserModel
    is_active = None
    validator_file = open(os.getcwd() + "/src/users/validator.json", "r")
    schema = json.load(validator_file)
    validator_file.close()
    validator = Validator(schema)
    auth_helper = None
    data = None

    def __init__(self):
        raise Exception("Constructor blocked")

    @classmethod
    def serialize(self):
        relevant_fields = ["auth_helper"]
        output = {}
        elements = dir(self)
        clean_elements = [
            element
            for element in elements
            if "__" not in element and element in relevant_fields
        ]
        for element in clean_elements:
            a = getattr(self, element)
            output[element] = a.serialize()
        return output

    def get_info(self):
        return self.manager.is_anonymous()

    @classmethod
    def login(self, username: str, password: str) -> object:
        hashed_password = self.handle_password(password)
        db_data = self.manager.query.filter_by(
            password=hashed_password, user=username
        ).first()

        complemented_data = self.build(db_data.id)
        complemented_data = complemented_data.serialize()
        complemented_data.update(db_data.serialize())
        return db_data, complemented_data

    @classmethod
    def build(self, id: int):
        data: Union[UserModel, None] = self.manager.query.get(id)
        if data is not None:
            self.data = data
            self.is_active = True
            self.auth_helper = AuthHelper(data.role)
        else:
            self.is_active = False
        return self

    @classmethod
    def create(self, **kwargs):
        if self.validator.validate(kwargs):
            kwargs["password"] = self.handle_password(kwargs["password"])
            if (
                hasattr(current_user, "auth_helper")
                and current_user.auth_helper.can_create_admin()
            ):
                kwargs["role"] = 1
            else:
                kwargs["role"] = 3
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
