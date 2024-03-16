
""" 
geometry managers:
- only one can be used for a given window
    - place - most detailed, absolute positioning (pixel by pixel)
    - pack - most common, relative positioning - allows tkinter to manage the layout
    - grid - most flexible, relative positioning - allows tkinter to manage the layout
        - gives you a chance to express your general wishes and tries to deploy the widgets according to them
"""

"""         
PLACE
- invoked from the widget's object
- height=h – the widget's desired height measured in pixels; if the parameter is omitted, the widget's height will be determined automatically;
- width=w – the widget's desired width measured in pixels; if the parameter is omitted, the widget's width will be determined automatically;
- x=x – the widget's top-left pixel's horizontal coordinate measured relative to the home window's top-left corner;
- y=y – the widget's top-left pixel's vertical coordinate measured relative to the home window's top-left corner.

"""

import tkinter as tk

window = tk.Tk()
button_1 = tk.Button(window, text="Button #1")
button_2 = tk.Button(window, text="Button #2")
button_3 = tk.Button(window, text="Button #3")
button_1.place(x=10, y=10, width=150)
button_2.place(x=20, y=40)
button_3.place(x=30, y=70, height=50)
# window.mainloop()

""" 
GRID -
- column=c – deploys the widget in the column number c; note: the columns' numbers start from zero, and if you omit this argument, the manager will assume 0 (the left-most column)
- row=r – deploys the widget in the row number r; if you omit this argument, the manager will assume the first free row starting from the top;
- columnspan=cs – determines how many neighboring columns the widget occupies; the parameter defaults to 1 (the widget won't cross a single grid's cell)
- rowspan=rs – works as columnspan but refers to rows.
"""

import tkinter as tk

window = tk.Tk()
button_1 = tk.Button(window, text="Button #1")
button_2 = tk.Button(window, text="Button #2")
button_3 = tk.Button(window, text="Button #3")
button_1.grid(row=0, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=2, column=2)
# window.mainloop()

# OR

import tkinter as tk

window = tk.Tk()
button_1 = tk.Button(window, text="Button #1")
button_2 = tk.Button(window, text="Button #2")
button_3 = tk.Button(window, text="Button #3")
button_1.grid(row=0, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=2, column=0, columnspan=2)  # 2 columns only needed for the window, 3rd button will span both
window.mainloop()

""" 
PACK - packs subsequent widgets into the window's interior. This means that the order in which the widgets are packed matters
side=s – forces the manager to pack the widgets in a specified direction, where s can be specified as TOP, BOTTOM, LEFT, RIGHT
fill=f – suggests to the manager how to expand the widget if you want it to occupy more space than the default, while f should be specified as: NONE, X, Y, or BOTH

We suggest you use it only as a temporary solution to help you get a working application quickly, 
but if you want your application to look nice and to be legible and clearyou'd better forget about pack()
and use either grid() (in simpler cases) or place().
"""

import tkinter as tk

window = tk.Tk()
button_1 = tk.Button(window, text="Button #1")
button_2 = tk.Button(window, text="Button #2")
button_3 = tk.Button(window, text="Button #3")
button_1.pack()
button_2.pack()
button_3.pack()
# window.mainloop()

# OR

window = tk.Tk()
button_1 = tk.Button(window, text="Button #1")
button_2 = tk.Button(window, text="Button #2")
button_3 = tk.Button(window, text="Button #3")
button_1.pack(side=tk.RIGHT)
button_2.pack()
button_3.pack()
# window.mainloop()

# OR

window = tk.Tk()
button_1 = tk.Button(window, text="Button #1")
button_2 = tk.Button(window, text="Button #2")
button_3 = tk.Button(window, text="Button #3")
button_1.pack(side=tk.RIGHT, fill=tk.Y)
button_2.pack()
button_3.pack()
window.mainloop()
