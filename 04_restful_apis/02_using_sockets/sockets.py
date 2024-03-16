import socket

server_addr = input("What server do you want to connect to? ")  # has to be a string website address
sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
sock.connect((server_addr, 80))  # 80 is the port number for HTTP
sock.send(b"GET / HTTP/1.1\r\nHost: " +
          bytes(server_addr, "utf8") +
          b"\r\nConnection: close\r\n" + 
          b"\r\n")
reply = sock.recv(10000) # 10000 is the max length of the reply's internal buffer
sock.shutdown(socket.SHUT_RDWR)
sock.close()
print(repr(reply))

"""  
potential run of script:

What server do you want to connect to?  www.site.com
b'HTTP/1.1 200 OK\r\nDate: Fri, 08 Mar 2019 08:24:41 GMT\r\nServer: UltraDNS Client Redirection Server\r\nLast-Modified: Fri, 08 Mar 2019 08:24:41 GMT\r\nAccept-Ranges: none\r\nConnection: close\r\nContent-Type: text/html\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n'

first line is the response header with code 200 (success)
after the header comes the document

on a connection error, the script will raise a socket.gaierror exception (get address info error)

on a timeout, the script will raise a socket.timeout exception

on a port of connection error, the script will raise a ConnectionRefusedError exception
"""