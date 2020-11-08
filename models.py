import flask_sqlalchemy
from datetime import datetime
import flask
from enum import Enum
from app import db

class AppUser(db.Model):
    __tablename__ = 'appuser'
    id = db.Column(db.Integer, primary_key=True)

    # User Authentication fields
    email = db.Column(db.String(255), nullable=False, unique=True)

    username = db.Column(db.String(50), nullable=False)

    # User fields
    active = db.Column(db.Boolean()),
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    profile_pic = db.Column(db.String)
    events = db.relationship('Event', backref='auser', lazy=True)
    comments = db.relationship('Comment', backref='auser', lazy=True)
    
    def __init__(self,email, first_name, last_name, auth_type, profile_pic):
        assert isinstance(auth_type, AuthUserType)
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.profile_pic = profile_pic
        self.username = first_name + " " + last_name
        self.auth_type = str(auth_type)
        
    def activate(self):
        self.active = True
    def deactivate(self):
        self.active = False
        
    def is_authenticated(self):
        return self.active
        
    def set_username(self,username):
        self.username = username
    
    
    
class Event(db.Model):
    __tablename__ = 'event'
    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(85), nullable=False)
    description = db.Column(db.Text)
    date_published = db.Column(db.DateTime, nullable=False)
    views = db.Column(db.Integer)
    duration = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('appuser.id'),nullable=False)
    comments = db.relationship('Comment', backref="event", lazy=True)
    
    def __init__(self, name, description,duration, user_id):
        self.name = name
        self.description = description
        self.date_published = datetime.now()
        self.views = 0
        self.duration = duration
        self.description = description
        self.user_id = user_id
        
    
    
    
class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    
    text = db.Column(db.String(140), nullable=False)
    created_at = db.Column(db.DateTime)
    
    user_id = db.Column(db.Integer, db.ForeignKey('appuser.id'),nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'),nullable=False)
    
    def __init__(self,text,created_at,user_id,event_id):
        self.text = text
        self.created_at = datetime.now()
        self.user_id = user_id
        self.event_id = event_id
    
    
    
class AuthUserType(Enum):
    """Class that represents Types of AuthUsers"""

    GOOGLE = "google"
    FACEBOOK = "facebook"
    
    
    

    
    