import re
from datetime import datetime

from flask_restful import abort


class Validator:

    @staticmethod
    def validate_email(email):
        if not re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', email):
            abort(422, message='Incorrect email.')

    @staticmethod
    def validate_password(password):
        # Minimum eight characters, at least one letter, one number and one special character
        if not re.fullmatch(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$', password):
            abort(422, message='Incorrect password.')

    @staticmethod
    def validate_title(title):
        if not re.fullmatch(r'^[A-Za-zА-Яа-я0-9 _-]*$', title):
            abort(422, message='Incorrect title.')

    @staticmethod
    def validate_body(body):
        if not re.fullmatch(r'^[A-Za-zА-Яа-я0-9 _-]*$', body):
            abort(422, message='Incorrect body.')

    @staticmethod
    def validate_is_done(is_done):
        if is_done not in [1, 0, '1', '0']:
            abort(422, message='Incorrect done status.')

    @staticmethod
    def validate_expiration_time(expiration_time):
        try:
            datetime.strptime(expiration_time, '%Y-%m-%d %H:%M:%S.%f')
        except Exception:
            abort(422, message='Incorrect expiration date.')
