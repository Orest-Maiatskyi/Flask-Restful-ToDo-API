import datetime

from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    registered_on = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)

    todos = db.relationship('ToDo', backref='user')
