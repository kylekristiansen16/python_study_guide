""" 
string quotes

Python allows us to use single-quoted (e.g., 'a string') and double-quoted (e.g., "a string") strings

Whitespace in expressions and statements

you should avoid using too much whitespace, as it makes your code difficult to follow.

do not use excessive whitespace immediately inside parentheses/brackets/braces, or immediately before a comma/semicolon/colon:
"""

# Bad:

my_list = ( dog[ 2 ] , 5 , { "year": 1980 } , "string" )
if 5 in my_list : print( "Hello!" ) ; print( "Goodbye!" )

# Good:

my_list = (dog[2], 5, {"year": 1980}, "string")
if 5 in my_list: print("Hello!"); print("Goodbye!")

""" 
In the case of a slice, the colon should have equal amounts of space on both sides
"""
# Bad:

bread[0 : 3], roll[1: 3 :5], bun[3: 5:], donut[ 1: :5 ]

# Good:

bread[0:3], roll[1:3:5], bun[3:5:], donut[1::5]

""" 
not use excessive whitespace:

after a trailing comma followed by a closing parenthesis, or
immediately before an opening parenthesis that marks the beginning of the argument list of a function invocation, or
immediately before an opening parenthesis that marks the beginning of indexing/slicing.
"""
# Bad:

my_tuple = (0, 1, 2, )
my_function (5)
my_dictionary ['key'] = my_list [index]

# Good:

my_tuple = (0, 1, 2,)
my_function(5)
my_dictionary['key'] = my_list[index]

""" 
Don’t use more than one space before and after operators
"""
# Bad:

a         = 1
b         = a        + 2
my_string = 'string' * 2

# Good:

a = 1
b = a + 2
my_string = 'string' * 2

""" 
Surround binary operators with a single space on both sides
"""
# Bad:

x=x+3
x -=1

x = x * 2 - 1
x = (x - 1) * (x + 2)

# Good:

x = x + 3
x -= 1

x = x*2 - 1  # Use your own judgement.
x = (x-1) * (x+2)  # Use your own judgement.

""" 
Don’t surround the = operator with spaces if it’s used to indicate a keyword argument/default value
"""
# Bad:

def my_function(x, y = 2):
    return x * y

# Good:

def my_function(x, y=2):
    return x * y
