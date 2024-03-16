
""" 
using the Entry, Radiobutton and Button widgets,
managing widgets with the grid manager,
checking the validity of user input and handling errors.

You need a calculator. A very simple and very specific calculator. 
Look at the picture (see slack) - it contains two fields that the user can use to enter arguments, a radio button to select the operation to perform, and a button initiating the evaluation:

We expect the calculator to behave in the following way:

if both fields contain valid (integer or float) numbers, clicking the Evaluate button should display an info window showing the evaluation's result;
if any of the fields contains invalid data (e.g., a string, or a field is empty), clicking the Evaluate button should present an error window describing the problem, and the focus should be moved to the field causing the problem.
Don't forget to protect your code from dividing by zero, and use the grid manager to compose the window interior.
"""

import tkinter as tk
from tkinter import messagebox

def check_left(*args):
    global left_0
    left = left_var.get()
    if left.isnumeric() or len(left) == 0:
        left_0 = left
    else:
        messagebox.showwarning("Warning!", "Only int & float entries allowed on left")
        left_var.set(left_0)

def check_right(*args):
    global right_0
    right = right_var.get()
    if right.isnumeric() or len(right) == 0:
        right_0 = right
    else:
        right_var.set(right_0)
        messagebox.showwarning("Warning!", "Only int & float entries allowed on left")
       
def show_info(value):
    messagebox.showinfo("Result!", f"Operation evaluated to: {value}")
 
def calculate(*args):
    op = operation.get()
    left = left_var.get()
    right = right_var.get()
    if len(left) == 0 or len(right) == 0:
        messagebox.showerror("Error!", "Please enter valid numbers for calculation!")
        return
    if right == 0:
        messagebox.showerror("Error!", "Trying to divide by 0")
        return
      
    if op == 1:  # +
        result = float(left) + float(right)
        show_info(result)
    elif op == 2:  # -
        result = float(left) - float(right)
        show_info(result)
    elif op == 3:  # *
        result = float(left) * float(right)
        show_info(result)
    elif op == 4:  # /
        result = float(left) / float(right)
        show_info(result)
    else:
        messagebox.showerror("Error!", f"Unexpected operation value of {op}")
        
    
wnd = tk.Tk()

left_0 = 0
right_0 = 0

left_var = tk.StringVar()
left_var.set(0)
left_var.trace("w", check_left)
right_var = tk.StringVar()
right_var.set(0)
right_var.trace("w", check_right)

left_entry = tk.Entry(wnd, textvariable=left_var)
right_entry = tk.Entry(wnd, textvariable=right_var)

left_entry.grid(row=1, column=1, rowspan=4)
right_entry.grid(row=1, column=3, rowspan=4)

operation = tk.IntVar()
operation.set(1)

rb_plus = tk.Radiobutton(wnd, text='+', variable=operation, value=1)
rb_minus = tk.Radiobutton(wnd, text='-', variable=operation, value=2)
rb_times = tk.Radiobutton(wnd, text='*', variable=operation, value=3)
rb_divide = tk.Radiobutton(wnd, text='/', variable=operation, value=4)

rb_plus.grid(row=1, column=2)
rb_minus.grid(row=2, column=2)
rb_times.grid(row=3, column=2)
rb_divide.grid(row=4, column=2)

evaluate = tk.Button(wnd, text='Evaluate', command=calculate)
evaluate.grid(row=5, column=1, columnspan=3)

wnd.mainloop()
