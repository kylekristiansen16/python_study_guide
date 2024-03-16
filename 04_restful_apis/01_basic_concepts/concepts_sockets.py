""" 
socket domains
- organized communication in 2 domains:
    - unix domain - within one operating system
    - internet domain - (INET) - between different operating systems connected using TCP/IP network (Internet)
    
socket address
- socket address = IP address (of computer sys) + port number (or service number) (this is for INET domain)
    ex. localhost:8080

ip address
- IP address (more precisely: IP4 address) is a 32-bit long value used to identify computers connected to any TCP/IP network
- reason for 32-bit: made up of 4 numbers between 0..255, each of which is an 8-bit value (byte) 
    2^32 = 4,294,967,296 (number of unique addresses)
- IPv6 is newer standard using 128 bits but not yet widely used (less than 20% of computers in the world are reachable by IP6)
    (2^128 = 340,282,366,920,938,463,463,374,607,431,768,211,456 unique addresses)
    
IPv4 IS PREDOMINANTLY USED

socket/service number (port number)
- port number is a 16-bit long value used to identify a socket within a particular system (can think of as a specific service running on a computer)
    65,536 (2 ** 16) possible socket/service numbers
- many standard network services usually use the same, constant socket numbers e.g., 
    the HTTP protocol, a carrier of data used by REST, usually uses port 80.
    hasura 8080
    postgres 5432

protocol
- a standardized set of rules allowing processes to communicate with each other

protocol stack
- a multilayer (hence the name) set of cooperating protocols providing a unified repertoire of services. 
- The TCP/IP protocol stack is designed to cooperate with networks based on the IP protocol (the IP networks).
- the most basic, elementary services are located at the bottom of the stack, while the most advanced and abstractive lie on the top.

IP (Internet Protocol)
- one of the lowest parts of TCP/IP protocol stack. Its functionality is very simple - it is able to send a packet of data (a datagram) between two network nodes.
- doesn't guarantee that:
    any of the sent datagrams will reach the target (moreover, if any of the datagrams is lost, it may remain undetected)
    the datagram will reach the target intact;
    a pair of sent datagrams will reach the target in the same order as they were sent.
- this is the job of the higher-level protocols (TCP, UDP)

|
V

UDP (User Datagram Protocol)
- higher part of TCP/IP protocol stack, but lower than the TCP
- It doesn't use handshakes, which has two serious consequences:
    it is faster than TCP (due to fewer overheads)
    it is less reliable than TCP.
UDP is not a connection-oriented protocol, which means that the communication channel doesn't have to be established before any data can be sent.

|
V

TCP (Transmission Control Protocol)
- datagrams (provided by the lower layers)
- handshakes (an automated process of synchronizing the flow of data)
- highest part of the TCP/IP protocol stack. It uses datagrams and handshakes to construct a reliable communication channel able to transmit and receive single characters. 
guarantees that:
    a stream of data reaches the target, or the sender is informed that communication has failed;
    data reaches the target intact.
TCP is a connection-oriented protocol, which means that the communication channel must be established before any data can be sent.
"""


# ** The key to this equation: **
# - TCP is a first-choice protocol for applications where data safety is more important that efficiency (e.g., WWW, REST, mail transfer, etc.)
# - UDP is more adequate for applications where response time is crucial (DNS, DHCP, etc.)



""" connections
connection-oriented communication - 
- Usually, both parties involved in the process aren't symmetrical i.e., their roles and routines are different. Both sides of the communication are aware that the other party is connected.
- A phone call is a perfect example of connection-oriented communication.
    the roles are strictly defined: there is a caller and there is a callee;
    the caller must dial the callee's number and wait till the network routes the connection;
    the caller must wait for the callee to answer the call (the callee may reject the connection, or just not answer the call)
    the actual communication won't start until all the previous steps are completed successfully;
    the communication ends when either of the parties hangs-up.
- TCP/IP networks use the following names for both sides of the communication and are used for connection-oriented communication  
    client = side that initiates the connection (caller)
    server =  side that answers the client (callee)

connectionless communication -
- can be established ad-hoc, without any preliminary actions, both parties usually have equal rights and are unaware of the other sides state.
- Using walkie-talkies is a very good analogy for connectionless communication, because:
    either of the parties of communication may initiate the communication at any time; it only requires pushing the talk button;
    talking to the mic doesn't guarantee that anybody will hear (it’s necessary to wait for an incoming answer to be sure)
- UDP is a connectionless protocol, and the parties of communication are called peers.
"""