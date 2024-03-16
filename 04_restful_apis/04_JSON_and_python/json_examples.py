
import json

# json.dumps() - converts a Python object into a JSON string
# ’s at the end of the function's name means string

comics = '"The Meaning of Life" by Monty Python\'s Flying Circus'
print(f"string: {json.dumps(comics)}")
with open("/Users/kylekristiansen/cherreco/python/04_restful_apis/04_JSON_and_python/file.txt", "w") as f:
    json.dump(comics, fp=f)

my_list = [1, 2.34, True, "False", None, ['a', 0]]
print(f"list: {json.dumps(my_list)}")

my_tuple = (1, 2.34, True, "False", None, ['a', 0])
print(f"tuple: {json.dumps(my_tuple)}")

my_dict = {'me': "Python", 'pi': 3.141592653589, 'data': (1, 2, 4, 8), 'set': None}
print(f"dict: {json.dumps(my_dict)}")

print()
""" 
pythong data -> json element
dict -> object
list, tuple -> array
string -> string
int, float -> number
True / False -> true / false
None -> null

what's the catch? 
"""

class Who:
    def __init__(self, name, age):
        self.name = name
        self.age = age


some_man = Who('John Doe', 42)
try:
    print(json.dumps(some_man))
except TypeError as te:
    print(f"TypeError: {te}")
    
# how to fix it?

# option 1: use a function to convert the object to a dictionary

def encode_who(w):
    if isinstance(w, Who):
        return w.__dict__
    else:
        raise TypeError(w.__class__.__name__ + ' is not JSON serializable')

some_man = Who('John Doe', 42)
print(f"option 1, use a function: {json.dumps(some_man, default=encode_who)}")

# option 2: use a class to convert the object to a dictionary, override the default method in json.JSONEncoder

class MyEncoder(json.JSONEncoder):
    def default(self, w):
        if isinstance(w, Who):
            return w.__dict__
        else:
            return super().default(self, w)


some_man = Who('John Doe', 42)
print(f"option 2, use a class: {json.dumps(some_man, cls=MyEncoder)}")

print()

# json.loads() - converts a JSON string into a Python object

jstr = '"\\"The Meaning of Life\\" by Monty Python\'s Flying Circus"' # must comply with JSON syntax to be valid for .loads()
comics = json.loads(jstr)
print(type(comics))
print(comics)

jstr = '[1, 2.34, true, "False", null, ["a", 0]]'
my_list = json.loads(jstr)
print(type(my_list))
print(my_list)

print()

# go back and forth between json and python

def decode_who(w):
    return Who(w['name'], w['age'])


old_man = Who("Jane Doe", 23)
json_str = json.dumps(old_man, default=encode_who)
new_man = json.loads(json_str, object_hook=decode_who)
print(f"encoded and decoded: {type(new_man)}")
print(f"attributes of new_man: {new_man.__dict__}")

print() 

# by the object approach, we can use the same class to encode and decode the object

class MyDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decode_who)

    def decode_who(self, d):
        return Who(**d)


some_man = Who('Jane Doe', 23)
json_str = json.dumps(some_man, cls=MyEncoder)
new_man = json.loads(json_str, cls=MyDecoder)

print(type(new_man))
print(new_man.__dict__)