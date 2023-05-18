from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Thundermandy12!@127.0.0.1/fieldapp"
app.config['SECRET_KEY']= "secret key"
db =SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

@app.route("/")
def map():
    # you can change xxx.html
    return render_template('savepage.html')
@app.route('/form')
def form():
    return render_template('form.html')

if __name__ == '__main__':
    print("Loading configuration....")
    # Here, you can add code to actually load a configuration if you need to.
    print("Done loading configuration")
    with app.app_context():
        db.create_all()
    app.run(debug = False)
    # app.run(debug=True)

    
#  *------------------------------------------------------------------*   

# python students.py