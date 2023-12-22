from datetime import datetime
from typing import Callable

import jwt
from flask import request, g
from flask_restful import abort
from sqlalchemy import exc

import app
from app.database.dao import user


# catch any sqlalchemy exceptions, log them than abort with status code 500
def dao_error_handler(func: Callable):

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except exc.SQLAlchemyError as e:
            with open('errors.log', 'a') as log_file:
                log_file.write(datetime.now().strftime('%m/%d/%Y, %H:%M:%S') + ' ' + str(func) + '\n' + str(e) + '\n')
            abort(500, message='Internal Server Error.')

    return wrapper


# checking for jwt token
def jwt_req(func: Callable):

    def wrapper(*args, **kwargs):
        token = request.cookies.get('auth-token')
        if token is None:
            return {'message': 'Auth token required.'}, 401
        try:
            current_user = user.UserDAO.get_user_by_public_id(
                jwt.decode(token, app.app.config['JWT_SECRET_KEY'], algorithms=['HS256'])['public_id'])
            if current_user is None:
                return {'message': 'Auth token is invalid.'}, 401
            g.current_user = current_user
            return func(*args, **kwargs)
        except jwt.exceptions.PyJWTError:
            return {'message': 'Auth token is invalid.'}, 401

    return wrapper
