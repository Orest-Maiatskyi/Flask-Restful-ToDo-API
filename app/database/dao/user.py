from uuid import uuid4

from ..models import User
from app import db, bcrypt
from ...utils.decorators import dao_error_handler


class UserDAO:

    @staticmethod
    @dao_error_handler
    def is_email_unique(email):
        return False if User.query.filter_by(email=email).first() else True

    @staticmethod
    @dao_error_handler
    def get_user_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    @dao_error_handler
    def get_user_by_public_id(public_id):
        return User.query.filter_by(public_id=public_id).first()

    @staticmethod
    @dao_error_handler
    def add_user(email, password):
        db.session.add(User(public_id=str(uuid4()), email=email, password=bcrypt.generate_password_hash(password).decode('utf-8')))
        db.session.commit()

    @staticmethod
    @dao_error_handler
    def delete_user_by_public_id(public_id):
        db.session.delete(User.query.filter_by(public_id=public_id).one())
        db.session.commit()
