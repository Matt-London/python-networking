import socket
from .Connection import Connection

class Server(Connection):
    """
    Server object to facilitate server connections
    """
    def __init__(self, ip="", port=0):
        """
        Constructor for Server objects

        :param: ip: IP to connect to
        :param: port: Port to connect to
        """
        # Construct using superclass
        super().__init__(ip, port)
    
    def bind(self):
        """
        Binds to whatever port was supplied on construction

        """
        # Binds to the port
        self.sock.bind((self.ip, self.port))

        # Allows given number of connections
        self.sock.listen(2)

        # Grabs connected addresses and new connection interface
        self.conn, self.addr = self.sock.accept()

    
    def send(self, msg=""):
        """
        Facilitates superclass send

        :param: msg: Message to send to the client
        """
        return super().send(self.conn, msg)


    def receive(self):
        """
        Calls superclass receive with interface

        """
        return super().receive(self.conn)

    def close(self):
        """
        Calls superclass close on connection
        """
        return super().close(self.conn)

