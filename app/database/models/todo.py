import datetime

from app import db


class ToDo(db.Model):
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String, nullable=False, unique=True)
    title = db.Column(db.String, nullable=False)
    body = db.Column(db.Text, nullable=False)
    is_done = db.Column(db.Boolean, default=True, nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)
    expiration_time = db.Column(db.DateTime, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
