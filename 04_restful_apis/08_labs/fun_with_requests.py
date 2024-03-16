


import sys
import requests
from pprint import pprint

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

try:
    reply = requests.head(url=f"http://{server}:{str(port)}")
    print(reply.status_code)
    pprint(reply.headers)
except requests.exceptions.Timeout:
    print("Error: connection timeout")
    sys.exit(1)
except requests.exceptions.ConnectionError:
    print("Error: connection error")
    sys.exit(1)

sys.exit(0)