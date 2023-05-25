from __init__ import db
from enum import Enum

class CategoryEnum(Enum):
    OPTION1 = 'Environmental Resources,'
    OPTION2 = 'Municipal Engineering'
    OPTION3 = 'Transportation'
    OPTION4= 'Water Resources'
    
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    number = db.Column(db.Integer,nullable =False)
    category = db.Column(db.Enum(CategoryEnum), nullable=False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    notes = db.Column(db.Text)
    
class Perimeter(db.Model):
    id = db.Column(db.Float, primary_key=True)
    lat1= db.Column(db.Float, nullable=False)
    long1= db.Column(db.Float, nullable=False)
    lat2= db.Column(db.Float, nullable=False)
    long2= db.Column(db.Float, nullable=False)
    lat3= db.Column(db.Float, nullable=False)
    long3= db.Column(db.Float, nullable=False)
    lat4= db.Column(db.Float, nullable=True)
    long4= db.Column(db.Float, nullable=True)
    lat5= db.Column(db.Float, nullable=True)
    long5= db.Column(db.Float, nullable=True)
    lat6= db.Column(db.Float, nullable=True)
    long6= db.Column(db.Float, nullable=True)

    