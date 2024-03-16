
""" 
methods for coloring
1. 
2. 
3. mixing
    three primary colors: red (R), green (G) and blue (B). The phenomenon is utilized by the so-called RGB color model
    allows you to set the saturation of every of primary colors in the range <0..255> what gives 256 different saturation levels, 
        from color's absence (saturation 0) to full color's presence (saturation 255)
        When all the components are set to zero (absence of the colors), we get black as a result.
        When all the components are set to 255 (full presence of the colors), we get white as a result.

coloring parameters:
1. bg – background color
2. fg – foreground color
3. activebackground – background color when the widget is active (pressed)
4. activeforeground – foreground color when the widget is active (pressed)

bg and fg refer to raised buttons only 

tkinter color names: https://www.tcl.tk/man/tcl8.4/TkCmd/colors.html

how does mixing work...
    It's is done by a trick used extensively in web pages – 
        as a string starting with a hash (#) followed by 6 hexadecimal digits. 
        Each pair of the digits forms the value from range 0x00..0xFF (0..255) what determines the specific component level.
    
    #RRGGBB
    
    #000000 is black
    #FFFFFF is white
    #FF0000 is red
    #00FF00 is green
    #0000FF is blue
    #00FFFF is turquoise
    #FF00FF is violet
    #FFFF00 is yellow
    
    when all the components are set to the same value, equal neither to zero nor to 0xFF (e.g. #0F0F0F), you will get 254 shades of gray

"""

import tkinter as tk

window = tk.Tk()
button = tk.Button(window, text="Button #1", bg="black", fg="green", activebackground="red", activeforeground="orange")
button.pack()
# window.mainloop()

import tkinter as tk

window = tk.Tk()
button = tk.Button(window, text="Button #1",
                   bg="MediumPurple",
                   fg="LightSalmon",
                   activeforeground="LavenderBlush",
                   activebackground="HotPink")
button.pack()
# window.mainloop()

import tkinter as tk

window = tk.Tk()
button = tk.Button(window, text="Button #1",
                   bg="#9370DB",
                   fg="#FFA07A",
                   activeforeground="#FFF0F5",
                   activebackground="#FF69B4")
button.pack()
window.mainloop()

# color order in hex code is RED GREEN BLUE