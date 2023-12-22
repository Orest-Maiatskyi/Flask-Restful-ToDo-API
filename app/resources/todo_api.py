from datetime import datetime

from flask import g, request
from flask_restful import Resource, abort

from app.database.dao.todo import TodoDAO
from app.utils.decorators import jwt_req
from app.utils.validator import Validator


class ToDoGetApi(Resource):

    @jwt_req
    def get(self, public_id):
        for todo in g.current_user.todos:
            if todo.public_id == public_id:
                return {'public_id': todo.public_id,
                        'title': todo.title,
                        'body': todo.body,
                        'is_done': todo.is_done,
                        'created_on': str(todo.created_on),
                        'expiration_time': str(todo.expiration_time)}, 200
        return {}, 204


class ToDoListApi(Resource):

    @jwt_req
    def get(self):
        json_todos = []
        for todo in g.current_user.todos:
            json_todos.append({'public_id': todo.public_id,
                               'title': todo.title,
                               'body': todo.body,
                               'is_done': todo.is_done,
                               'created_on': str(todo.created_on),
                               'expiration_time': str(todo.expiration_time)})
        if len(json_todos) > 0:
            return {'todos': json_todos}, 200
        return {}, 204


class ToDoCreateApi(Resource):

    @jwt_req
    def post(self):
        args = request.args
        title = args.get('title')
        body = args.get('body')
        is_done = args.get('is_done')
        expiration_time = args.get('expiration_time')

        if len(args) != 4 or title is None or body is None or is_done is None or expiration_time is None:
            abort(400, message='Bad request params.')

        Validator.validate_title(title)
        Validator.validate_body(body)
        Validator.validate_is_done(is_done)
        Validator.validate_expiration_time(expiration_time)

        TodoDAO.add_todo(title,
                         body,
                         int(is_done),
                         datetime.strptime(expiration_time, '%Y-%m-%d %H:%M:%S.%f'),
                         g.current_user.id)

        return {'message': 'Success'}, 200


class ToDoUpdateApi(Resource):

    @jwt_req
    def put(self, public_id):
        args = request.args
        title = args.get('title')
        body = args.get('body')
        is_done = args.get('is_done')
        expiration_time = args.get('expiration_time')

        if len(args) != 4 or title is None or body is None or is_done is None or expiration_time is None:
            abort(400, message='Bad request params.')

        Validator.validate_title(title)
        Validator.validate_body(body)
        Validator.validate_is_done(is_done)
        Validator.validate_expiration_time(expiration_time)

        current_todo = None
        for todo in g.current_user.todos:
            if todo.public_id == public_id:
                current_todo = todo
                break

        if current_todo is None:
            abort(404, message=f'No such todo with public_id: {public_id}')

        TodoDAO.update_todo(current_todo,
                            title,
                            body,
                            int(is_done),
                            datetime.strptime(expiration_time, '%Y-%m-%d %H:%M:%S.%f'))

        return {'message': 'Success'}, 200


class ToDoDeleteApi(Resource):

    @jwt_req
    def delete(self, public_id):
        current_todo = None
        for todo in g.current_user.todos:
            if todo.public_id == public_id:
                current_todo = todo
                break

        if current_todo is None:
            abort(404, message=f'No such todo with public_id: {public_id}')

        TodoDAO.delete_todo(current_todo)

        return {'message': 'Success'}, 200
