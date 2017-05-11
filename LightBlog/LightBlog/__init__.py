"""
The flask application package.
"""

from flask import Flask
from config import config
from ext import db
from LightBlog.controller import front


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)
    app.register_blueprint(front)
    return app

