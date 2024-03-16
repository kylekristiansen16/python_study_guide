"""
*args – refers to a tuple of all additional, not explicitly expected positional arguments, # ARGS IS A TUPLE
        so arguments passed without keywords and passed next after the expected arguments. 
        In other words, *args collects all unmatched positional arguments;
**kwargs    (keyword arguments) – refers to a dictionary of all unexpected arguments that were passed in the form of keyword=value pairs. 
            Likewise, **kwargs collects all unmatched keyword arguments.
            
ordering of arguments matters!! cannot pass unknown keyword arguments before known ones
"""

def combiner(a, b, *args, **kwargs):
    print(a, type(a))
    print(b, type(b))
    print(args, type(args))
    print(kwargs, type(kwargs))


combiner(10, '20', 40, 60, 30, argument1=50, argument2='66')

"""
When you want to forward arguments received by your very smart and universal function 
(defined with *args and **kwargs, of course) to another handy and smart function, you should do that in the following way:
"""

def combiner(a, b, *args, **kwargs):
    super_combiner(*args, **kwargs)

def super_combiner(*my_args, **my_kwargs):
    print('my_args:', my_args)
    print('my_kwargs', my_kwargs)

combiner(10, '20', 40, 60, 30, argument1=50, argument2='66')

# VS 

def combiner(a, b, *args, **kwargs):
    super_combiner(args, kwargs)
    
combiner(10, '20', 40, 60, 30, argument1=50, argument2='66')

# getting tricky with it:

def combiner(a, b, *args, c=20, **kwargs):
    super_combiner(c, *args, **kwargs)
    
def super_combiner(my_c, *my_args, **my_kwargs):
    print('my_args:', my_args)
    print('my_c:', my_c)
    print('my_kwargs', my_kwargs)
    
combiner(1, '1', 1, 1, c=2, argument1=1, argument2='1')