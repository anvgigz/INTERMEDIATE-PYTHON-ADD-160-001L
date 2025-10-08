
import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Joke")
root.geometry("300x150")

# Add a label with the joke setup
joke_label = tk.Label(root, text="Why don't scientists trust atoms?")
joke_label.pack(pady=20)

# Define the function to show the punchline
def show_punchline():
    messagebox.showinfo("Punchline", "Because they make up everything!")
    root.destroy()

# Add a button to show the punchline
punchline_button = tk.Button(root, text="Show Punchline", command=show_punchline)
punchline_button.pack(pady=10)

# Run the application
root.mainloop()