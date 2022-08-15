import os

from dotenv import load_dotenv
from flask import Flask

from extensions import db


def prod_app() -> Flask:
    load_dotenv()
    app: Flask = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KEY", "")
    db_user: str = os.getenv("DB_USER", "")
    db_key: str = os.getenv("DB_KEY", "")
    db_host: str = os.getenv("DB_HOST", "")
    db_name: str = os.getenv("DB_NAME", "")
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = f"postgresql://{db_user}:{db_key}@{db_host}/{db_name}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    return app
