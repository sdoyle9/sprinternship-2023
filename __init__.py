from flask import Flask, Blueprint

from .extensions import db
from .views import main

def create_app():
    app = Flask(__name__)
    
    db.init_app(app)
    
    app.register_blueprint(main)
    
    return app
    