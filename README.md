Database Connector
==================

This repository defines a class that allows the wrapping of a MySQL connection. This class lets you query a connection without dealing with connection or cursor objects. Other database connections may be supported in later versions (PostgreSQL, SQLite, etc)

Database Connector Object
-------------------------

### Usage

The DatabaseConnector can be used as a regular object or as a context manager. These are two valid ways to use a DatabaseConnector:

```
db = DatabaseConnector(host, username='test')
db.execute('INSERT INTO table VALUES (1,2)')

with DatabaseConnector(host) as db:
    db.query('SELECT * FROM table')
```

### Class Methods
- `DatabaseConnector.__init__(host, [username, password, port, database])`: creates a new DatabaseConnector object, connected to the MySQL server given in the host, optionally with the given username, password, port, and database.
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