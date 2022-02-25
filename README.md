# Python Networking
This is a simple wrapper essentially for the socket library. It boils down to send
and receive rather than worrying about setup and byte counts

## Importing
To import this module, make sure the networking package is in the current directory.
Run the following either in a Python interpreter or in a Python program
```python
>>> from networking.Server import Server # Import the server module
>>>
>>> from networking.Client import Client # Import the client module
```

## Setting up the connection
Create both objects, likely on different computers
Creating the server object on the server (ip, port):

```python
>>> port = 4444 # Change this to desired port
>>> s = Server("127.0.0.1", port) # Open port 4444 on local loopback
```

Creating the client object (ip, port):

```python
>>> ip = "192.168.1.12" # Change this to desired ip
>>> port = 4444 # Change this to desired port
>>> c = Client(ip, port)
```

## Establishing the connection
On the server open the port first:
```python
>>> s.bind()
```

NOTE: This will hang until a connection is made from a client

On the client, connect to the port:
```python
>>> c.connect()
```

The TCP connection is now completed

## Sending data
From either client or server:
Use .send(str) to send information and .receive() to receive it

For example:
On the server
```python
>>> s.send("This is a test")
```

On the client
```python
>>> c.receive()
'This is a test'
```

NOTE: .receive() will hang until data is received

## Contributing
If you would like to contribute, you may make a pull request. It will be helpful if you first open an issue describing the change that you are interested in contributing.

## License
[MIT](https://choosealicense.com/licenses/mit/)

