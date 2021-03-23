

import tkinter as tk

string_variable = tk.StringVar()
int_variable = tk.IntVar()
float_var = tk.DoubleVar()
bool_variable = tk.BooleanVar()

# Getting and Setting
string_variable.set('Hi')
string_variable.get()

# Tracing
def r_observer(*args):
    print("Reading")

def w_observer(*args):
    print("Writing")
# r_observer will be called when string_variable is read
r_obsid = string_variable.trace("r", r_observer)
# w_observer will be called when string_variable is set
w_obsid = string_variable.trace('w', w_observer)
