import json
import os

from cerberus import Validator

from src.book.models import *


class BookController:
    def __init__(self, book: dict):
        validator_file = open(os.getcwd() + "/src/book/validator.json", "r")
        schema = json.load(validator_file)
        validator_file.close()
        self.validator = Validator(schema)
        self.validate(book)

    def create(self):
        pass

    def validate(self, new_book):
        if self.validator.validate(new_book):
            pass
        else:
            raise ValueError
