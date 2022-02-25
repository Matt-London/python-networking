import socket

class Connection(object):
    """
    Parent class for Client and server objects to handle the
    transmissions that are the same


    """

    def __init__(self, ip="", port=0):
        """
        Constructor for Connection

        :param: self: Self object to build
        :param: ip: The ip used in the connection
        :param: port: The port used in the connection
        """
        # Construct the object
        self.ip = ip
        self.port = port
        self.sock = socket.socket()
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def send(self, interface, msg="") -> int:
        """
        Transmits data to saved port using given interface from child

        :param: self: Containing object
        :param: interface: Interface passed by children
        :param: msg: Message to transmit
        """
        try:
            # Return result of sending msg
            return interface.sendall(msg.encode())
        
        except Exception as e:
            # Return false if it fails
            print(e)
            return -1

    # Reads outstanding data on the port
    def receive(self, interface) -> str:
        """
        Receives data on the interface and then hands it off

        :param: interface: Interface to listen on
        """
        try:
            # Returns the data if successful
            ## Loops through and ensures transmission is complete
            data = str(interface.recv(1024).decode("ascii"))
            
            return data

        except Exception as e:
            # Throws error and returns false if exception is raised
            print(e)
            return ""

    # Closes the open connection
    def close(self, interface) -> bool:
        """
        Closes the interface
        
        :param: interface: Interface to close
        """
        try:
            interface.close()
            return True
        
        except Excetion as e:
            print(e)
            return False

