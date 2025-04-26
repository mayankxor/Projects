import tkinter as tk
from tkinter import messagebox
from mailtm import Email

root = tk.Tk()
root.geometry("500x300")
def create_status_bar(address: str, domain: str):
    frame = tk.Frame(master=root,bd=1, relief=tk.SUNKEN)
    frame.pack(side=tk.BOTTOM, fill=tk.X)
    left_label = tk.Label(master=frame, text=f"{address}@{domain}", bd=1, anchor=tk.W)
    left_label.pack(side=tk.LEFT, padx=5)
    


def create_new_email():
    client = Email()
    domain = client.domain
    chosen_mail = choose_mail.get()
    if chosen_mail == '':
        messagebox.showwarning("Empty handle passed.")
        return
    for i in chosen_mail:
        if i.isalnum():
            pass
        else:
            messagebox.showwarning(title="Invalid E-mail handle request")
            return
    chosen_mail = choose_mail.get()
    client.register(username=chosen_mail, domain=domain)
    start_button.destroy()
    choose_mail.destroy()

    #TODO: Try client = Email() out of the function to check if `client=Email()` makes the new address or is it `client.register()`
    print("Email created!\naddress: {}@{}".format(chosen_mail, domain))
    create_status_bar(address=chosen_mail, domain=domain)

    

choose_mail = tk.Entry(master=root)
choose_mail.pack()
start_button = tk.Button(master=root, text="Create a new E-mail address", command=create_new_email)
start_button.pack()


















































root.mainloop()