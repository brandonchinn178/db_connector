---
layout: default
title: DatabaseConnector
---

DatabaseConnector
=================

This class lets you query a connection without dealing with connection or cursor objects. Other database connections may be supported in later versions (PostgreSQL, SQLite, etc)

Usage
-----

The DatabaseConnector can be used as a regular object or as a context manager.

    from servconn import DatabaseConnector

    db = DatabaseConnector(host, username='test')
    db.execute('INSERT INTO table VALUES (1,2)')
    
    with DatabaseConnector(host) as db:
        db.query('SELECT * FROM table')

Class Methods
-------------

`servconn.DatabaseConnector([host, username, password, port, database])`

- Creates a DatabaseConnector object, connecting to the given host (localhost by default), optionally with the given username, password, port, or database.

Instance Variables
------------------

`DatabaseConnector.connection`

- The MySQL Connection object used to connect this object to the MySQL database.

`DatabaseConnector.c`

- The MySQL Cursor object used to execute queries.

Instance Methods
----------------

`query(query)`

- Returns the result of running the given query on the connection.

`execute(query)`

- Executes the query but doesn't return anything. Useful for INSERT or DROP operations.

`compute(query)`

- Returns the first row of the result of the running the query. Useful for SQL aggregate functions.

`close()`

- Closes the connection from any further queries.