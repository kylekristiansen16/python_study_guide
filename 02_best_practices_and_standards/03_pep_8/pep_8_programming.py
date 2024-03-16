# https://peps.python.org/pep-0008/#programming-recommendations

""" 
– make comparisons to the None object with the use of is or is not, not with the (in)equality operators (== and !=), e.g.
"""

# Bad:

if x == None:
    print("A")

# Good:

if x is None:
    print("A")
    
""" 
– do not use the (in)equality operators when comparing Boolean values to True or False. Again, use is or is not instead:
"""
# Bad:

my_boolean_value = 2 > 1
if my_boolean_value == True:
    print("A")
else:
    print("B")

# Good:

my_boolean_value = 2 > 1
if my_boolean_value is True:
    print("A")
else:
    print("B")
 
# Better:

my_boolean_value = 2 > 1
if my_boolean_value:
    print("A")
else:
    print("B")
    
""" 
– for readability purposes, use the is not operator instead of not … is:
"""
# Bad:

if not x is None:
    print("It exists")

# Good:

if x is not None:
    print("It exists")

""" 
– when you want to “catch" an exception, refer to specific exceptions rather than use the bare except: clause only:
"""
# good
try:
    import my_module
except ImportError:
    my_module = None
    
""" 
– when checking for prefixes or suffixes, use the ''.startswith() and ''.endswith() string methods, as they’re cleaner and less error prone. 
Generally, it’s better to use string methods over importing the string module.
"""
# Bad:

if name[:4] == 'Adam':
    # do something

# Good:

if name.startswith('Adam'):
    # do something