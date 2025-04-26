import tkinter as tk

def selection_changed(choice):
	label.config(text=f"Selected: {choice}")

root = tk.Tk()
root.geometry("300x200")
error_correction_options = ["Low", "Medium", "Quarter", "High"]

selected_option = tk.StringVar()
selected_option.set(options[0])

dropdown = tk.OptionMenu(root, selected_option, *options, command=selection_changed)
dropdown.pack(pady=20)
label = tk.Label(root, text="Selected: None")
label.pack()
root.mainloop()