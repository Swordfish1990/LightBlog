"""
The flask application package.
"""

from flask import Flask
from config import config
from LightBlog.ext import db
from LightBlog.controller import front
from LightBlog.controller import plugin


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)
    db.app=app
    app.register_blueprint(front)
    app.register_blueprint(plugin)
    return app

