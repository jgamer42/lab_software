import base64
import hashlib

from src.users.models import User as UserModel


class User:
    manager = UserModel
    is_active = None

    def __init__(self):
        raise Exception("Constructor blocked")

    @classmethod
    def login(self, username: str, password: str) -> object:
        decoded_password: bytes = base64.b64decode(password.encode("utf-8"))
        hashed_password: str = hashlib.md5(decoded_password).hexdigest()
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

    @property
    def is_authenticated(self):
        return self.is_active
