from uuid import uuid4

from ..models import ToDo
from app import db
from ...utils.decorators import dao_error_handler


class TodoDAO:

    @staticmethod
    @dao_error_handler
    def add_todo(title, body, is_done, expiration_time, user_id):
        db.session.add(ToDo(public_id=str(uuid4()), title=title, body=body, is_done=is_done, expiration_time=expiration_time, user_id=user_id))
        db.session.commit()

    @staticmethod
    @dao_error_handler
    def update_todo(todo, title, body, is_done, expiration_time):
        todo.title = title
        todo.body = body
        todo.is_done = is_done
        todo.expiration_time = expiration_time
        db.session.commit()

    @staticmethod
    @dao_error_handler
    def delete_todo(todo):
        db.session.delete(todo)
        db.session.commit()
