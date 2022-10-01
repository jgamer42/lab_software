import os
import sys

sys.path.append(os.getcwd())
from extensions import db
from src.app import prod_app
from src.book.models import *
from src.users.models import *
from src.users.paymentsMethods import *
from src.utils.models import *

db.create_all(app=prod_app())
