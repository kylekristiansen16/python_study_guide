
""" high level: 
        - REST
        - JSON
        - XML
        - HTTP
        - CRUD
"""

""" the knowledge destination:
- the basic concepts of network programming, REST, network sockets, and client-server communication;
- how to use and create sockets in Python, and how to establish and close the connection with a server;
- what JSON and XML files are, and how they can be used in network communication;
- what HTTP methods are, and how to say anything in HTTP;
- how to build a sample testing environment;
- what CRUD is;
- how to build a simple REST client, and how to fetch and remove data from server, add new data to it, and update the already-existing data.
"""

""" REST
REpresentational
State
Transfer

REpresentational: 
- our machinery stores, transmits and receives representations
- data or states are retained inside the system and presented to the users
- the data is not the state, but the representation of the state

the data is always text - the data represents the state of the system

State:
not completely explained except for the following metaphor:
    Imagine any object. The object contains a set (the most preferable set is a non-empty one) of properties. We can say that the values of all
    the object's properties constitute its state. If any of the properties changes its value, this inevitably entails the effect of changing the 
    whole object's state. Such a change is often called a transition.
        aka... the `dir()` function would represent the "characteristics" of any object in Python
        then... the `__dict__` property contains the state of those `dir()` characteristics at a given point in time

    Now imagine that the object is stored somewhere else, not on your computer, but on a server located over the hill and far away. Of course, you 
    can access the server's resources using the network, but you can't just get the object and transfer it into your computer. Why not? Because it 
    has to be accessible to many (maybe a few, maybe a million) users. It must stay on the server.
        you can't get the physical entity 
        kind of like... how they won't send you the car when you're buying it online, they'll just let you know about the state of the car

    Imagine that you want to (or you must) affect the object's state through the network. No, you are not able to invoke any of its methods. Sorry, 
    that's impossible. You can't do it directly. But you can do it using REST.
        you're allowed to make requests over the network against the state of the object
        NOT the object itself
    
Transfer:
- The network (not only the Internet) is able to act as a carrier allowing you to transmit states' representations to and from the server.
- transferring the states enables you to achieve results similar to those caused by method invocations

"""

""" sockets
- socket is a kind of end-point, which is a point where the data is available to get it from and where the data may be sent to
- socket is a door, or a window, or a dock at a warehouse that a truck can use to load or unload its cargo

first socket from Berkeley
BSD (Berkeley Software Distribution) sockets
- BSD = name of unix-class operating system where the sockets were first implemented
- ultimately adopted by POSIX (Portable Operating System Interface - standard of contemporary unix-class operating systems)
"""