import socket, json, ssl

class SocketConnector:
    def __init__(self, host, port, bufsize=4096, ca_certs=None):
        """
        Initializes a SocketConnector with the provided options

        @param host -- the host to connect to
        @param port -- the port to connect to
        @param bufsize -- the size of data allowed to be received (default 4096)
        @param ca_certs -- the certificate file to optionally encrypt the connection
        """
        self.address = (host, port)
        self.bufsize = bufsize
        self.ca_certs = ca_certs

    def send(self, data):
        """
        Sends the data to the server as a JSON string and returns the response.

        @param data -- a Python object to send as JSON

        @return (object|String) the response from the server as a Python object extracted from
            the JSON formatted string. If the response isn't a JSON string, returns the
            response
        """
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if self.ca_certs:
            sock = ssl.wrap_socket(sock, cert_reqs=ssl.CERT_REQUIRED, ca_certs=self.ca_certs)

        sock.connect(self.address)
        sock.send(json.dumps(data))
        response = sock.recv(self.bufsize)
        sock.close()
        try:
            return json.loads(response)
        except ValueError:
            return response

    @classmethod
    def send_to(cls, host, port, data, bufsize=4096):
        """
        Initializes a SocketConnector and sends the packet. Deletes the SocketConnector
        afterwards. Alias for:

        SocketConnector(host, port).send(data)
        """
        return cls(host, port, bufsize).send(data)