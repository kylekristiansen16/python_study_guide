
""" canvas
a flat, rectangular surface that you can cover with drawings, text, frames, and other widgets
it can scroll itself and react to many events

Property name	Property role
borderwidth	canvas border’s width in pixels (default: 2)
background (bg)	canvas border’s color (default: the same as the underlying window’s color)
height	canvas height (in pixels)
width	canvas width (in pixels)

for create_line() method:
Option name	Option meaning
arrow	normally, the chain ends aren’t marked in any special way, but you may want them to be finished with arrowheads; 
    setting the arrow option to FIRST results in drawing an arrowhead at the chain’s beginning, LAST at the chain’s end, BOTH at both sides of the chain.
fill	chain color (setting the option to an empty string causes the line to be transparent)
smooth	setting it to True rounds the chain’s corners using a set of connected parabolas
width	line width (default: 1 pixel)

for create_rectangle() method:
Option name	Option meaning
outline	rectangle edge color (if specified as an empty string, the edge is transparent)
fill	rectangle interior color
width	rectangle edge width in pixels (default: 1)

for create_arc() method:
Option name	Option meaning
style	can be set to one of the following: PIESLICE (default), CHORD and ARC; the shape of the resulting drawing is presented here:
            Pieslice, chord & arch.png
start	the angle (in degrees) of the arc’s start relative to the X-axis (e.g., 90 means the highest point of the ellipse, while 0 is the right-most point. The default is 0)
extent	the arc’s span (in degrees) relative to the start point; note: the span is calculated counter-clockwise. The default is 90 (a quarter of an ellipse)
"""

import tkinter as tk


window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg='green')

# canvas.create_line(10, 380, 200, 10, 380, 380, 10, 380,                   # creates polygonal chain, (x0, y0, x1, y1, ..., xn, yn)
#                    arrow=tk.BOTH, fill='red', smooth=True, width=3)

# canvas.create_rectangle(200, 100, 300, 300,                               # creates rectangle using only the opposite corners, (x0, y0, x1, y1)
#                         outline='white', width=5, fill='blue')

# canvas.create_polygon(20, 380, 200, 68, 380, 380,                         # the final segment connecting x0, y0 with xn, yn is drawn automatically
#                       outline='purple', width=5, fill='yellow')

# canvas.create_oval(100, 100, 300, 300,                                    # creates oval using only the opposite corners of surrounding rectangle, (x0, y0, x1, y1)
#                    outline='red', width=20, fill='white')

canvas.create_arc(10, 100, 380, 300, 
                  outline='red', width=5)
canvas.create_arc(10, 100, 380, 300, 
                  outline='blue', width=5, style=tk.CHORD, start=90, fill='white')
canvas.create_arc(10, 100, 380, 300, 
                  outline='orange', width=5, style=tk.ARC, start=180, extent=180)
  
button = tk.Button(window, text="Quit", command=window.destroy)
canvas.grid(row=0)
button.grid(row=1)
window.mainloop()