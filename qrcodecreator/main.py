import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk
from IPython.display import display

def CreateQR():
	# Creating the image
	string = entry.get()
	img = qrcode.make(string)
	img.save("{}.png".format(string))

	# Load the image
	image = Image.open("{}.png".format(string))
	image = ImageTk.PhotoImage(image)
	image_label = tk.Label(root, image=image)
	image_label.pack()
	print("Clicked!")

# Create main window
root = tk.Tk()
root.title("Simple App")
root.geometry("700x450")

# Label
label = tk.Label(root, text="Enter the string: ")
label.pack(pady=10)

# Entry (Text input)
entry = tk.Entry(root, width=25)
entry.pack(pady=5)

# generate Button
generate_button = tk.Button(
    root,
    text="Generate",
    command=CreateQR,
    bg="#4CAF50",  # Green color
    fg="white"
)
generate_button.pack(pady=5)

# Quit Button
#quit_button = tk.Button(
 #   root,
  #  text="Quit",
   # command=root.destroy,
    #bg="#f44336",  # Red color
    #fg="white"
#)
#quit_button.pack(pady=5)

# Start the GUI event loop
root.mainloop()