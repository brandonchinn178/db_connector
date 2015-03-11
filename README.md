ServConn
========

This repository defines classes that wrap connections to certain servers. The current classes defined are:
- DatabaseConnector: a class that wraps a MySQL connection
- SocketConnector: a class that wraps a socket connection

Development
-----------

To develop, use the following to setup your environment

1. (optional) Setup a virtual environment with virtualenv
2. Install pip
3. `pip install -r requirements.txt`

Installing
----------

To install this package, either run `python setup.py install` from this project or call `pip install servconn`.

DatabaseConnector
-----------------

This class lets you query a connection without dealing with connection or cursor objects. Other database connections may be supported in later versions (PostgreSQL, SQLite, etc)

### Usage

The DatabaseConnector can be used as a regular object or as a context manager.

```
from servconn import DatabaseConnector

db = DatabaseConnector(host, username='test')
db.execute('INSERT INTO table VALUES (1,2)')

with DatabaseConnector(host) as db:
    db.query('SELECT * FROM table')
```

### Class Methods
- `DatabaseConnector.__init__([host, username, password, port, database])`: creates a new DatabaseConnector object. Connects to localhost by default, optionally with the given username, password, port, and database.
- `DatabaseConnector.__del__()`: closes the connection before this object is deleted.
- `DatabaseConnector.__enter__()`: allows a DatabaseConnector to be used as a context manager
- `DatabaseConnector.__exit__()`: closes the connection on exit as a context manager

### Instance Variables
- `DatabaseConnector.connection`: the MySQL Connection object
- `DatabaseConnector.c`: the MySQL Cursor object

### Instance Methods
- `query(query)`: Returns the result of running the given query on the connection
- `execute(query)`: Executes the query but doesn't return anything. Useful for INSERT or DROP operations
- `compute(query)`: Returns the first row of the result of the running the query. Useful for SQL aggregate functions
- `close()`: Closes the connection from any further queries

SocketConnector
---------------

This class lets you send and receive JSON packets to the provided server.

### Usage

The SocketConnector can be used as a regular object or as a context manager.

```
from servconn import SocketConnector

socket = SocketConnector(host, port)
data = {
    'hello': 'world'
}
response = socket.send(data)

with SocketConnector(host, port) as socket:
    socket.send(data)
```