
""" 
shelve, is built on top of pickle, and implements a serialization dictionary where objects are pickled and associated with 
a key. The keys must be ordinary strings, because the underlying database (dbm) requires strings.
"""

import os
out = './01_classes_and_oop/04_object_persistance/output'
if not os.path.exists(f'{out}'):
    os.mkdir(f'{out}')

""" 
flag parameter:
    'r'	Open existing database for reading only
    'w'	Open existing database for reading and writing
    'c'	Open database for reading and writing, creating it if it doesn’t exist (this is a default value)
    'n'	Always create a new, empty database, open for reading and writing
"""
 
import shelve

shelve_name = os.path.join(out,'shelve.shlv')

my_shelve = shelve.open(shelve_name, flag='c')
my_shelve['EUR'] = {'code':'Euro', 'symbol': '€'}
my_shelve['GBP'] = {'code':'Pounds sterling', 'symbol': '£'}
my_shelve['USD'] = ['code', 'US dollar', 'symbol', '$']
my_shelve['JPY'] = {'code':'Japanese yen', 'symbol': '¥'}
my_shelve.close()

print('items shelved\n')

new_shelve = shelve.open(shelve_name)
print('accessing shelve: USD')
print(new_shelve['USD'])
new_shelve.close()

""" 
You should treat a shelve object as a Python dictionary, with a few additional notes:

the keys must be strings;
Python puts the changes in a buffer which is periodically flushed to the disk. To enforce an immediate flush, call the sync() method on your shelve object;
when you call the close() method on an shelve object, it also flushes the buffers.
When you treat a shelve object like a Python dictionary, you can make use of the dictionary utilities:

the len() function;
the in operator;
the keys() anditems() methods;
the update operation, which works the same as when applied to a Python dictionary;
the del instruction, used to delete a key-value pair.

because the shelve module is backed by pickle, it isn’t safe to load a shelve from an untrusted source. As with pickle, loading a shelve can execute arbitrary code
"""