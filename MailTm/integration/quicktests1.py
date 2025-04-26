import tkinter as tk

class StatusBar:
    def __init__(self, master):
        # Create a frame at the bottom to act as status bar
        self.status_frame = tk.Frame(master, bd=1, relief=tk.SUNKEN)
        self.status_frame.pack(side=tk.BOTTOM, fill=tk.X)

        # Left section (like current file/mode)
        self.left_label = tk.Label(
            self.status_frame, 
            text="Ready", 
            bd=1, 
            anchor=tk.W
        )
        self.left_label.pack(side=tk.LEFT, padx=5)

        # Right section (like line/column info)
        self.right_label = tk.Label(
            self.status_frame, 
            text="Ln 1, Col 1", 
            bd=1, 
            anchor=tk.E
        )
        self.right_label.pack(side=tk.RIGHT, padx=5)

        # Middle section (optional)
        self.middle_label = tk.Label(
            self.status_frame, 
            text="", 
            bd=1
        )
        self.middle_label.pack(side=tk.LEFT, expand=True, fill=tk.X)

    def set_left_status(self, text):
        """Update left status text"""
        self.left_label.config(text=text)

    def set_right_status(self, text):
        """Update right status text"""
        self.right_label.config(text=text)

    def set_middle_status(self, text):
        """Update middle status text"""
        self.middle_label.config(text=text)

def main():
    # Create main window
    root = tk.Tk()
    root.title("VS Code-like Status Bar")
    root.geometry("800x600")

    # Create a text widget to simulate interaction
    text_area = tk.Text(root, wrap=tk.WORD)
    text_area.pack(expand=True, fill=tk.BOTH)

    # Create status bar
    status_bar = StatusBar(root)

    # Example of updating status dynamically
    def update_cursor_position(event):
        # Get current line and column
        current_line = text_area.index(tk.INSERT).split('.')[0]
        current_column = text_area.index(tk.INSERT).split('.')[1]
        status_bar.set_right_status(f"Ln {current_line}, Col {current_column}")

    # Bind cursor movement events
    text_area.bind('<KeyRelease>', update_cursor_position)
    text_area.bind('<Button-1>', update_cursor_position)

    # Simulate some status updates
    root.after(2000, lambda: status_bar.set_left_status("Python - main.py"))
    root.after(4000, lambda: status_bar.set_middle_status("Spaces: 4"))

    root.mainloop()

if __name__ == "__main__":
    main()