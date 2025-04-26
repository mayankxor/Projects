import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image  # Requires Pillow

def submit_name():
    name = entry.get()
    if not name:
        name = "Guest"
    messagebox.showinfo("Greeting", f"Hello, {name}!")

# Create main window
root = tk.Tk()
root.title("App with Image")
root.geometry("300x280")  # Adjust window height

# ================== Add Image ==================
try:
    # Load image (resize if needed)
    img = Image.open("Wooohooo.jpg")  # Replace with your image path
    img = img.resize((100, 100), Image.Resampling.LANCZOS)  # (width, height)
    photo_img = ImageTk.PhotoImage(img)
    
    # Create label to hold the image
    img_label = tk.Label(root, image=photo_img)
    img_label.image = photo_img  # Keep a reference to avoid garbage collection
    img_label.pack(pady=10)
except Exception as e:
    print(f"Error loading image: {e}")
# ===============================================

# Name entry widgets
label = tk.Label(root, text="Enter your name:")
label.pack(pady=5)

entry = tk.Entry(root, width=25)
entry.pack(pady=5)

# Buttons
greet_button = tk.Button(
    root,
    text="Submit",
    command=submit_name,
    bg="#4CAF50",
    fg="white"
)
greet_button.pack(pady=5)

quit_button = tk.Button(
    root,
    text="Quit",
    command=root.destroy,
    bg="#f44336",
    fg="white"
)
quit_button.pack(pady=5)

root.mainloop()