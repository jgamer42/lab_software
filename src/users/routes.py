import datetime

from flask import Blueprint, session
from flask_login import current_user, login_required, login_user, logout_user

from src.users.models import User

users_blueprint = Blueprint("users_blueprint", __name__)


@users_blueprint.route("/login")
def login():
    user = User.query.get(1)
    login_user(user, duration=datetime.timedelta(minutes=1))
    session.permanent = True
    return "hola mundo"


@users_blueprint.route("/loged")
@login_required
def test_login():
    # logout_user()
    return "logg out"
