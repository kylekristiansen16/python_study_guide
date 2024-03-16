
""" 
observable variable. 
 - This variable works like a regular variable (i.e., it’s able to store values which are accessible to the outside world) 
 - but there is something more – any change of the variable’s state can be observed by a number of external agents. 
     - For example, the Entry widget can use its own observable variable to inform other objects that the contents of the input field have been changed

 - such a variable is an object of the container class. This means that a variable of that kind has to be explicitly created and initialized
 - these variables are typed. You have to be aware of what type of value you want to store in them, and don’t change your mind during the variable’s life
 - you can only create an observable variable after the main window initialization

types:
    BooleanVar = True/False, default=False
    DoubleVar = float, default=0.0
    IntVar = integer, default=0
    StringVar = string, default=""
    
    get() = returns the variable’s value
    set() = sets the variable’s value
    
Each observable variable can be enriched with a number of observers. 
    An observer is a function (a kind of callback) which will be invoked automatically each time a specified event occurs in the variable’s life
    
*** trace() = method used to add an observer to the variable ***

obsid = variable.trace(trace_mode, observer)
    trace_mode = one of the following values:
        "r" = the observer will be invoked when the variable’s value is read (get)
        "w" = the observer will be invoked when the variable’s value is written (set)
        "u" = the observer will be invoked when the variable is unset (del)
    observer = a function to be invoked when the event occurs
    
observing the state of the variable is important!!! 
    note that the observer is a function
"""

# def observer(id, ix, act):
#     """ 
#         id – an internal observable variable identifier (unusable for us);
#         ix – an empty string (always – don’t ask us why, it’s tkinter’s business)
#         act – a string informing us what happened to the variable or, in other words, what reason triggered the observer ('r', 'w' or 'u')
#     """
#     print("observer:", id, ix, act)
    
# remove the observer using the variable’s trace_vdelete(trace_mode, obsid) method
#   trace_mode – the mode in which the observer has been created;
#   obsid – the observer’s identifier obtained from the previous trace() invocation.

import tkinter as tk

def r_observer(*args):
    print("Reading")

def w_observer(*args):
    print("Writing")

dummy = tk.Tk()    # we need this although we won't display any windows
variable = tk.StringVar()
variable.set("abc")
r_obsid = variable.trace("r", r_observer)
w_obsid = variable.trace("w", w_observer)
variable.set(variable.get() + 'd')  # read followed by write
variable.trace_vdelete("r", r_obsid)
variable.set(variable.get() + 'e')
variable.trace_vdelete("w", w_obsid)
variable.set(variable.get() + 'f')
print(variable.get())
