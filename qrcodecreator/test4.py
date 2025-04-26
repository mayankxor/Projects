import tkinter as tk
from PIL import Image, ImageTk
import qrcode
import random

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
	error_correction=qrcode.constants.ERROR_CORRECT_M,
	box_size=12,
	border=2
	)
	string = entry.get()
	qr.add_data(string)
	img = qr.make_image(
		fill_color="black",
		back_color="white")
	img.save("qrcode.png")
	photo = tk.PhotoImage(file="D:\\Coding\\Projects\\qrcodecreator\\qrcode.png")
	photolabel.config(image=photo)
	photolabel.image = photo
	settings_button.lift()


def create_settings_window():
	sw = tk.Toplevel(root)
	sw.title("Settings")
	sw.geometry("552x566")
	sw.grab_set()
	sw.wait_window()



generate_button = tk.Button(master=root, text="Generate", command = generateqr)
generate_button.pack()
root.bind("<Return>", lambda event: generateqr())

settings_image = tk.PhotoImage(file="Settingsx2.png")
settings_button = tk.Button(master=root, image=settings_image, command=create_settings_window)
settings_button.place(anchor="se", relx=1, rely=1)
settings_button.lift()

error_correction_options = ["Low", "Medium", "Quarter", "High"]


photolabel = tk.Label(master=root)
photolabel.pack()

# Settings

















































































































































































































































root.mainloop()
