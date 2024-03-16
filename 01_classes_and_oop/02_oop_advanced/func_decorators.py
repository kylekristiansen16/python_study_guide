""" 
A decorator is one of the design patterns that describes the structure of related objects. Python is able to decorate functions, methods, and classes.

The decorator's operation is based on wrapping the original function with a new "decorating" function (or class), hence the name "decoration". 
This is done by passing the original function (i.e., the decorated function) as a parameter to the decorating function so that the decorating 
function can call the passed function. The decorating function returns a function that can be called later. 
- !the decorating function returns a function that can be called later!

Of course, the decorating function does more, because it can take the parameters of the decorated function and perform additional actions and that make 
it a real decorating function.

Decorators are used to perform operations before and after a call to a wrapped object or even to prevent its execution, depending on the circumstances. 
As a result, we can change the operation of the packaged object without directly modifying it.

Decorators are used in:

the validation of arguments;
the modification of arguments;
the modification of returned objects;
the measurement of execution time;
message logging;
thread synchronization;
code refactorization;
caching.
"""

# basic implementation of a decorator:
def simple_hello():
    print("Hello from simple function!")

def simple_decorator(function):
    print('We are about to call "{}"'.format(function.__name__))
    return function

decorated = simple_decorator(simple_hello)
decorated()

# more interesting implementation:
# this is the most important thing to remember: 
#       the name of the simple_function object ceases to indicate the object representing our simple_function() 
#       and from that moment on it indicates the object returned by the decorator, the simple_decorator.
def simple_decorator(function):
    print('We are about to call "{}"'.format(function.__name__))
    return function

@simple_decorator
def simple_hello():
    print("Hello from simple function!")

simple_hello()

# wrapping a function within a decorator:
def simple_decorator(own_function):

    def internal_wrapper(*args, **kwargs):
        print('"{}" was called with the following arguments'.format(own_function.__name__))
        print('\t{}\n\t{}\n'.format(args, kwargs))
        own_function(*args, **kwargs)
        print('Decorator is still operating')

    return internal_wrapper

@simple_decorator
def combiner(*args, **kwargs):
    print("\tHello from the decorated function; received arguments:", args, kwargs)

combiner('a', 'b', exec='yes')

