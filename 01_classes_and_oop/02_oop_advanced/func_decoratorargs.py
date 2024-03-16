# decorator receiving arguments
# The pack_books function will be executed as follows:
#       the warehouse_decorator('kraft') function will return the wrapper function;
#       the returned wrapper function will take the function it is supposed to decorate as an argument;
#       the wrapper function will return the internal_wrapper function, which adds new functionality (material display) and runs the decorated function.

def warehouse_decorator(material):
    def wrapper(our_function):
        def internal_wrapper(*args, **kwargs): # it's always safe to do this, and it must be done if our_function takes keyword arguments
            print('<strong>*</strong> Wrapping items from {} with {}'.format(our_function.__name__, material))
            our_function(*args, **kwargs)
            print()
        return internal_wrapper
    return wrapper

@warehouse_decorator('kraft') # wrapper around normal func, not even in class (then it would be called method)
def pack_books(*args, **kwargs): # *args is a tuple of non-keyworded arguments, **kwargs is a dictionary of keyword arguments
    print("We'll pack books:", args)
    print("got some interesting extra arguments:", kwargs)

@warehouse_decorator('foil')
def pack_toys(*args):
    print("We'll pack toys:", args)

@warehouse_decorator('cardboard')
def pack_fruits(*args):
    print("We'll pack fruits:", args)

pack_books('Alice in Wonderland', 'Winnie the Pooh', whose='line', iss='it anyway')
pack_toys('doll', 'car')
pack_fruits('plum', 'pear')