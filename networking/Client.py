import socket
from .Connection import Connection

class Client(Connection):
    """
    Child to facilitate the client of the connection

    """
    def __init__(self, ip="", port=0):
        """
        Constructor for the client side of the connection

        :param: ip: IP to connect to
        :param: port: Port to connect to
        """
        # Calls superclass constructor
        super().__init__(ip, port)
    
    def connect(self):
        """
        Call superclass connect with the given info
        """
        return self.sock.connect((self.ip, self.port))
    
    def send(self, msg=""):
        """
        Call superclass send to send the given data

        :param: msg: The message to send to server
        """
        return super().send(self.sock, msg)
    
    def receive(self):
        """
        Call superclass receive to return data
        """
        return super().receive(self.sock)
    
    def close(self):
        """
        Close the open connections
        """
        return super().close(self.sock)

