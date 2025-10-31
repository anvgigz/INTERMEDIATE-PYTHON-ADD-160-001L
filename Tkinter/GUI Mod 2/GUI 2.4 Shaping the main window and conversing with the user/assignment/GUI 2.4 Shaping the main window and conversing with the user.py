import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Stephen's Tkinter App")
root.geometry("400x300")
root.minsize(300, 200)
root.maxsize(600, 400)

# Set the window icon 
root.iconbitmap(r"C:\Users\stephen\Desktop\INTERMEDIATE PYTHON ADD-160-001L\INTERMEDIATE-PYTHON-ADD-160-001L-main\Tkinter\GUI Mod 2\GUI 2.4 Shaping the main window and conversing with the user\assignment\MicroDev.ico")


# Define close window behavior
def on_closing():
    if messagebox.askokcancel("Exit Confirmation", "Are you sure you want to exit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

# Display message boxes
def show_messages():
    messagebox.showerror("Error", "Oops! Something went wrong.")
    messagebox.showwarning("Warning", "This is just a warning.")
    messagebox.showinfo("Info", "Everything is working fine!")

# Dialog functions
def ask_questions():
    if messagebox.askyesno("Proceed?", "Do you want to continue?"):
        print("User chose Yes")
    else:
        print("User chose No")

    if messagebox.askokcancel("Continue?", "Do you want to proceed with the operation?"):
        print("User chose OK")
    else:
        print("User chose Cancel")

    if messagebox.askretrycancel("Retry?", "Would you like to try again?"):
        print("User chose Retry")
    else:
        print("User chose Cancel")

# Buttons to trigger message boxes and dialogs
btn_messages = tk.Button(root, text="Show Messages", command=show_messages)
btn_messages.pack(pady=10)

btn_dialogs = tk.Button(root, text="Ask Questions", command=ask_questions)
btn_dialogs.pack(pady=10)

# Run the application
root.mainloop()