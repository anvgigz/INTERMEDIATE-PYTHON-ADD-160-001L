import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Tkinter Widget Showcase")

# Create a StringVar for dynamic label updates
dynamic_text = tk.StringVar()
dynamic_text.set("Dynamic label will update here.")

# Label Widget (Static and Dynamic)
static_label = tk.Label(root, text="This is a static text label.")
static_label.pack(pady=5)

dynamic_label = tk.Label(root, textvariable=dynamic_text)
dynamic_label.pack(pady=5)

# Message Widget
message = tk.Message(root, text="This is a message widget.\nIt is useful for displaying multi-line text.")
message.pack(pady=5)

# Frame Widget
frame = tk.Frame(root, bd=2, relief=tk.SUNKEN)
frame.pack(padx=10, pady=10)

label1 = tk.Label(frame, text="Label inside Frame - 1")
label1.pack()

label2 = tk.Label(frame, text="Label inside Frame - 2")
label2.pack()

# LabelFrame Widget
labelframe = tk.LabelFrame(root, text="This is a LabelFrame", padx=10, pady=10)
labelframe.pack(padx=10, pady=10)

label_in_labelframe = tk.Label(labelframe, text="Label inside LabelFrame")
label_in_labelframe.pack()

# Entry Widget
entry = tk.Entry(root)
entry.pack(pady=5)

# Button to fetch Entry data and update dynamic label
def show_entry_data():
    entry_data = entry.get()
    dynamic_text.set(entry_data)

button = tk.Button(root, text="Show Entry Data", command=show_entry_data)
button.pack(pady=5)

# Run the application
root.mainloop()