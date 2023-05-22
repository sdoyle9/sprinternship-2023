from flask import Flask
from views import db 
from flask_sqlalchemy import SQLAlchemy



class MyModel(db.Model):
    project = db.Column(db.String(150), nullable = False, unique = True)
    
    def __repr__(self):
        return '<Name %r>' % self.name
    