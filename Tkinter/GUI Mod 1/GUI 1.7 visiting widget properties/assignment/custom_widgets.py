import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Custom Widgets")
root.geometry("500x400")
root.configure(bg="white")

# --- Buttons with different colors and cursors ---
button1 = tk.Button(root, text="Button 1", fg="white", bg="darkblue", cursor="hand2")
button1.pack(pady=10)

button2 = tk.Button(root, text="Button 2", fg="black", bg="orange", cursor="plus")
button2.pack(pady=10)

button3 = tk.Button(root, text="Button 3", fg="purple", bg="lightgray", cursor="cross")
button3.pack(pady=10)

# --- Labels with different fonts, styles, and alignment ---
label1 = tk.Label(root, text="Text 1: Bold & Italic", font=("Helvetica", 14, "bold italic"),
                  fg="darkred", bg="lightyellow", anchor="w", width=40)
label1.pack(pady=5)

label2 = tk.Label(root, text="Text 2: Underlined", font=("Times New Roman", 16, "underline"),
                  fg="navy", bg="lightgreen", anchor="e", width=40)
label2.pack(pady=5)

label3 = tk.Label(root, text="Text 3: Large & Plain", font=("Courier", 18),
                  fg="black", bg="lightblue", anchor="center", width=40)
label3.pack(pady=5)

# Run the main loop
root.mainloop()