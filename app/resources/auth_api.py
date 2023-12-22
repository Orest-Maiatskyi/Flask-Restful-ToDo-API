from datetime import datetime

import jwt
from flask import request, jsonify
from flask_restful import Resource, abort

from app import bcrypt
from app.database.dao.user import UserDAO
from app.utils.decorators import jwt_req
from app.utils.validator import Validator

import app


class AuthTokenApi(Resource):

    def get(self):
        args = request.args
        email = args.get('email')
        password = args.get('password')

        if len(args) != 2 or email is None or password is None:
            abort(400, message='Bad request params.')
        Validator.validate_email(email)
        Validator.validate_password(password)

        user = UserDAO.get_user_by_email(email)
        if user is None:
            abort(401, message='Incorrect email.')

        if not bcrypt.check_password_hash(user.password, password):
            abort(401, message='incorrect password.')

        return {'auth-token': jwt.encode({
            'public_id': user.public_id,
            'exp': datetime.utcnow() + app.app.config['JWT_ACCESS_TOKEN_EXPIRES']
        }, app.app.config['JWT_SECRET_KEY'])}, 200

    def post(self):
        args = request.args
        email = args.get('email')
        password = args.get('password')

        if len(args) != 2 or email is None or password is None:
            abort(400, message='Bad request params.')
        Validator.validate_email(email)
        Validator.validate_password(password)

        if not UserDAO.is_email_unique(email):
            abort(409, message='This email is already registered.')

        UserDAO.add_user(email, password)

        return {'message': 'Successful registration.'}, 201

    @jwt_req
    def delete(self):
        args = request.args
        email = args.get('email')
        password = args.get('password')

        if len(args) != 2 or email is None or password is None:
            abort(400, message='Bad request params.')
        Validator.validate_email(email)
        Validator.validate_password(password)

        user = UserDAO.get_user_by_email(email)
        if user is None:
            abort(401, message='Incorrect email.')

        if not bcrypt.check_password_hash(user.password, password):
            abort(401, message='incorrect password.')

        UserDAO.delete_user_by_public_id(user.public_id)

        return {'message': 'Account successfully deleted.'}, 200
