from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template
from datetime import datetime
from __init__ import app

views = Blueprint('views', __name__)

@views.route('/')
def main():
    return render_template('login.html')

@views.route('/login')
def login():
    return render_template('login.html')

@views.route('/home')
def home():
    return render_template('home_page.html')

@views.route('/map')
def map_page():
    return render_template('map.html')

@views.route('/savepage')
def savepage():
    return render_template('savepage.html')


#  *------------------------------------------------------------------*   Lily 

# from flask import render_template

# def home():
#     return render_template('home_page.html')

# def login():
#     return render_template('login.html')

# def map_page():  
#     return render_template('map.html')

# def savepage():
#     return render_template('savepage.html')
#  *------------------------------------------------------------------*   END Lily 
