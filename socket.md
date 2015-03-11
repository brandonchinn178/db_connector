---
layout: default
title: SocketConnector
---

SocketConnector
===============

This class lets you send and receive JSON packets to the provided server.

Usage
-----

The SocketConnector is used as a regular Python object.

    from servconn import SocketConnector

    socket = SocketConnector(host, port)
    data = {
        'hello': 'world'
    }

    response = socket.send(data)

Class Methods
-------------

`SocketConnector.__init__(host, port[, bufsize=4096])`

- Creates a SocketConnector object that will send packets to the given host and port. The bufsize may also be specified (default 4096).

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