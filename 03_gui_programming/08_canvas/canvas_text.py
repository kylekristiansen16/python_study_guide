
""" 
canvas.create_text():
Option name	Option meaning
fill	text color
font	text font
justify	text justification: LEFT (default), CENTER, RIGHT
text	text to display (\n works as expected)
width	normally, the rectangle is as wide as the longest text line; using the width option forces the text to be aligned to that size
"""

import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg='blue')
canvas.create_text(200, 200, 
                   text="Mary\nhad\na\nlittle\nlamb",
                   font=("Times","40","bold"),
                   justify=tk.CENTER,
                   fill='white')
button = tk.Button(window, text="Quit", command=window.destroy)
canvas.grid(row=0)
button.grid(row=1)
window.mainloop()
