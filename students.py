# from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime
# app = Flask(__name__)

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////Users/yufangyang/fieldapp.db"
# app.config['SECRET_KEY']= "secret key"
# db =SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)

# class Test(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), unique=True, nullable=False)

# @app.route("/")
# def map():
#     # you can change xxx.html
#     return render_template('savepage.html')
# @app.route('/form')
# def form():
#     return render_template('form.html')

# if __name__ == '__main__':
#     print("Loading configuration....")
#     # Here, you can add code to actually load a configuration if you need to.
#     print("Done loading configuration")
#     with app.app_context():
#         db.create_all()
#     app.run(debug = False)
#     # app.run(debug=True)

    
#  *------------------------------------------------------------------*   
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from views import home, login, map_page, savepage

app = Flask(__name__)

<<<<<<< HEAD
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////Users/yufangyang/fieldapp.db"
app.config['SECRET_KEY']= "secret key"
db =SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(120), nullable=False)
    salary = db.Column(db.Float, nullable=False)

=======
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////Users/meleenatorres/FieldApp.db"
app.config['SECRET_KEY']= "secret key"
db =SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)

@app.route("/")
def map():
    # you can change xxx.html
    return render_template('login.html')
@app.route('/form')
def form():
    return render_template('form.html')
>>>>>>> 672ed60c7d18494e2a7612cc1d3880d0aa772356

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

app.add_url_rule('/', 'home', home)
app.add_url_rule('/login', 'login', login)
app.add_url_rule('/map', 'map_page', map_page)
app.add_url_rule('/savepage', 'savepage', savepage)

<<<<<<< HEAD
if __name__ == '__main__':
    with app.app_context():
        db.drop_all()  # Drop all existing tables
        db.create_all()  # Create new tables according to the current models
    app.run(debug=False)
=======
# python students.py
>>>>>>> 672ed60c7d18494e2a7612cc1d3880d0aa772356
