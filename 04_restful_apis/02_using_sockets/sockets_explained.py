
""" goals
    we want to write a program which reads the address of a WWW site (e.g., pythoninstitute.org) using the standard input() function and 
        fetches the root document (the main HTML document of the WWW site) of the specified site;
    the program outputs the document to the screen;
    the program uses TCP to connect to the HTTP server.

steps to follow:
    1 create a new socket able to handle connection-oriented transmissions based on TCP;
    2 connect the socket to the HTTP server of a given address;
    3 send a request to the server (the server wants to know what we want from it)
    4 receive the server's response (it will contain the requested root document of the site)
    5 close the socket (end the connection)
"""

# region 1. create a new socket able to handle connection-oriented transmissions based on TCP
import socket

server_addr = input("What server do you want to connect to? ")

""" 
server_addr can be 2 different things:
    it can be the domain name of the server (like www.pythoninstitute.org, but without the leading http://)
    it can be the IP address of the server (like 87.98.235.184), but it must be said firmly that this variant is potentially ambiguous. 
        Why? Because there can be more than one HTTP server located at the same IP address - the server you will reach may be not the server you intended to connect to.
"""

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
# socket.AF_INET = domain code (INET = Internet)
# socket.SOCK_STREAM = type code (STREAM = connection-oriented) - specify a high-level socket able to act as a character device (i.e., a stream of characters)
# it's the default socket configuration for TCP protocol

# endregion

# region 2. connect the socket to the HTTP server of a given address

sock.connect((server_addr, 80))
# connect() method takes one argument - a tuple containing the server's address and the port number
# port number is 80 because it's the standard port number for HTTP servers, default for internet connections

# endregion

# region 3. send a request to the server (the server wants to know what we want from it)

""" http protocol
HTTP defines a set of acceptable requests - these are the request methods or HTTP words
- method asking the server to send a particular document of a given name is called GET
- method asking the server to accept a document of a given name is called PUT
- method asking the server to delete a document of a given name is called DELETE
- method asking the server to send a list of all documents available on the server is called LIST

GET method requires...
    a line containing the method name (i.e., GET) followed by the name of the resource the client wants to receive; 
        the root document is specified as a single slash (i.e., `/`); the line must also include the HTTP protocol version (i.e., HTTP/1.1) and 
        must end with the characters \r\n; note: all lines must end the same way;
    a line containing the name of the site (e.g., www.site.com) preceded by the parameter name (i.e., Host:)
    a line containing a parameter named Connection: along with its value `close`, which forces the server to close the connection after the first request is served; 
        it will simplify our client's code;
    an empty line is a request terminator.
    
To get a root document from a site named www.site.com:
    GET / HTTP/1.1\r\n
    Host: www.site.com\r\n
    Connection: close\r\n
    \r\n
"""

sock.send(
    b"GET / HTTP/1.1\r\n" \
    b"Host: " + bytes(server_addr, "utf8") + b"\r\n" \
    b"Connection: close\r\n" \
    b"\r\n"
    )
# send() method is extremely complicated - it engages not only many layers of the OS, but also lots of network equipment deployed on the route 
# between the client and server, and obviously the server itself.

# endregion

# region 4.receive the server's response (it will contain the requested root document of the site)

reply = sock.recv(10000)
# receive max 10000 bytes of data from the socket
# data is returned as bytes

# endregion

# region 5. close the socket (end the connection)

sock.shutdown(socket.SHUT_RDWR)
# "We have no more to say to you. We don't want to hear from you, either. The rest is silence."
# socket.SHUT_RD - we aren't going to read the server's messages anymore (we declare ourselves deaf)
# socket.SHUT_WR - we won't say a word (actually, we'll be dumb)
# socket.SHUT_RDWR - specifies the conjunction of the two previous options.

sock.close()
print(repr(reply))

# endregion



