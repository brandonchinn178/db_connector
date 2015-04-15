---
layout: default
title: DatabaseConnector
---

DatabaseConnector
=================

This class lets you query a SQL database without dealing with connection or cursor objects. You must install the relevant Python packages in order to use the related DatabaseConnector: `mysql-python` for MySQL and `psycopg2` for PostgreSQL.

Usage
-----

The DatabaseConnector can be used as a regular object or as a context manager.

    from servconn import DatabaseConnector

    db = DatabaseConnector.connect_mysql(host, username='test')
    db.execute('INSERT INTO table VALUES (1,2)')
    
    with DatabaseConnector.connect_mysql(host) as db:
        db.query('SELECT * FROM table')

Class Methods
-------------

`DatabaseConnector(connection, cursor)`

- Creates a DatabaseConnector object with the given connection and cursor.

`DatabaseConnector.connect_mysql([host, username, password, port, database, **kwargs])`

- Connects to a MySQL server. Connects to localhost by default on port 3306, optionally with the given username, password, and database. Additional parameters will be passed into the connect function

`DatabaseConnector.connect_sqlite([database, **kwargs])`

- Connects to the SQLite database file provided. Defaults to the database in RAM. Additional parameters will be passed into the connect function

`DatabaseConnector.connect_postgres([host, username, password, port, database, **kwargs])`

- Connects to a PostgreSQL server. Connects to the Unix socket by default on port 5432, optionally with the given username, password, and database. Additional parameters will be passed into the connect function

`DatabaseConnector.connect_mssql([host, username, password, port, database, **kwargs])`

- Connects to a Microsoft SQL server. Connects to localhost by default on port 1433, optionally with the given username, password, and database. Additional parameters will be passed into the connect function

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

`query_column(query)`

- Returns the result of running the given query on the connection, but only returns the first column for every row. Useful for SELECT operations on only one column.

`execute(query)`

- Executes the query but doesn't return anything. Useful for INSERT or DROP operations.

`compute(query)`

- Returns the first row of the result of the running the query. Useful for SQL aggregate functions.

`close()`

- Closes the connection from any further queries.