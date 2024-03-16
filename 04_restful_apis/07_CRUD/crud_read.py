
import requests

key_names = ["id", "brand", "model", "production_year", "convertible"]
key_widths = [10, 15, 10, 20, 15]


def show_head():
    for (n, w) in zip(key_names, key_widths):
        print(n.ljust(w), end='| ')
    print()


def show_car(car):
    for (n, w) in zip(key_names, key_widths):
        print(str(car[n]).ljust(w), end='| ')
    print()


def show(json):
    show_head()
    for car in json:
        show_car(car)


try:
    reply = requests.get('http://localhost:3000/cars')
except requests.RequestException:
    print('Communication error')
else:
    if reply.status_code == requests.codes.ok:
        show(reply.json())
    else:
        print('Server error')

print('\n---------------------\n')

""" 
URI for specific response: http://server:port/resource/id
"""


def show_empty():
    for w in key_widths:
        print(' '.ljust(w), end='| ')
    print()


def show(json):
    show_head()
    if type(json) is list:
        for car in json:
            show_car(car)
    elif type(json) is dict:
        if json:
            show_car(json)
        else:
            show_empty()


try:
    reply = requests.get('http://localhost:3000/cars/2') # 2 is the id of the car we request from the server
except requests.RequestException:
    print('Communication error')
else:
    if reply.status_code == requests.codes.ok:
        show(reply.json())
    elif reply.status_code == requests.codes.not_found:
        print("Resource not found")
    else:
        print('Server error')

print('\n---------------------\n')

"""  
json-server assumes that a uri formed in the following way:
    http://server:port/resource?_sort=property
causes the response to be sorted in ascending order using a property named prop

** the ? character separates the resource identification from additional request parameters **

want to reverse the sort order? 
    http://server:port/resource?_sort=property&_order=desc

**  the & character separates additional request parameters from each other **

Some servers can do much more, e.g., they can perform full-text searches, make slices, or analyze complex filtering expressions. The sky is the limit.
"""

try:
    # reply = requests.get('http://localhost:3000/cars?_sort=production_year')
    reply = requests.get('http://localhost:3000/cars?_sort=production_year&_order=desc')
except requests.RequestException:
    print('Communication error')
else:
    print('Connection=' + reply.headers['Connection']) # Connection=keep-alive or Connection=close, depending on the server
    if reply.status_code == requests.codes.ok:
        show(reply.json())
    elif reply.status_code == requests.codes.not_found:
        print("Resource not found")
    else:
        print('Server error')

""" 
keep-alive refers to the server's mode of connection management. it's returned in the response header
"""