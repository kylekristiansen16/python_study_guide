# a function is "callable"

def simple_decorator(own_function):

    def internal_wrapper(*args, **kwargs):
        print('"{}" was called with the following arguments'.format(own_function.__name__))
        print('\t{}\n\t{}\n'.format(args, kwargs))
        own_function(*args, **kwargs)
        print('Decorator is still operating')

    return internal_wrapper

# is equal to 

class SimpleDecorator:
    def __init__(self, own_function):
        self.func = own_function # assign decorated function to a self.<attribute>

    def __call__(self, *args, **kwargs): # __call__ is a special method that makes an object callable
        print('"{}" was called with the following arguments'.format(self.func.__name__))
        print('\t{}\n\t{}\n'.format(args, kwargs))
        self.func(*args, **kwargs)
        print('Decorator is still operating')

@SimpleDecorator
def combiner(*args, **kwargs):
    print("\tHello from the decorated function; received arguments:", args, kwargs)

combiner('a', 'b', exec='yes')

# the benefit:
#     classes bring all the subsidiarity they can offer, like inheritance and the ability to create dedicated supportive methods.

""" 
another way to write decorators, with classes instead of cuntions 

the  __call__() special method implements the decorator functionality -> makes the object callable like a function
"""

# --------------------------------------------------------------------------------------------------------------------------------------------

print()

def warehouse_decorator(material):
    def wrapper(our_function):
        def internal_wrapper(*args):
            print('* Wrapping items from {} with {}'.format(our_function.__name__, material))
            our_function(*args)
            print()
        return internal_wrapper
    return wrapper
@warehouse_decorator('kraft')
def pack_books(*args):
    print("We'll pack books:", args)
    
# is equal to

class WarehouseDecorator:
    def __init__(self, material):
        self.material = material # now the decorator argument is an attribute of the class

    def __call__(self, own_function): # function gets passed to call method
        def internal_wrapper(*args, **kwargs):
            print('<strong>*</strong> Wrapping items from {} with {}'.format(own_function.__name__, self.material))
            own_function(*args, **kwargs)
            print()
        return internal_wrapper

@WarehouseDecorator('kraft')
def pack_books(*args):
    print("We'll pack books:", args)
