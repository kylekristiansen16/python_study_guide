
""" MENU
- a classic menu is actually a horizontal bar located at the top of the application window;
- the bar contains a number of horizontally deployed options, often referred to as items or entries;
- these options can have hot-keys (keyboard shortcuts enabling the user to quickly access selected operations without using a mouse; 
- usually, hot-keys are triggered by pressing Alt-hotkey on the keyboard)
- selecting a menu’s option (it doesn’t matter whether through a hotkey or by a mouse click) causes one of two effects:
    - it launches a callback bound to the option;
    - it unrolls a new menu (actually a submenu)
- if you want to have such a menu within your Tkinter application, you have to:
    - create a top-level menu object;
    - embed it inside the window;
    - bind a number of required submenus (this is called a cascade) or connect a single callback.

"""

import tkinter as tk
from tkinter import messagebox


def about_app():
    messagebox.showinfo("App", "The application\nthat does nothing")

def are_you_sure(event=None):
    if messagebox.askyesno("", "Are you sure you want to quit the App?"):
        window.destroy()

def open_file():
    messagebox.showinfo("Open doc", "We'll open a file here...")

window = tk.Tk()

# main menu creation
main_menu = tk.Menu(window) # create a menu object
window.config(menu=main_menu) # attach the menu to the window

# 1st main menu item: an empty (as far) submenu
sub_menu_file = tk.Menu(main_menu) # create a submenu object using main_menu as a parent
main_menu.add_cascade(label="File", menu=sub_menu_file, underline=0) # add the submenu as first item to the main menu

sub_menu_file.add_command(label="Open...", underline=0, command=open_file)

sub_sub_menu_file = tk.Menu(sub_menu_file, tearoff=0)
sub_menu_file.add_cascade(label="Open recent file...", underline=5, menu=sub_sub_menu_file)
sub_sub_menu_file.add_command(label="File 1", underline=0, command=open_file)

for i in range(6):
    number = str(i + 2)
    sub_sub_menu_file.add_command(label=number + ". file.txt", underline=0, command=open_file)


sub_menu_file.add_separator()
sub_menu_file.add_command(label="Quit", underline=0, accelerator="Ctrl-Q", command=are_you_sure) # accelerator: hotkey 

# 2nd main menu item: a simple callback
sub_menu_help = tk.Menu(main_menu)
main_menu.add_cascade(label="About...", menu=sub_menu_help, underline=1)

sub_menu_help.add_command(label="Help", underline=2, command=about_app)

window.bind_all("<Control-q>", are_you_sure) # create hotkey binding for quitting the window

window.mainloop()

""" A menu like this has one important disadvantage – it’s hard to use it without a mouse """

""" 
you have to create the menu,
then create a submenu on it
then add the submenu to the menu using add_cascade()
then add a command to the submenu using add_command()
"""
