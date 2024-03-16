
"""  
tk = widget toolkit / GUI toolkit / UX library
- a set of tools that allow you to build a GUI application portable across OS platforms

tkinter = tk interface, a python binding to the tk toolkit

The GUI application itself consists of four essential elements:
 - importing the needed tkinter components;
 - creating an application’s main window;
 - adding a set of necessary widgets to the window;
 - launching the event controller.
 
EVENT CONTROLLER
- the event controller is a component that monitors the state of the application's GUI and responds to user actions

EVENT LOOP
- the event loop is a piece of code that waits for the event controller to detect an event, and then calls the appropriate action

EVENT HANDLER
- the event handler is a piece of code that is executed when the event loop detects an event
- responsible for responding to all clicks addressed to our button

CALLBACK / HANDLER
- a function designed to be invoked by someone/something else (not us!) is often called a callback. We'll use the names handler and callback interchangeably
- the callback is a function that is called when the user clicks the button

DIALOGBOX
- dialog box is an example of a modal window – a window which grabs the whole of the application's focus. It means that all other application widgets become deaf as long as the modal window is present
"""

import tkinter as tk # import the tkinter module
from tkinter import messagebox # import the messagebox module from tkinter
# help(tk)

skylight = tk.Tk()  # create a window - completely invisible window
skylight.title("Skylight")  # set the window title

# build a callback function
def click():
    reply = messagebox.askquestion("Exit", "Do you really want to quit?")  # title, message
    if reply == "yes":
        skylight.destroy()

# create button
button = tk.Button(skylight, text="Exit", command=click)  # create a button widget - the button is not visible yet or placed on the window
# button.pack(side=tk.LEFT)  # place the button on the window - the button is now visible
button.place(x=10, y=10)  # (0,0) is the top left hand corner on a window coordinate plane

skylight.mainloop()  # launch the event controller - the window is now visible and can be interacted with
