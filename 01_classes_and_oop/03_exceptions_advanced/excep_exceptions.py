# Python comes with ~63 built-in exceptions, and they can be represented in the form of a tree-shaped hierarchy. 
# The reason for this is that exceptions are inherited from BaseException, the most general exception class

""" 
exceptions all have attributes 
    args
    name
    path
    and others
"""

print(dir(Exception))
print()
print(Exception.__dict__)
print()
print(Exception.__doc__)

print()

try:
    import abcdefghijk
except ImportError as e:
    print(e.args)
    print(e.name)
    print(e.path)

print('\n--------------------------------------------------------------------------------------------------------------\n')

try:
    print(int('a'))
except ValueError as e_variable:
    print(e_variable.args)

print('\n--------------------------------------------------------------------------------------------------------------\n')

try:
    b'\x80'.decode("utf-8")
except UnicodeError as e:
    print(e)
    print(e.encoding)
    print(e.reason)
    print(e.object)
    print(e.start)
    print(e.end)
    
print('\n--------------------------------------------------------------------------------------------------------------\n')

""" 
exceptions get chained together and that relationship is how we can reference them
    __context__ -> implicit - stacked function calls sending exceptions up the stack
    __cause__ -> only filled out when you use the "raise from" construct (explicit)
    
this is how to tell the difference!
- explicity - raise from
- implicitly - try except
"""
a_list = ['First error', 'Second error']

try:
    print(a_list[3])
except Exception as e:
    try:
        # the following line is a developer mistake - they wanted to print progress as 1/10	but wrote 1/0
        print(1 / 0)
    except ZeroDivisionError as f:
        print('Inner exception (f):', f)
        print('Outer exception (e):', e)
        print('Outer exception referenced:', f.__context__)
        print('Is it the same object:', f.__context__ is e)
        
        print(f'inner exception context: {f.__context__}, inner exception cause: {f.__cause__}')
        print(f'outer exception context: {e.__context__}, outer exception cause: {e.__cause__}')

print('\n--------------------------------------------------------------------------------------------------------------\n')

class RocketNotReadyError(Exception):
    pass

def personnel_check():
    try:
        print("\tThe captain's name is", crew[0])
        print("\tThe pilot's name is", crew[1])
        print("\tThe mechanic's name is", crew[2])
        print("\tThe navigator's name is", crew[3])
    except IndexError as e:
        raise RocketNotReadyError('Crew is incomplete') from e

crew = ['John', 'Mary', 'Mike']
print('Final check procedure')

# personnel_check()
# vs.
try:
    personnel_check()
except RocketNotReadyError as f:
    print('General exception: "{}", caused by "{}"'.format(f, f.__cause__))
    
print('\n--------------------------------------------------------------------------------------------------------------\n')

# check out how the same exception can be used to bucket different types of errors
# the approach becomes more generic 

class RocketNotReadyError(Exception):
    pass

def personnel_check():
    try:
        print("\tThe captain's name is", crew[0])
        print("\tThe pilot's name is", crew[1])
        print("\tThe mechanic's name is", crew[2])
        print("\tThe navigator's name is", crew[3])
    except IndexError as e:
        raise RocketNotReadyError('Crew is incomplete') from e

def fuel_check():
    try:
        print('Fuel tank is full in {}%'.format(100 / 0))
    except ZeroDivisionError as e:
        raise RocketNotReadyError('Problem with fuel gauge') from e

crew = ['John', 'Mary', 'Mike']
fuel = 100
check_list = [personnel_check, fuel_check]

print('Final check procedure')

for check in check_list:
    try:
        check()
    except RocketNotReadyError as f:
        print('RocketNotReady exception: "{}", caused by "{}"'.format(f, f.__cause__))

print('\n--------------------------------------------------------------------------------------------------------------\n')

""" 
traceback objects are ascoociated with exceptions
- they come with nice methods for simplifying the traceback
"""
import traceback # each exception has a traceback object associated with it

class RocketNotReadyError(Exception):
    pass

def personnel_check():
    try:
        print("\tThe captain's name is", crew[0])
        print("\tThe pilot's name is", crew[1])
        print("\tThe mechanic's name is", crew[2])
        print("\tThe navigator's name is", crew[3])
    except IndexError as e:
        raise RocketNotReadyError('Crew is incomplete') from e

crew = ['John', 'Mary', 'Mike']

print('Final check procedure')

try:
    personnel_check()
except RocketNotReadyError as f:
    print(f.__traceback__)
    print(type(f.__traceback__))
    print('\nTraceback details')
    details = traceback.format_tb(f.__traceback__)
    print("\n".join(details))

print('Final check is over')