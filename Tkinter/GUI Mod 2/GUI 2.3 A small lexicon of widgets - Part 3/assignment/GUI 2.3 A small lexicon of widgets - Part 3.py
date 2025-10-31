import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Widget Demonstration")

# Create a LabelFrame to group widgets
frame = tk.LabelFrame(root, text="User Input Section", padx=10, pady=10)
frame.pack(padx=10, pady=10)

# Create a Message widget to display instructions
instruction = tk.Message(frame, text="Please enter your name below and click the button to display it.")
instruction.pack()

# Create an Entry widget with a StringVar to hold the text
name_var = tk.StringVar()
entry = tk.Entry(frame, textvariable=name_var, width=30)
entry.pack(pady=5)

# Create a Label to display the entered name using another StringVar
display_var = tk.StringVar()
display_label = tk.Label(frame, textvariable=display_var, fg="blue")
display_label.pack(pady=5)

# Function to update the display label with the entered name
def display_name():
    display_var.set(f"Hello, {name_var.get()}!")

# Create a Button to trigger the display function
submit_button = tk.Button(frame, text="Display Name", command=display_name)
submit_button.pack(pady=5)

# Run the application
root.mainloop()