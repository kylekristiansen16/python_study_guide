

import tkinter as tk
from tkinter import messagebox

def on_off():
    global switch
    if switch:
        button_2.config(command=do_nothing)
        button_2.config(text="Gee!")
    else:
        button_2.config(command=peekaboo)
        button_2.config(text="Peekaboo!")
    switch = not switch

def peekaboo():
    messagebox.showinfo("", "PEEKABOO!")

def do_nothing():
    pass

switch = True
window = tk.Tk()
buton_1 = tk.Button(window, text="On/Off", command=on_off)
buton_1.pack()
button_2 = tk.Button(window, text="Peekaboo!", command=peekaboo)
button_2.pack()
window.mainloop()


