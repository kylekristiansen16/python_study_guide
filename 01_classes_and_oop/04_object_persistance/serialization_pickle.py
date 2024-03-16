
""" 
The simplest way to persist outcomes is to generate a flat text file and to write your outcomes. It’s a very simple thing to do way which 
is not suitable for persisting sets of different types of objects or nested structures.

Object serialization is the process of converting an object structure into a stream of bytes to store the object in a file or database, or 
to transmit it via a network. This byte stream contains all the information necessary to reconstruct the object in another Python script.

This reverse process is called deserialization.

The following types can be pickled:
    None, booleans;
    integers, floating-point numbers, complex numbers;
    strings, bytes, bytearrays;
    tuples, lists, sets, and dictionaries containing pickleable objects;
    objects, including objects with references to other objects (remember to avoid cycles!)
    references to functions and classes, but not their definitions.
"""

import os
out = './01_classes_and_oop/04_object_persistance/output'
if not os.path.exists(f'{out}'):
    os.mkdir(f'{out}')

import pickle

a_dict = dict()
a_dict['EUR'] = {'code':'Euro', 'symbol': '€'}
a_dict['GBP'] = {'code':'Pounds sterling', 'symbol': '£'}
a_dict['USD'] = {'code':'US dollar', 'symbol': '$'}
a_dict['JPY'] = {'code':'Japanese yen', 'symbol': '¥'}

a_list = ['a', 123, [10, 100, 1000]]

with open(os.path.join(out,'multidata.pckl'), 'wb') as file_out:
    pickle.dump(a_dict, file_out)
    pickle.dump(a_list, file_out)
    
print('pickle dumped\n')
    
with open(os.path.join(out,'multidata.pckl'), 'rb') as file_in:
    data1 = pickle.load(file_in)
    data2 = pickle.load(file_in)

print(type(data1))
print(data1)
print(type(data2))
print(data2)

# Remember that with the 'pickle' module, you have to remember the order in which the objects were persisted and the deserialization code should follow the same order.

print('\n--------------------------------\n')

# returning byte objects to be sent elsewhere

a_list = ['a', 123, [10, 100, 1000]]
bytes = pickle.dumps(a_list)
print('Intermediate object type, used to preserve data:', type(bytes))

# now pass 'bytes' to appropriate driver -> whatever you're working with 

print('\n')

# therefore when you receive a bytes object from an appropriate driver you can deserialize it
b_list = pickle.loads(bytes)
print('A type of deserialized object:', type(b_list))
print('Contents:', b_list)

print('\n--------------------------------------------------------------------------------------------------------------\n')

""" 
Note that functions (both built-in and user-defined) are pickled by their name reference, not by any value. This means that 
only the function name is pickled; neither the function’s code, nor any of its function attributes, are pickled.

Similarly, classes are pickled by named reference, so the same restrictions in the unpickling environment apply. Note that 
none of the class’s code or data are pickled.

ensure that the environment where the class or function is unpickled is able to import the class or function definition. In 
other words, the function or class must be available in the namespace of your code reading the pickle file.
"""

def f1():
    print('Hello from the jar!')

with open(os.path.join(out,'function.pckl'), 'wb') as file_out:
    pickle.dump(f1, file_out)

with open(os.path.join(out,'function.pckl'), 'rb') as file_in:
    data = pickle.load(file_in)

print(type(data))
print(data)
data() # only works because the function is defined in the namespace of the code reading the pickle file

print('\n--------------------------------\n')

class Cucumber:
    def __init__(self):
        self.size = 'small'

    def get_size(self):
        return self.size

cucu = Cucumber()

with open(os.path.join(out,'cucumber.pckl'), 'wb') as file_out:
    pickle.dump(cucu, file_out)

with open(os.path.join(out,'cucumber.pckl'), 'rb') as file_in:
    data = pickle.load(file_in)

print(type(data))
print(data)
print(data.size)
print(data.get_size())

""" 
Summary:
    it’s a Python implementation of the serialization process, so the pickled data cannot be exchanged with programs written 
        in other languages like Java or C++. In such cases, you should think about the JSON or XML formats, which could be 
        less convenient than pickling, but when assimilated are more powerful than pickling;
    the pickle module is constantly evolving, so the binary format may differ between different versions of Python. Pay 
        attention that both serializing and deserializing parties are making use of the same pickle versions;
    the pickle module is not secured against erroneous or maliciously constructed data. Never unpickle data received from an 
        untrusted or unauthenticated source.
"""