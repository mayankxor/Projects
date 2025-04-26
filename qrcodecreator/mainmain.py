import tkinter as tk
from PIL import Image, ImageTk
import qrcode
import random

ERROR_CORRECTION_DICT = {
	'L': 1,
	'M': 0,
	'Q': 3,
	'H': 2
}
ERROR_CORRECTION_CHOICE = 0

"""
L -> 1
M -> 0
Q -> 3
H -> 2

"""

root = tk.Tk()
root.geometry("652x666")
root.title("QR Code Generator")

entry_label = tk.Label(master=root, text="Enter a string:")
entry_label.pack()

entry = tk.Entry(master=root, width=652)
entry.pack()


def generateqr():
	print("Clicked!")
	qr = qrcode.QRCode(
	version=1,
	error_correction=ERROR_CORRECTION_CHOICE,
	box_size=12,
	border=2
	)
	print(ERROR_CORRECTION_CHOICE)
	string = entry.get()
	qr.add_data(string)
	img = qr.make_image(
		fill_color="black",
		back_color="white")
	img.save("qrcodemain.png")
	photo = tk.PhotoImage(file="D:\\Coding\\Projects\\qrcodecreator\\qrcodemain.png")
	photolabel.config(image=photo)
	photolabel.image = photo 
	settings_button.lift()

def create_settings_window():
	sw = tk.Toplevel(root)
	sw.title("Settings")
	sw.geometry("652x666")
	def apply_settings():
		global ERROR_CORRECTION_CHOICE
		ERROR_CORRECTION_CHOICE = ERROR_CORRECTION_DICT[error_correction_selection.get()[0]]
		print(type(ERROR_CORRECTION_CHOICE))
		print(ERROR_CORRECTION_CHOICE)
		generateqr()
		sw.destroy()


	# Settings
	# Error Correction
	error_correction_options = ["Low", "Medium", "Quarter", "High"]

	error_correction_selection = tk.StringVar()
	error_correction_selection.set(error_correction_options[1])

	error_correction_menu = tk.OptionMenu(sw, error_correction_selection, *error_correction_options)
	error_correction_label = tk.Label(sw, text="Error Correction: ")
	error_correction_label.grid(row=0, column=0)
	error_correction_menu.grid(row=0, column=1)





	settings_list = [error_correction_selection]


	apply_button = tk.Button(sw, text="Apply", command=apply_settings)
	apply_button.place(anchor="se", relx=1, rely=1)




	sw.grab_set()
	sw.wait_window()



generate_button = tk.Button(master=root, text="Generate", command = generateqr)
generate_button.pack()
root.bind("<Return>", lambda event: generateqr())

settings_image = tk.PhotoImage(file="Settingsx2.png")
settings_button = tk.Button(master=root, image=settings_image, command=create_settings_window)
settings_button.place(anchor="se", relx=1, rely=1)
settings_button.lift()


photolabel = tk.Label(master=root)
photolabel.pack()

















































































































































































































































root.mainloop()
