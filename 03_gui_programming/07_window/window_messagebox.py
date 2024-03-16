
""" 
messagebox dialog behavior:
- title – a string displayed in the dialog’s title bar (it can’t be very long, of course);
- message – a string displayed inside the dialog; note: the \n plays its normal role and breaks up the message’s lines;
- options – a set of options shaping the dialog in a non-default way, two of which are useful to us:
    - default – sets the default (pre-focused) answer; usually, it’s focused on the button located first from the left; 
        this can be changed by setting the keyword argument with identifiers like CANCEL, IGNORE, OK, NO, RETRY, and YES;
    - icon – sets the non-default icon for the dialog: possible values are: ERROR, INFO, QUESTION, and WARNING.
"""

import tkinter as tk
from tkinter import messagebox


def question():
    # answer = messagebox.askyesno("?", "To be or not to be?")                          # question mark icon, returns True or False
    # answer = messagebox.askokcancel("?", "I'm going to format your hard drive")       # question mark icon, returns True or False
    # answer = messagebox.askretrycancel("?", "I'm going to format your hard drive")    # warning icon, returns True or False
    answer = messagebox.askquestion("?", "I'm going to format your hard drive")         # question mark icon, returns "yes" or "no"

    print(answer)

def question2():
    # answer = messagebox.showerror("!", "Your code does nothing!")                     # error icon, returns "ok"
    answer = messagebox.showwarning("Be careful!", "Big Brother is watching you!")      # warning icon, returns "ok"
    
    print(answer)

window = tk.Tk()
button = tk.Button(window, text="Ask the question!", command=question)
button.pack()

button2 = tk.Button(window, text="Alarming message", command=question2)
button2.pack()

window.mainloop()
