import datetime
import os

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager

from extensions import db
from src.book.routes import books_blueprint
from src.users.controllers.user import User
from src.users.routes import users_blueprint


def prod_app() -> Flask:
    load_dotenv()
    app: Flask = Flask(__name__)
    CORS(
        app,
        origins=["http://127.0.0.1:8080", "http://localhost:8080"],
        supports_credentials=True,
    )
    app.secret_key = os.getenv("SECRET_KEY", "")
    db_user: str = os.getenv("DB_USER", "")
    db_key: str = os.getenv("DB_KEY", "")
    db_host: str = os.getenv("DB_HOST", "")
    db_name: str = os.getenv("DB_NAME", "")
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = f"postgresql://{db_user}:{db_key}@{db_host}/{db_name}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PERMANENT_SESSION_LIFETIME"] = datetime.timedelta(minutes=5)
    app.register_blueprint(users_blueprint)
    app.register_blueprint(books_blueprint, url_prefix="/book")

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.build(user_id)

    db.init_app(app)
    return app
