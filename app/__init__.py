from flask import Flask
from flask_restful import Api

from .config import current_config
from .extensions import *
from .resources import init_api_routes

app = Flask(__name__)
app.config.from_object(current_config)
init_extensions(app)
api = Api(app)  # not in the extensions, cause: https://github.com/flask-restful/flask-restful/issues/644

from app.database.models import *

with app.app_context():
    db.create_all()

init_api_routes(api)
