import tkinter as tk
from tkinter import Toplevel
from pymailtm import MailTm

client = MailTm()
domains = client._get_domains_list()
root = tk.Tk()

account = client.get_account()
print(account)


root.title("Simple Tkinter App with Menu")
root.geometry("500x300")




def opening_domains_list_window():
    domains_list_window = Toplevel(master=root)
    domains_list_window.title(string="List of available domains")
    for i in domains:
        label = tk.Label(master=domains_list_window, text=f"{i}", font=("Arial", 14), wraplength=350)
        label.pack(expand=True, fill="both", padx=10, pady=10)
    

menu_bar = tk.Menu(root)

view_menu = tk.Menu(menu_bar, tearoff=0)
view_menu.add_command(label="List available domains", command=opening_domains_list_window)
menu_bar.add_cascade(label="View", menu=view_menu)

root.config(menu=menu_bar)


mail_field = tk.Entry(master=root)
mail_field.insert(0, "Waiting...")
mail_field.config(state="readonly")
mail_field.pack(address)



root.mainloop()