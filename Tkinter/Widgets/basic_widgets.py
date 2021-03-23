

import tkinter as tk

# Button
button  = tk.Button(<parent>, text='text', textvariable=<tk.observer_variable_str>, command=<callback_function>)
# Checkbutton
checkbutton = tk.Checkbutton(<parent>, text='text', variable=<tk.observer_variable_int>, command=<callback_function>)
# Radiobuttons
radio_var = tk.IntVar()
radiobutton = tk.Radiobutton(<parent>, text='text', variable=radio_var, value=1, command=<callback_function>)

# Label
label = tk.Label(<parent>, textvariable=<tk.observer_variable_str>, height=y, width=x)
# Message
message = tk.Message(<parent>, text='text', textvariable=<tk.observer_variable_str>, width=x)
# Frame
frame = tk.Frame(<parent>, width=x, height=y, bg='white')
# LabelFrame
labelframe = tk.LabelFrame(<parent>, width=x, height=y, labelanchor='n')
# Entry
entry_var = tk.StringVar()
entry = tk.Entry(<parent>, textvariable=entry_var)
