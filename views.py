from flask import render_template

def home():
    return render_template('home_page.html')

def login():
    return render_template('login.html')

def map_page():  
    return render_template('map.html')

def savepage():
    return render_template('savepage.html')
