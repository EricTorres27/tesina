from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class UserSession(db.Model):
    __tablename__ = 'user_session'
    user_Id= db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    session_Id= db.Column(db.Integer, db.ForeignKey('session.id'), primary_key=True)

class Session(db.Model):
    __tablename__ = 'session'
    id = db.Column(db.Integer, primary_key=True)
    q1= db.Column(db.Integer)
    q2= db.Column(db.Integer) 
    q3= db.Column(db.Integer)
    q4= db.Column(db.Integer)
    q5= db.Column(db.Integer)
    q6= db.Column(db.Integer)
    date= db.Column(db.DateTime(timezone=True), default=func.now())
    users= db.relationship("User", secondary="user_session", back_populates="sessions")
    
class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(100))
    users = db.relationship('User', backref='role', lazy=True)

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id= db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'),nullable=False)
    idNumber= db.Column(db.String(100))
    fullName= db.Column(db.String(100))
    password= db.Column(db.String(100))
    sessions= db.relationship("Session", secondary="user_session", back_populates="users")

    
