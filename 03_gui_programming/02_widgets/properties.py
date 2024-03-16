
""" 
1. font 
  - font=("font_family", "font_size", "font_style")
  - fond=("font_family", "font_size")
  
style: 
"bold"
"italic"
"underline"
"overstrike"
"""

import tkinter as tk

window = tk.Tk()
label_1 = tk.Label(window, text="Quick brown fox jumps over the lazy dog")
label_1.grid(column=0, row=0)
label_2 = tk.Label(window, text="Quick brown fox jumps over the lazy dog", font=("Times", "12"))
label_2.grid(column=0, row=1)
label_3 = tk.Label(window, text="Quick brown fox jumps over the lazy dog", font=("Arial", "16", "bold"))
label_3.grid(column=0, row=2)
# window.mainloop()

""" 
2. size
  - dimensions:
  
Widget property name	Property role
borderwidth	| The width of the 3D-frame surrounding some widgets (e.g., Button)
highlightthickness |	The width of the additional frame drawn around the widget when it gains the focus
padx
pady | 	The width/height of an additional empty space/margin around the widget
wraplength |	If the text filling the widget becomes longer than this property’s value, it will be wrapped (possibly more than once)
height |	The height of the widget
underline |	The index of the character inside the widget’s text, which should be presented as underlined or -1 otherwise (the underlined letter/digit can be used as a shortcut key, but it needs a specialized callback to work – no automation here, sorry)
width |	The width of the widget
"""

import tkinter as tk

window = tk.Tk()
button_1 = tk.Button(window, text="Ordinary button")
button_1.pack()
button_2 = tk.Button(window, text="Exceptional button")
button_2.pack()
button_2["borderwidth"] = 10
button_2["highlightthickness"] = 10
button_2["padx"] = 10
button_2["pady"] = 5
button_2["underline"] = 1
# window.mainloop()

""" 
3. color
Widget property name	Property role
background
bg	The color of the widget’s background (you can freely use either of these two forms)
foreground
fg	The color of the widget’s foreground (note: it can mean different things in different widgets; in general, it’s used to specify text color)
activeforeground
activebackground	Like bg and fg but used when the widget becomes active
disabledforeground	The width of the widget
"""

import tkinter as tk

window = tk.Tk()
button_1 = tk.Button(window, text="Ordinary button");
button_1.pack()
button_2 = tk.Button(window, text="Colorful button")
button_2.pack()
button_2.config(bg ="#000000")
button_2.config(fg ="yellow")
button_2.config(activeforeground ="#FF0000")
button_2.config(activebackground ="green")
# window.mainloop()


""" 
4. anchor
  - an imaginary (invisible) point inside the widget to which the text (if any) is anchored
  - name the anchor using cardinal directions (N, NE, E, SE, S, SW, W, NW, CENTER)
  
"""

import tkinter as tk

window = tk.Tk()
button_1 = tk.Button(window, text="Regular button");
button_1["anchor"] = tk.E
button_1["width"] = 20  # pixels!
button_1.pack()
button_2 = tk.Button(window, text="Another button")
button_2["anchor"] = tk.SW  # config isn't the only way to set properties on a widget
button_2["width"] = 20
button_2["height"] = 3  # rows
button_2.pack()
# window.mainloop()

""" 
5. cursor
  - cursor can change when it enters a certain area of the widget
  - cursors: https://www.tcl.tk/man/tcl8.4/TkCmd/cursors.html
  
"""

import tkinter as tk

window = tk.Tk()
label_1 = tk.Label(window, height=3, text="arrow", cursor="arrow")
label_1.pack()
label_2 = tk.Label(window, height=3, text="clock", cursor="clock")
label_2.pack()
label_3 = tk.Label(window, height=3, text="heart", cursor="heart")
label_3.pack()
window.mainloop()

# use config to set a widget's properties
# or use the property name as a key in a dictionary