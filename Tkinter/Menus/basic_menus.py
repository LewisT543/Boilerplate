


import tkinter as tk
from tkinter import messagebox

def about_app():
    messagebox.showinfo("App", "The application\nthat does nothing")

def are_you_sure():
    if messagebox.askyesno("", "Are you sure you want to quit the App?"):
        window.destroy()

def open_file():
    messagebox.showinfo("Open doc", "We'll open a file here...")

window = tk.Tk()
window.title('Menus')
# Add main menu
main_menu = tk.Menu(window)
window.config(menu=main_menu)
# Add sub menu cascade
sub_menu_file = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="File", menu=sub_menu_file, underline=0)
# Add sub sub menu
sub_sub_menu_file = tk.Menu(sub_menu_file, tearoff=0)
sub_menu_file.add_cascade(label="Open recent file...", underline=5, menu=sub_sub_menu_file)

# Add items to submenu
for i in range(8):
    number = str(i + 1)
    sub_sub_menu_file.add_command(label=number + ". file.txt", underline=0)
# Manually adding a command to menu items
sub_menu_file.add_command(label="Open...", underline=0, command=open_file)
# Add seperator in list
sub_menu_file.add_separator()

# Add keyboard shortcuts
sub_menu_file.add_command(label='Quit', accelerator='Ctrl-Q', underline=0, command=are_you_sure)
window.bind_all('<Control-q>', are_you_sure)

window.mainloop()