# Flask RESTful ToDo API
#### ToDo API created with Flask-RESTful extension

---

### Quick API overview

The API includes basic authentication capabilities such as <b><i>registration</i></b>, 
<b><i>login</i></b> and <b><i>account deletion</i></b>. In turn, the user can <b><i>create</i></b>, 
<b><i>edit</i></b> and <b><i>delete</i></b> notes, it is also possible to <b><i>get 
a note by UUID</i></b> or <b><i>get all current notes</i></b>.

> [!NOTE]
> A more detailed description of the API can be found in the root of the project in the form of swagger documentation :
> `openapi.json`, `openapi.yaml` (For convenience, the documentation is presented in two formats)

<br>

### Authentication issues :(

Out of the box, <b><i>API does not provide any mechanism for saving and updating user tokens</i></b>, 
flask-jwt-extended offers [different options for solving this problem](https://flask-jwt-extended.readthedocs.io/en/stable/refreshing_tokens.html#), 
you can choose any of them or come up with something of your own ;)

<br>

### How to start using API ...?

1. Install [Python version 3.7](https://www.python.org/downloads/release/python-370/), 
create virtual environment and install all dependencies from `requirements.txt`.

> [!NOTE]
> You can use newer versions of Python, but do not forget to update the versions of the modules in requirements.txt 
> since they are designed specifically for Python version 3.7.

2. To run flask server run `entry.py`. First start will create `database.db`.
By default, API uses SQLite3 database and places it in the root folder.
You can use any other databases, as long as they are compatible with SQLALCHEMY. 
All you need to do is install the necessary driver for the database and slightly 
change the connection string in `app/config.py`. For example, you can use 
[MysQL](https://stackoverflow.com/questions/29355674/how-to-connect-mysql-database-using-pythonsqlalchemy-remotely) or 
[PostgreSQL](https://docs.sqlalchemy.org/en/20/core/engines.html#postgresql)

> [!CAUTION]
> Don't forget to change all the secret keys located in `app/config.py`!
