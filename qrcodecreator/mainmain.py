import tkinter as tk
from tkinter import colorchooser
from PIL import Image, ImageTk
import qrcode
import random

ERROR_CORRECTION_DICT = {
	'L': 1,
	'M': 0,
	'Q': 3,
	'H': 2
}
ERROR_CORRECTION_NAMES_CHRONO = [ "Medium", "Low", "High", "Quarter"]
ERROR_CORRECTION_CHOICE = 0

VERSION = 1
VERSION_LIST = [i for i in range(1, 41)]

BOX_SIZE = 12

FILL_COLOR = "black"
BACK_COLOR = "white"

root = tk.Tk()
root.geometry("652x666")
root.title("QR Code Generator")

entry_label = tk.Label(master=root, text="Enter a string:")
entry_label.pack()

entry = tk.Entry(master=root, width=652)
entry.pack()


def generateqr():
	
	if entry.get():
		print("Clicked!")
		print(ERROR_CORRECTION_NAMES_CHRONO[ERROR_CORRECTION_CHOICE])
		qr = qrcode.QRCode(
		version=VERSION,
		error_correction=ERROR_CORRECTION_CHOICE,
		box_size=BOX_SIZE,
		border=2
		)
		print(ERROR_CORRECTION_CHOICE)
		string = entry.get()
		qr.add_data(string)
		img = qr.make_image(
			fill_color=FILL_COLOR,
			back_color=BACK_COLOR)
		img.save("qrcodemain.png")
		photo = tk.PhotoImage(file="D:\\Coding\\Projects\\qrcodecreator\\qrcodemain.png")
		photolabel.config(image=photo)
		photolabel.image = photo 
	# settings_button.lift()

def create_settings_window():
	sw = tk.Toplevel(root)
	sw.title("Settings")
	sw.geometry("652x666")
	def apply_settings():
		global ERROR_CORRECTION_CHOICE, VERSION, BOX_SIZE
		VERSION = version_selector.get()
		ERROR_CORRECTION_CHOICE = ERROR_CORRECTION_DICT[error_correction_selection.get()[0]]
		generateqr()
		sw.destroy()


	# Settings
	# Error Correction
	error_correction_options = ["Low", "Medium", "Quarter", "High"]

	error_correction_selection = tk.StringVar()
	error_correction_selection.set(ERROR_CORRECTION_NAMES_CHRONO[ERROR_CORRECTION_CHOICE])

	error_correction_menu = tk.OptionMenu(sw, error_correction_selection, *error_correction_options)
	error_correction_label = tk.Label(sw, text="Error Correction: ")
	error_correction_label.grid(row=0, column=0)
	error_correction_menu.grid(row=0, column=1)


	# Fill Color

	def take_fill_color():
		global FILL_COLOR
		global current_fill_color
		FILL_COLOR = colorchooser.askcolor()[1]
		current_fill_color = tk.Label(sw, bg=FILL_COLOR, width=10)
		current_fill_color.grid(row=1, column=1)
		print(FILL_COLOR)

	def take_back_color():
		global BACK_COLOR
		BACK_COLOR = colorchooser.askcolor()[1]
		current_back_color = tk.Label(sw, bg=BACK_COLOR, width=10)
		current_back_color.grid(row=2, column=1)
		print(BACK_COLOR)


	fill_color_label = tk.Label(sw, text="Fill Color: ")
	current_fill_color = tk.Label(sw, bg=FILL_COLOR, width=10)
	fill_color_chooser_button = tk.Button(sw, text="Change", command=take_fill_color)

	back_color_label = tk.Label(sw, text="Background Color: ")
	current_back_color = tk.Label(sw, bg=BACK_COLOR, width=10)
	back_color_chooser_button = tk.Button(sw, text="Change", command=take_back_color)

	fill_color_label.grid(row=1, column=0)
	current_fill_color.grid(row=1, column=1)
	fill_color_chooser_button.grid(row=1, column=2)

	back_color_label.grid(row=2, column=0)
	current_back_color.grid(row=2, column=1)
	back_color_chooser_button.grid(row=2, column=2)

	# Version
	def version_validator(input):
		if input == "":
			return True
		try:
			value = int(input)
			return 1<=value<=40
		except ValueError:
			return False
	version_tracker = tk.IntVar(value=VERSION)
	reg = (sw.register(version_validator), '%P')
	version_label = tk.Label(sw, text="Version: ")
	version_label.grid(row=3, column=0)
	version_selector = tk.Spinbox(sw, from_=1, to_=40, validate="key", validatecommand=reg, textvariable=version_tracker, width=4)
	version_selector.grid(row=3, column=1)
	apply_button = tk.Button(sw, text="Apply", command=apply_settings)
	apply_button.place(anchor="se", relx=1, rely=1)

	sw.grab_set()
	sw.wait_window()

root.mainloop()
