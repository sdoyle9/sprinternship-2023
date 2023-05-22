from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template

app = Flask(__name__)

main = Blueprint('main', __name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Thundermandy12!@127.0.0.1/fieldapp"
app.config['SECRET_KEY']= "secret key"
db =SQLAlchemy(app)

@app.route('/')
def login():
    return render_template('login.html')