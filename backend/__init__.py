import os
from flask import Flask
from flask_cors import CORS
from backend import database
from backend.database import db
from .configuration import config_provider
from .freight import model
# 使用db.create_all() 必须要先导入要创建的表模型类
# `from .freight import model`
# 否则 调用了create_all方法，代码没有报错，表也没有创建


def create_app():
    app = Flask(__name__)

    CORS(app, supports_credentials=True)
    config_file_path = get_config_file_path()
    config_provider.load(config_file_path)
    database.init_app(app)
    _register_blueprints(app)
    with app.app_context():
        db.create_all()


    return app


def get_config_file_path():
    from utils import get_project_root
    config_file = os.path.join(get_project_root(), f"conf/config.yml")
    return config_file


def _register_blueprints(app):
    from backend.api import bp as api

    app.register_blueprint(api, url_prefix="/api")