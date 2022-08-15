import os
import sys

sys.path.append(os.getcwd())
from extensions import db
from src.app import prod_app
from src.users.models import User

db.create_all(app=prod_app())
