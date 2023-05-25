from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Thundermandy12!@127.0.0.1/fieldapp"
app.config['SECRET_KEY']= "secret key"

db = SQLAlchemy(app)

def create_app():    
    from views import views
    app.register_blueprint(views, url_prefix='/')

    return app