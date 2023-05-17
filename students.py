# import os
from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy

# from sqlalchemy.sql import func


# basedir = os.path.abspath(os.path.dirname(__file__))

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] =\
#         'sqlite:///' + os.path.join(basedir, 'database.db')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

app = Flask(__name__)
app.template_folder = 'templates'

@app.route("/")
def map():
    # you can change xxx.html
    return render_template('home_page.html')

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