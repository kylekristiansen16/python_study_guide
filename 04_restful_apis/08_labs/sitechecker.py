
""" 
We want you to write a simple CLI (Command Line Interface) tool which can be used in order to diagnose the current 
status of a particular http server. The tool should accept one or two command line arguments:
- (obligatory) the address (IP or qualified domain name) of the server to be diagnosed (the diagnosis will be extremely 
    simple, we just want to know if the server is dead or alive)
- (optional) the server's port number (any absence of the argument means that the tool should use port 80)
    use the HEAD method instead of GET — it forces the server to send the full response header but without any content; it's 
    enough to check if the server is working properly; the rest of the request remains the same as for GET.
    We also assume that:

the tool checks if it is invoked properly, and when the invocation lacks any arguments, the tool prints an error message 
and returns an exit code equal to 1;
if there are two arguments in the invocation line and the second one is not an integer number in the range 1..65535, the 
tool prints an error message and returns an exit code equal to 2;
if the tool experiences a timeout during connection, an error message is printed and 3 is returned as the exit code;
if the connection fails due to any other reason, an error message appears and 4 is returned as the exit code;
if the connection succeeds, the very first line of the server’s response is printed.
Hints:

- to access command line arguments, use the argv variable from the sys module; its length is always one more than the actual 
    number of arguments, as argv[0] stores your script's name; this means that the first argument is at argv[1] and the second 
    at argv[2]; don't forget that the command line arguments are always strings!
- returning an exit code equal to n can be achieved by invoking the exit(n) function.

Assuming that the tool is placed in a source file name sitechecker.py, here are some real-use cases:
"""

import sys
import socket

if len(sys.argv) not in [2,3]:
    print("Error: impropert number of args: at least one is required and not more than two are allowed")
    print("\trequired: server HTTP address")
    print("\toptional: server port number (default: 80)")
    sys.exit(1)
    
script = sys.argv[0]
server = sys.argv[1]
port = 80
if sys.argv[2:] and sys.argv[2].isdigit() and int(sys.argv[2]) in range(1,65536):
        port = int(sys.argv[2])

server_ipv4 = socket.gethostbyname(server)

try:
    with socket.create_connection((server, port), timeout=5) as conn:
        conn.sendall(b"HEAD / HTTP/1.1\r\nHost: " + bytes(server, "utf8") + b"\r\n\r\n")
        data = conn.recv(1024)
        print(data.decode())
except socket.timeout:
    print("Error: connection timeout")
    sys.exit(1)
except socket.gaierror:
    print("Error: get address info error")
    sys.exit(1)

sys.exit(0)