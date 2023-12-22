from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
bcrypt = Bcrypt()


def init_extensions(app):
    db.init_app(app)
    bcrypt.init_app(app)
