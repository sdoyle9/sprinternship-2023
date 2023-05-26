from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////Users/nilo-noche/cbbelapp.db"
app.config['SECRET_KEY']= "secret key"

db = SQLAlchemy(app)

def create_app():    
    from views import views
    app.register_blueprint(views, url_prefix='/')

    return app