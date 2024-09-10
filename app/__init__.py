from flask import Flask
from flask_bootstrap import Bootstrap

from .config import Config

def create_app():
    app = Flask(__name__)
    #de esta forma se inicializa bootstrap
    bootstrap = Bootstrap(app)
    app.config.from_object(Config)
    app.debug = True

    return app