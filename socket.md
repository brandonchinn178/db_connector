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

`SocketConnector(host, port[, bufsize=4096, ca_certs=None, delimiter='$'])`

- Creates a new SocketConnector object that will connect to the given host and port. Various options may also be specified (see instance variables)

`SocketConnector.send_to(host, port, data, **kwargs)`

- Creates a SocketConnector object and sends the given data to the given host and port. Useful for one-time connections.

Instance Variables
------------------

`SocketConnector.host`

- The host to connect to

`SocketConnector.port`

- The port to connect to

`SocketConnector.bufsize`

- The maximum amount of data allowed to be received at once through this socket (by default 4096)

`SocketConnector.ca_certs`

- The file path to an SSL certificate. Set to enable encrypted connections (by default None)

`SocketConnector.delimiter`

- The delimiter used for the `sendall` function. Messages will continue to be received until this delimiter is reached in the message string (by default '$')

Instance Methods
----------------

`send(data)`

- Sends the provided data over the socket as a JSON-formatted string. Returns the response up to the bufsize.

`sendall(data)`

- Sends the provided data over the socket as a JSON-formatted string. Receives data until the delimiter is reached, then returns the response.
