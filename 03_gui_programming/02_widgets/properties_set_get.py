
""" 
widget's property is not just an object property. Although every widget is actually an object,
you can access its properties by using the dot notation. You have to use one of two possible ways of reading and setting widget properties’ values.

1) dict-like access and 2) the cget() and config() methods
"""

# rename widget property using it's built in dictionary
# old_val = Widget["prop"]
# Widget["prop"] = new_val

import tkinter as tk

def on_off():
    global button
    state = button["text"]
    if state == "ON":
        state = "OFF"
    else:
        state = "ON"
    button["text"] = state

window = tk.Tk()
button = tk.Button(window, text="OFF", command=on_off)
button.place(x=50, y=100, width=100)
# window.mainloop()

# two specialized widget methods, 
# the first named cget() designed to read the property’s value, and 
# the second named config(), which allows you to set a new value to the property
# old_val = Widget.cget("prop")
# Widget.config(prop=new_val)

import tkinter as tk

def on_off():
    global button
    state = button.cget("text")
    if state == "ON":
        state = "OFF"
    else:
        state = "ON"
    button.config(text=state)

window = tk.Tk()
button = tk.Button(window, text="OFF", command=on_off)
button.place(x=50, y=100, width=100)
window.mainloop()


