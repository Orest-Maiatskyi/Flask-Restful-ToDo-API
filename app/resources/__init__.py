from .auth_api import AuthTokenApi
from .todo_api import ToDoGetApi, ToDoListApi, ToDoCreateApi, ToDoUpdateApi, ToDoDeleteApi


api_route = ''


def init_api_routes(api):
    api.add_resource(AuthTokenApi, api_route + '/auth')
    api.add_resource(ToDoGetApi, api_route + '/todo/<public_id>')
    api.add_resource(ToDoListApi, api_route + '/todo/all')
    api.add_resource(ToDoCreateApi, api_route + '/todo/create')
    api.add_resource(ToDoUpdateApi, api_route + '/todo/update/<public_id>')
    api.add_resource(ToDoDeleteApi, api_route + '/todo/delete/<public_id>')
