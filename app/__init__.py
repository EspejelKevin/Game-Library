import aifc
from flask import Flask
from config import Config
from .start import start
from .auth import auth

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    app.register_blueprint(start)
    app.register_blueprint(auth)
    
    return app
