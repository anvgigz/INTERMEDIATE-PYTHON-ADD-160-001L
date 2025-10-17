import tkinter as tk

# Initialize the main window
root = tk.Tk()
root.title("Greeting App")

# Declare observable variables
name_var = tk.StringVar()
age_var = tk.StringVar()
message_var = tk.StringVar()

# Create the user interface
tk.Label(root, text="Name:").grid(row=0, column=0)
tk.Entry(root, textvariable=name_var).grid(row=0, column=1)

tk.Label(root, text="Age:").grid(row=1, column=0)
tk.Entry(root, textvariable=age_var).grid(row=1, column=1)


# Define the function to update the message
def update_message(*args):
    name = name_var.get()
    age = age_var.get()
    
    if name and age:
        message_var.set(f"Hello, {name}! You are {age} years old.")
    else:
        message_var.set("")

# Add observers
name_var.trace("w", update_message)
age_var.trace("w", update_message)

# Create the label to display the message
tk.Label(root, textvariable=message_var).grid(row=2, columnspan=2)

# Start the Tkinter event loop
root.mainloop()