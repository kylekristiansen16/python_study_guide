

import tkinter as tk

def on_off():
    global switch
    if switch:
        label.unbind("<Button-1>")
    else:
        label.bind("<Button-1>", rhyme)
    switch = not switch

def rhyme(dummy):
    global word_no, words
    word_no += 1
    label.config(text=words[word_no % len(words)])

switch = True
words = ["Old", "McDonald", "Had", "A", "Farm"]
word_no = 0
window = tk.Tk()
button = tk.Button(window, text="On/Off", command=on_off)
button.pack()
label = tk.Label(window, text=words[0])
label.bind("<Button-1>", rhyme)
label.pack()
# window.mainloop()


import tkinter as tk
from tkinter import messagebox

def hello(dummy):
    messagebox.showinfo("", "Hello!")

window = tk.Tk()
button = tk.Button(window, text="On/Off")
button.pack()
label = tk.Label(window, text="Label")
label.pack()
frame = tk.Frame(window, bg="yellow", width=100, height=20)
frame.pack()
window.bind_all("<Button-1>", hello)  # able to bind all widgets to the same event
window.mainloop()
