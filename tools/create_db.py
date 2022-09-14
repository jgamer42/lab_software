import os
import sys

sys.path.append(os.getcwd())
from extensions import db
from src.app import prod_app
from src.book import *
from src.users import *

db.create_all(app=prod_app())
