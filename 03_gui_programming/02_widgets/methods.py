
""" 
Widget.after(time_ms, function)
 - two arguments: 
    - the first is a time interval specification (expressed in milliseconds: 1 s = 1000 ms) and 
    - the second points to an existing function; 
 - successful invocation of the method causes the event manager to change its plans; 
 - when the number of milliseconds elapses, the manager will invoke the function (only once); 
 - note: this the only possible way of controlling the passage of time when using an event-driven environment

Widget.after_cancel(id)
 -  the method cancels the planned invocation identified by the id argument.
 

"""

import tkinter as tk

def blink():
    global is_white
    if is_white:
        color = 'black'
    else:
        color = 'white'
    is_white = not is_white
    frame.config(bg=color)
    # we continue to encourage it every time the blink() function is invoked – 
    # this gives the application the ability to blink as long as the application is running.
    frame.after(500, blink)  # recursive call bc the function calls itself


is_white = True
window = tk.Tk()
frame = tk.Frame(window, width=200, height=100, bg='white')
# we initially encourage it to make the invocation before the frame widget is packed into the main window;
frame.after(500, blink)
frame.pack()
# window.mainloop()

""" 
destroy() method is very destructive. 
It removes the widget completely, not only from your sight, but also from the event manager’s memory, as the widget’s object is deleted and becomes inaccessible.
 - rule works recursively, destroying children on a destroyed widget

"""

import tkinter as tk

def suicide():
    frame.destroy()

window = tk.Tk()
frame = tk.Frame(window, width=200, height=100, bg='green')
button = tk.Button(frame, text="I'm a frame's child")
button.place(x=10, y=10)
frame.after(5000, suicide)
frame.pack()
# window.mainloop()

""" 
focus()
wi.focus_get()
 - focus_get() method returns a reference to the currently focused widget, 
                or None when no widget owns the focus (note: you can invoke the method from any widget, including the main window)
wi.focus_set()
 - focus_set() method focuses the widget from the method which was invoked, so you have to choose it carefully.

"""

import tkinter as tk

def flip_focus():
    if window.focus_get() is button_1:
        button_2.focus_set()
    else:
        button_1.focus_set()
    window.after(1000, flip_focus)

window = tk.Tk()
button_1 = tk.Button(window, text="First")
button_1.pack()
button_2 = tk.Button(window, text="Second")
button_2.pack()
window.after(1000, flip_focus)
window.mainloop()