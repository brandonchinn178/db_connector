---
layout: default
title: SocketConnector
---

SocketConnector
===============

This class lets you send and receive JSON packets to the provided server.

Usage
-----

The SocketConnector is used as a regular Python object. Data can also be sent via the class method `send_to` for one-time connections.

    from servconn import SocketConnector

    socket = SocketConnector(host, port)
    data = {
        'hello': 'world'
    }

    response = socket.send(data)
    response = SocketConnector.send_to(host, port, data)

Class Methods
-------------

`SocketConnector(host, port[, bufsize=4096])`

- Creates a SocketConnector object that will send packets to the given host and port. The bufsize may also be specified (default 4096).

`SocketConnector.send_to(host, port, data[, bufsize=4096])`

- Creates a SocketConnector object and sends the given data to the given host and port. Useful for one-time connections.

Instance Variables
------------------

`SocketConnector.host`

- The host of the address to send packets to.

`SocketConnector.port`

- The port of the address to send packets to.

`SocketConnector.bufsize`

- The maximum amount of data allowed to be received at once through this socket.

Instance Methods
----------------

`send(data)`

- Sends the provided data over the socket as a JSON-formatted string