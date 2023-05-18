from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)



db_user = 'root'
db_pass = 'sprintern2023'
db_name = 'FieldApp'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:sprintern2023@localhost/FieldApp"
app.config['SECRET_KEY']= "secret key"
db =SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    

def __repr__(self):
        return '<User %r>' % self.username
    
    
app.template_folder = 'templates'





@app.route("/")
def map():
    # you can change xxx.html
    return render_template('login.html')
@app.route('/form')
def form():
    return render_template('form.html')

# @app.route("/maep")
# def map():
#     return render_template('map.html')

if __name__ == '__main__':
    print("Loading configuration....")
    # Here, you can add code to actually load a configuration if you need to.
    print("Done loading configuration")
    db.create_all()
    app.run(debug = False)
    # app.run(debug=True)

    
#  *------------------------------------------------------------------*   

# python students.py