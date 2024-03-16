
""" 
canvas.create_image():
Option name	Option meaning
image	an object of the PhotoImage class containing the image itself; 
            the PhotoImage class constructor needs a keyword argument named file pointing to a bitmap file 
            (note: only GIF and PNG formats are accepted); the argument should specify the file’s path
            
if you want a jpeg image...
    from PIL import ImageTk, Image
    build an object of the Image() class and use its open() method to fetch the bitmap from the file (the argument should specify the file’s path)
    convert this object into a PhotoImage class object using an ImageTk function of the same name;
    
"""

import tkinter as tk
import PIL

window = tk.Tk()
canvas = tk.Canvas(window, width=800, height=800, bg='green')

image = tk.PhotoImage(file='/Users/kylekristiansen/cherreco/python/03_gui_programming/07_window/institute.png')
canvas.create_image(400, 400, image=image)

""" create image with jpeg
jpg = PIL.Image.open('logo.jpg')
image = PIL.ImageTk.PhotoImage(jpg)
canvas.create_image(200, 200, image=image)
"""

button = tk.Button(window, text="Quit", command=window.destroy)

canvas.grid(row=0)
button.grid(row=1)

window.mainloop()

