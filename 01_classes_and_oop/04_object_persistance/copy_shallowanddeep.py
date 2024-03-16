
# for: a_list = [ 1, 'New York', 100]

# - At first, an object (a list in this example) is created in the computer's memory. Now the object has its identity;
# - then the object is populated with other objects. Now our object has a value;
# - finally a variable, which you should treat as a label or name binding, is created, and this label refers to a distinct place in the computer memory.

""" 
id() points to the location in memory of the object

id() = identity of the object, a unique value amongst other object 
- NOT the absolute memory address occupied by the object
"""

a_string = '10 days to departure'
b_string = '20 days to departure'

print('a_string identity:', id(a_string))
print('b_string identity:', id(b_string))

print('\n--------------------------------------------------------------------------------------------------------------\n')

# id must be same when 2 vars refer to same object

a_string = '10 days to departure'
b_string = a_string

print('a_string identity:', id(a_string))
print('b_string identity:', id(b_string))

print('\n--------------------------------------------------------------------------------------------------------------\n')

# When comparing separate objects, start with the `==` operator, which compares the values of objects
# To check whether both operands refer to the same object or not, you should use the 'is' operator. 
#       In other words, it responds to the question: “Are both variables referring to the same identity?”

""" 
'==' compares value of objects
'is' compares identity of objects, are they actually the same object in memory
"""

a_string = ['10', 'days', 'to', 'departure']
b_string = a_string

print('a_string identity:', id(a_string))
print('b_string identity:', id(b_string))
print('The result of the value comparison:', a_string == b_string)
print('The result of the identity comparison:', a_string is b_string)

print()

a_string = ['10', 'days', 'to', 'departure']
b_string = ['10', 'days', 'to', 'departure']

print('a_string identity:', id(a_string))
print('b_string identity:', id(b_string))
print('The result of the value comparison:', a_string == b_string)
print('The result of the identity comparison:', a_string is b_string)

print('\n--------------------------------------------------------------------------------------------------------------\n')

print("Part 1")
print("Let's make a copy")
a_list = [10, "banana", [997, 123]]
b_list = a_list[:] # populates b_list with references to a_list in memory (shallow copy - and id is different)
print("a_list contents:", a_list, id(a_list))
print("b_list contents:", b_list, id(b_list))
print("Is it the same object?", a_list is b_list)

print()
print("Part 2")
print("Let's modify b_list[2]")
b_list[2][0] = 112
print("a_list contents:", a_list)
print("b_list contents:", b_list)
print("Is it the same object?", a_list is b_list)

# a modification of b_list[2] affected a_list[2] as well.
# why?
# - the 'a_list' object is a compound object;
# - we’ve run a shallow copy that constructs a new compound object, b_list in our example, and then populated it with references to the objects found in the original;
# - as you can see, a shallow copy is only one level deep. The copying process does not recurse and therefore does not create copies of the child objects, 
#           but instead populates b_list with references to the already existing objects.

print('\n--------------------------------------------------------------------------------------------------------------\n')

# use deepcopy to create a separate instance of the object in memory with the same attributes

import copy

print("Let's make a deep copy")
a_list = [10, "banana", [997, 123]]
b_list = copy.deepcopy(a_list)
print("a_list contents:", a_list)
print("b_list contents:", b_list)
print("Is it the same object?", a_list is b_list)

print()
print("Let's modify b_list[2]")
b_list[2][0] = 112 # won't affect a_list because we didn't do a deepcopy
print("a_list contents:", a_list)
print("b_list contents:", b_list)
print("Is it the same object?", a_list is b_list)

print('\n--------------------------------------------------------------------------------------------------------------\n')

import copy
import time

a_list = [(1,2,3) for x in range(1_000_000)]

print('Single reference copy')
time_start = time.time()
b_list = a_list
print('Execution time:', round(time.time() - time_start, 3))
print('Memory chunks:', id(a_list), id(b_list))
print('Same memory chunk?', a_list is b_list)

print()

print('Shallow copy')
time_start = time.time()
b_list = a_list[:] # different id's in memory, but they still refer to the same object
print('Execution time:', round(time.time() - time_start, 3)) # 0.004
print('Memory chunks:', id(a_list), id(b_list))
print('Same memory chunk?', a_list is b_list)

print()

print('Deep copy')
time_start = time.time()
b_list = copy.deepcopy(a_list)
print('Execution time:', round(time.time() - time_start, 3)) # 1.246
print('Memory chunks:', id(a_list), id(b_list))
print('Same memory chunk?', a_list is b_list)

print('\n--------------------------------------------------------------------------------------------------------------\n')

# deepcopy applied to objects
import copy

class Example:
    def __init__(self):
        self.properties = ["112", "997"]
        print("Hello from __init__()")

a_example = Example()
b_example = copy.deepcopy(a_example)
print("Memory chunks:", id(a_example), id(b_example))
print("Same memory chunk?", a_example is b_example)
print()
print("Let's modify the movies list")
b_example.properties.append("911")
print('a_example.properties:', a_example.properties)
print('b_example.properties:', b_example.properties)

# summary:
#   the deepcopy() method creates and persists new instances of source objects, whereas any shallow copy operation only stores references to the original memory address;
#   a deep copy operation takes significantly more time than any shallow copy operation;
#   the deepcopy() method copies the whole object, including all nested objects; it’s an example of practical recursion taking place;
#   deep copy might cause problems when there are cyclic references in the structure to be copied.