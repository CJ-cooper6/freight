from flask_sqlalchemy import SQLAlchemy
from .database import db
import os


def init_app(app):
    from backend.configuration import config_provider
    config = config_provider.config['DATABASE']
    print(config)
    _init_sqlalchemy(app, config)


def _init_sqlalchemy(app, config):
    app.config["SQLALCHEMY_DATABASE_URI"] = get_connection_url(config)
    print(app.config["SQLALCHEMY_DATABASE_URI"])
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)



def get_connection_url(config):
    password = ":" + os.environ.get('MY_ENV_PASSWORD') or ":" + config["PASSWORD"] if len(config["PASSWORD"]) > 0 else ""
    user = os.environ.get('MY_ENV_USER') or config["USER"]
    host = os.environ.get('MY_ENV_HOST') or str(config["HOST"]) + ":" + str(config["PORT"])

    database = config["DB"]
    return "mysql+pymysql://{}{}@{}/{}?charset=utf8".format(user, password, host, database)
