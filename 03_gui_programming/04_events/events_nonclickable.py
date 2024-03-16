

""" 
Fortunately, you’re still able to bind a callback to any of the events it may receive (including clicks, of course)
and this is done with a method named – it couldn’t be anything else – bind():

widget.bind(event, callback)

Q: What is an event from the event controller’s point of view?
A: It’s an object carrying some useful info about what actually happens when the event has been induced (by the user or by another factor).

Q: How are the events identified?
A: By unique names – each event has its own name and the name is just a unified string.

widget.bind(event, callback)

events v
Event name	Event role
<Button-1>	Single left-click (if your mouse is configured for a right-handed user)
<Button-2>	Single middle-click
<Button-3>	Single right-click
<ButtonRelease-1>	Left mouse button release

Note: there are also events named <ButtonRelease-2> and <ButtonRelease-3>
<DoubleButton-1>	Double left-click

Note: there are also events named <DoubleButton-2> and <DoubleButton-3>

Note again: the <Button-1> event is a part of <DoubleButton-1> too; if you assign a callback to <Button-1>, it will be launched, too!

Event name	Event role
<Enter>	Mouse cursor appears over the widget
<Leave>	Mouse cursor leaves the widget area
<Focus-In>	The widget gains the focus
<Focus-Out>	The widget loses the focus
<Return>	The user presses the Enter/Return key
<Key>	The user presses any key

Event name	Event role
x	The user presses x key (x can be neither a space nor the < key)   !!!!
<space>	The user presses the spacebar
<less>	The user presses the < key
<Cancel>	The user presses the key/keys used by the current OS to stop the program (e.g., Ctrl-C or Ctrl-Break)
<BackSpace>	The user presses the Backspace key
<Tab>	The user presses Tab key

Event name	Event role
<Shift_L>	The user presses one of the Shift keys
<Control_L>	The user presses one of the Control keys
<Alt_L>	The user presses one of the Alt keys
<Pause>	The user presses the Pause key
<Caps_Lock>	The user presses the Caps Lock key
<Esc>	The user presses the Escape keys

Event name	Event role
<Prior>	The Page Up key
<Next>	The Page Down key
<End>	The End key
<Home>	The Home key
<Left>
<Right>
<Up>
<Down>	Cursor (arrows) keys
<Num_Lock>
<Scroll_Lock>	The two Lock keys
<Shift-x>
<Alt-x>
<Control-x>	The x key has been pressed along with any of the Shift, Alt, or Control keys

a callback designed for usage with the command property/parameter is a parameterless function;
a callback intended to cooperate with the bind() method is a one-parameter function (the callback’s argument carries some info about the captured event)

"""

import tkinter as tk
from tkinter import messagebox

def click(event=None):
    tk.messagebox.showinfo("Click!", "I love clicks!")

window = tk.Tk()
label = tk.Label(window, text="Label")
label.bind("<Button-1>", click)   # Line I
label.pack()

button = tk.Button(window, text="Button", command=click)
button.pack(fill=tk.X)

frame = tk.Frame(window, height=30, width=100, bg="#55BF40")
frame.bind("<Button-1>", click)   # Line II
frame.pack()

window.mainloop()

