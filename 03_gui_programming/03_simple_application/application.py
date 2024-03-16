
""" 

Objects of the IntVar class are used by tkinter to organize internal communication between different widgets. 
    A regular variable can't play such a role

"""

import tkinter as tk

window = tk.Tk()

label = tk.Label(window, text = "Little label:")  # label = non-clickable, short textual information
label.pack()

frame = tk.Frame(window, height=30, width=100, bg="#000099")  # frame = non-clickable, container for other widgets, used for grouping
frame.pack()

button = tk.Button(window, text="Button")  # doesn't do anything yet
button.pack(fill=tk.X)

switch = tk.IntVar()    # organize internal communication between different widgets
switch.set(1)           # cannot use "=" assignment on IntVar objects

# setting variable=switch creates bidirectional link between the variable and the checkbutton
# if the variable changes, the checkbutton is updated
checkbutton = tk.Checkbutton(window, text="Check Button", variable=switch)  # checkbutton = clickable, can be selected or deselected (two-state selection)
checkbutton.pack()

entry = tk.Entry(window, width=30)  # entry = clickable, single-line text field
entry.pack()

# Radiobuttons always work in groups, they are bound by sharing the same variable (switch)
radiobutton_1 = tk.Radiobutton(window, text="Steak", variable=switch, value=0)
radiobutton_1.pack()
radiobutton_2 = tk.Radiobutton(window, text="Salad", variable=switch, value=1)
radiobutton_2.pack()

window.mainloop()
