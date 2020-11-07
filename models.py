import flask_sqlalchemy
from datetime import datetime
from enum import Enum
from app import db

class AppUser(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)

    # User Authentication fields
    email = db.Column(db.String(255), nullable=False, unique=True)

    username = db.Column(db.String(50), nullable=False)

    # User fields
    active = db.Column(db.Boolean()),
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    profile_pic = db.Column(db.String)
    comments = db.relationship('comment', backref='user', lazy=True)
    
    
    
class Event(db.Model):
    __tablename__ = 'event'
    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(85), nullable=False)
    description = db.Column(db.Text)
    date_published = db.Column(db.DateTime, nullable=False)
    views = db.Column(db.Integer)
    duration = db.Column(db.Integer)
    comments = db.relationship('comment', backref='event', lazy=True)
    
    
    
class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'),nullable=False)
    
class AuthUserType(Enum):
    """Class that represents Types of AuthUsers"""

    GOOGLE = "google"
    FACEBOOK = "facebook"
    
    
    

    
    