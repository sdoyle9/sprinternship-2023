from flask import Flask, Blueprint

from models import Projects
from extensions import db
from views import main

app = Flask(__name__)


# def create_app():
#     app = Flask(__name__)
    
#     db.init_app(app)
    
#     app.register_blueprint(main)
    
#     return app
    