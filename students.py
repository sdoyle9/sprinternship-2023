from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

db = SQLAlchemy(app)

db_user = 'root'
db_pass = 'sprintern2023'
db_name = 'FieldApp'

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:sprintern2023@localhost/FieldApp"



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
    return render_template('home_page.html')
@app.route('/form')
def form():
    return render_template('form.html')

# @app.route("/map")
# def map():
#     return render_template('map.html')

if __name__ == '__main__':
    print("Loading configuration....")
    # Here, you can add code to actually load a configuration if you need to.
    print("Done loading configuration")
    app.run(debug = False)
    # app.run(debug=True)

    
#  *------------------------------------------------------------------*   

# python students.py