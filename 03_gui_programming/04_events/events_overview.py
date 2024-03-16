
""" 
events are the fuel which propel the application’s movements. All events come to the event manager, 
which is responsible for dispatching them to all the application components. 
This also means that some of the events may launch some of your callbacks, 
which makes you responsible for preparing the proper reactions to the user’s actions.

If your widget is a clickable one, you can connect a callback to it using its command property

3 total widgets are clickable: Button, Checkbutton, Radiobutton
"""


import tkinter
from tkinter import messagebox

def clicked():
    messagebox.showinfo("info", "some\ninfo")  # everything in the info box is contained in this invocation

window = tkinter.Tk()
button_1 = tkinter.Button(window, text="Show info", command=clicked)
button_1.pack()
button_2 = tkinter.Button(window, text="Quit", command=window.destroy)
button_2.pack()
# window.mainloop()


import tkinter as tk
from tkinter import messagebox

def click():
    tk.messagebox.showinfo("Click!","I love clicks!")

window = tk.Tk()
label = tk.Label(window, text="Label")
label.pack()

button = tk.Button(window, text="Button", command=click)
button.pack(fill=tk.X)

frame = tk.Frame(window, height=30, width=100, bg="#55BF40")
frame.pack();

window.mainloop()

