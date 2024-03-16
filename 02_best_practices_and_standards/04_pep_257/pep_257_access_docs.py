
def my_fun(a, b):
    """The summary line goes here.

    A more elaborate description of the function.

    Parameters:
    a: int (description)
    b: int (description)

    Returns:
    int: Description of the return value.
    """
    return a*b

print(my_fun.__doc__)

print('------------------')

# print(help(my_fun))

print('------------------')

import pprint

print('###################')
print('### pprint docs ###')
print('###################')
print(pprint.__doc__)

print('------------------')

import requests

print('##################')
print('###  requests  ###')
print('##################')
print(requests.__doc__)