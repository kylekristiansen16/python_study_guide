""" 
When writing code in Python, you should remember to follow these two simple rules:

Use four spaces per indentation level, and;
Use spaces rather than tabs.

"""
# Bad:

def my_fun_one(x, y):
    return x * y

def my_fun_two(a, b):
  return a + b

# Good:

def my_function(x, y):
    return x * y
  
""" 
Continuation lines (i.e., logical lines of code that you want to split because they’re too long or because you want to improve readability) 
are allowed if using parentheses/brackets/braces:
"""
# Bad:

my_list_one = [1, 2, 3,
    4, 5, 6
]

a = my_function_name(a, b, c,
    d, e, f)

# Good:

my_list_one = [
    1, 2, 3,
    4, 5, 6,
    ]

a = my_function_name(a, b, c,
                       d, e, f)


# Good:

my_list_two = [
    1, 2, 3,
    4, 5, 6,
]


def my_fun(
        a, b, c,
        d, e, f):
    return (a + b + c) * (d + e + f)
  
""" 
max line length and line breaks 

If possible, you should limit all lines to a maximum of 79 characters as this will help you avoid wrapping several lines of code
72 for docstrings/comments (always)
99 is feasible exception for code lines(rarely)

Line breaks and operators

break before binary operators
"""

# Recommended

total_fruits = (apples
                + pears
                + grapes
                - (black currants - red currants)
                - bananas
                + oranges)

""" 
blank lines

– two blank lines to surround top-level function and class definitions:
– a single blank line to surround method definitions inside a class:
– blank lines in functions in order to indicate logical sections (sparingly). For example:
"""

class ClassOne:
    pass


class ClassTwo:
    pass


def my_top_level_function():
    return None
print("------------------")
  
class MyClass:
    def method_one(self):
        return None

    def method_two(self):
        return None
print("------------------")

def calculate_average():
    how_many_numbers = int(input("How many numbers? "))
    
    if how_many_numbers > 0:
        sum_numbers = 0
        for i in range(0, how_many_numbers):
            number = float(input("Enter a number: "))
            sum_numbers += number

        average = 0
        average = sum_numbers / how_many_numbers

        return average
    else:
        return "Nothing happens."
      
""" 
recommended that you use Python’s default encodings (Python 3 -- UTF-8, Python 2 -- ASCII)

always put imports at the beginning of your script
between module comments/docstrings and module globals and constants, respecting the following order:
 - Standard library imports;
 - Related third-party imports;
 - Local application/library specific imports.
 
avoid using wildcard imports (from <module> import *).
"""
# Bad:

import sys, os

# Good:

import os
import sys

from subprocess import Popen, PIPE

import animals.mammals.dogs.puppies
