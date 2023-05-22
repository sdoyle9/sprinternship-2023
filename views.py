from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)

def home():
    return render_template('home_page.html')

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Thundermandy12!@127.0.0.1/fieldapp"
app.config['SECRET_KEY']= "secret key"
db =SQLAlchemy(app)

@app.route('/')
def main_index():
    return "Blueprint hello!"


#  *------------------------------------------------------------------*   Lily code

from flask import render_template

def home():
    return render_template('home_page.html')

def login():
    return render_template('login.html')

def map_page():  
    return render_template('map.html')

def savepage():
    return render_template('savepage.html')
#  *------------------------------------------------------------------*   END Lily code