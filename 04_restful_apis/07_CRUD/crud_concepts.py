
""" 
some context on rest:
    a properly trained web server can be a very effective and convenient gateway to very complicated and heavy 
    databases or other services designed for storing and processing information. Moreover, the structure of the 
    database (or the service) may vary, e.g., it may be a simple relational database residing in a single file, 
    or on the contrary, a huge, distributed cloud of cooperating servers; but the interface provided to the user 
    (you) will always look the same.

^ what REST was invented for. Thanks to it, very different programs written in very different technologies can utilize shared data through one, universal interface

CRUD:
    - Create - POST method - add new items to data collections
    - Read - GET method - browse data stored in a collection / read data from the server
    - Update - PUT method - modify the contents of the selected item without removing it from the collection
    - Delete - DELETE method - remove the selected item from the collection
"""

# run `json-server --watch cars.json` in the terminal to spin up a webserver

import requests
import json

try:
    reply = requests.get("http://localhost:3000/cars") # this will allow us to protect ourselves against the possible effects of connection problems
except requests.RequestException: # base exception in the requests module
    print("Communication error")
else:
    if reply.status_code == requests.codes.ok:
        print(reply.headers['Content-Type'])
        print(reply.json())
        print(reply.__dict__)
        # print(reply.text) # the response's contents are stored as a text property of the response object
    else:
        print("Server error")



