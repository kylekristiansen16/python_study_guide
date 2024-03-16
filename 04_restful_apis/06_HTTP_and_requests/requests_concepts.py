
""" 
we need a server serving a web service AND
we also need a tool simpler than the socket module to talk with the service
- socket is too bloated and too heavy when you just want to have a little chat with a web service
- it's good for low-level communication, but it's not the best choice for a higher level of abstraction

need a server: json-server, implemented on top of the Node.js environment
- node.js = an open-source, cross-platform JavaScript run-time environment that executes JavaScript code outside of a browser

npm = Node.js Package Manager

3000 (json-server's default port)

HTTP = HyperText Transfer Protocol
"""

import requests

reply = requests.get('http://localhost:3000/cars')
print(reply.status_code)
# the HTTP method is a two-way interaction between the client and the server dedicated to the execution of a certain action
# note: the client initiates the transmission
# GET = the client asks the server to send some data
# only details we need to provide are the server’s address and the service port number
# when server not local, server address would be formed as an IP address or fully qualified domain name (FQDN)

# remember server address & port! that's the key to internet communication and making successful call to a web service on a server

# HTTP status codes: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

print()

# print(requests.codes.__dict__) # see all status codes
# use dictionary to write human readable code:
if reply.status_code == requests.codes.ok:
    print('everything is fine!')

print()

# server's response consists of two parts: the header and the contents
from pprint import pprint
pprint(f'headers: \n{reply.headers}')
print()
pprint(f"content type: {reply.headers['Content-Type']}") # very important! tells server / requestor what kind of data is being sent
print()
pprint(f'content: \n{reply.text}')

""" other methods
POST (create)
- like GET, is used to transfer a resource, but in the opposite direction: from the client to the server; 
- just like in GET, the identification of the resource has to be given (the server wants to know what to name the piece of information it has received); 
- it is also assumed that the resource the client sends is new to the server – it doesn't replace or overwrite any of the previously collected data;

PUT (update)
- PUT, similarly to POST, transfers a resource from the client to the server, 
- but the intention is different – the resource being sent is intended to replace the previously stored data;

DELETE (delete)
– this name leaves no doubt: it is used to order the server to remove a resource from a given identification; the resource is unavailable from then on;

other methods: HEAD, OPTIONS, TRACE, CONNECT
"""

print()

# exceptions
try:
    reply = requests.get('http://localhost:3000', timeout=0.00001)
except requests.exceptions.Timeout:
    print('Sorry, you didn\'t get your data')
else:
    print('Here is your data!')
    
try:
    reply = requests.get('http://localhost:3001', timeout=1)
except requests.exceptions.ConnectionError:
    print('Nobody\'s home, sorry!')
else:
    print('Everything fine!')

try:
    reply = requests.get('http:////////////')
except requests.exceptions.InvalidURL:
    print('Recipient unknown!')
else:
    print('Everything fine!')
    
""" requests.exceptions tree 
RequestException
|___HTTPError
|___ConnectionError
|   |___ProxyError	
|   |___SSLError	
|___Timeout
|   |___ConnectTimeout
|   |___ReadTimeout
|___URLRequired
|___TooManyRedirects
|___MissingSchema
|___InvalidSchema
|___InvalidURL
|   |___InvalidProxyURL
|___InvalidHeader
|___ChunkedEncodingError
|___ContentDecodingError
|___StreamConsumedError
|___RetryError
|___UnrewindableBodyError
"""