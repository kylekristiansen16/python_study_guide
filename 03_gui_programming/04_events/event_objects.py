
"""
An event object is an instantiation of the Event class
not all properties have meaning for every event. If the event is related to some of the mouse actions, 
the object’s parts referring to the keyboard remain uninitialized, and vice versa.

Property name	Property role
widget	The widget’s object (not the widget’s name!) to which the event is addressed
<x>
<y>	The mouse cursor’s coordinates at the moment of the event’s occurrence (both coordinates are counted relative to the target widget)
<x_root>
<y_root>	As above, but relative to the screen
<char>	The pressed key character code (only for keyboard events)
<keysym>	The pressed key symbol (only for keyboard events)
The full list of all recognized key symbols is presented here: https://www.tcl.tk/man/tcl8.4/TkCmd/keysyms.htm
<keycode>	The pressed key numerical code (only for keyboard events)
Don’t confuse this with char, which is the ASCII/UNICODE code of the character bound to the key
<num>	The number of the clicked mouse button (only for mouse events - 1 for the left button, 2 for the middle button, 3 for the right button)
<type>	The event’s type
"""


import tkinter as tk
from tkinter import messagebox

def click(event=None):
    if event is None:
        tk.messagebox.showinfo("Click!", "I love clicks!")
    else:
        string = "x=" + str(event.x) + ",y=" + str(event.y) + \
                 ",num=" + str(event.num) + ",type=" + event.type
        tk.messagebox.showinfo("Click!", string)        

window = tk.Tk()
label = tk.Label(window, text="Label")
label.bind("<Button-1>", click)
label.pack()

button = tk.Button(window, text="Button", command=click)
button.pack(fill=tk.X)

frame = tk.Frame(window, height=30, width=100, bg="#55BF40")
frame.bind("<Button-1>", click)
frame.pack()

window.mainloop()

