import tkinter as tk
from tkinter import Toplevel
import random
from pymailtm import MailTm



# Function to open a new window
def open_new_window(title, text):
    new_window = Toplevel(root)
    new_window.title(title)
    new_window.geometry("400x200")
    label = tk.Label(new_window, text=text, font=("Arial", 14), wraplength=350)
    label.pack(expand=True, fill="both", padx=10, pady=10)

# Random text generator
def random_text():
    texts = [
        "This is the first random text. Hello, world!",
        "Here is some more random text. Python is fun!",
        "Keep exploring tkinter for cool apps!",
        "Learning tkinter step by step is rewarding.",
        "This is just another random sentence."
    ]
    return random.choice(texts)

# Main app window
root = tk.Tk()
root.title("Simple Tkinter App with Menu")
root.geometry("500x300")

# Create a menu bar
menu_bar = tk.Menu(root)

# Adding different bars to the menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Option 1", command=lambda: open_new_window("Option 1", random_text()))
file_menu.add_command(label="Option 2", command=lambda: open_new_window("Option 2", random_text()))
menu_bar.add_cascade(label="File", menu=file_menu)

edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Option 3", command=lambda: open_new_window("Option 3", random_text()))
edit_menu.add_command(label="Option 4", command=lambda: open_new_window("Option 4", random_text()))
menu_bar.add_cascade(label="Edit", menu=edit_menu)

view_menu = tk.Menu(menu_bar, tearoff=0)
view_menu.add_command(label="Option 5", command=lambda: open_new_window("Option 5", random_text()))
menu_bar.add_cascade(label="View", menu=view_menu)

# Attach the menu bar to the root window
root.config(menu=menu_bar)

# Run the application
root.mainloop()
