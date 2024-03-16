
""" 
window controlled by you and your operating system
- os must be aware of anything you do to the window

"""

import tkinter as tk
from tkinter import messagebox


def click(*args):
    global counter
    if counter > 0:
        counter -= 1
    window.title(str(counter))


counter = 10
window = tk.Tk()
window.title(str(counter))
window.bind("<Button-1>", click)

# use low level tk commands to change the window logo
window.tk.call('wm', 'iconphoto', window._w, tk.PhotoImage(file='/Users/kylekristiansen/cherreco/python/03_gui_programming/07_window/institute.png')) # how to swap the icon photo
# window.bind("&lt;Button-1&gt;", lambda e: window.destroy())

def click_size(*args):
    global size, grows
    if grows:
        size += 50
        if size >= 700:
            grows = False
    else:
        size -= 50
        if size <= 100:
            grows = True
    window.geometry(str(size) + "x" + str(size))


size = 100
grows = True
# window.resizable(width=False, height=False)  # if you want to make the window NOT resizable
window.minsize(width=300, height=300)
window.maxsize(width=600, height=600)
window.geometry("500x500")

message = tk.Message(window, text="Click me to change window size!")
message.bind("<Button-1>", click_size)
message.pack()

def really():
    if messagebox.askyesno("?", "Wilt thou be gone?"):
        window.destroy()
        
window.protocol("WM_DELETE_WINDOW", really)

window.mainloop()
