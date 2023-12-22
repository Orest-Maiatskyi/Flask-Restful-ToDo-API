import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', '100% later I will forget to update it ...')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=20)
    JWT_SECRET_KEY = '100% later I will forget to update it too ...'
    DEBUG = True


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '../database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


configs = dict(
    prod=ProdConfig,
)

current_config = configs.get('prod')
