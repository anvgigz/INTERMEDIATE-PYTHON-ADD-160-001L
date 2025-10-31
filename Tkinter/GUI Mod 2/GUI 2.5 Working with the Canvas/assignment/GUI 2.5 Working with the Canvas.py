import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Christmas Tree Canvas")

# Create a canvas with specified dimensions and background color

canvas = tk.Canvas(root, width=400, height=500, bg='lightblue', borderwidth=2)
canvas.pack()



# Tree layers (centered at x=200)
canvas.create_polygon(200, 50, 250, 150, 150, 150, outline='green', fill='green', width=2)   # Top
canvas.create_polygon(200, 120, 270, 220, 130, 220, outline='green', fill='green', width=2) # Middle
canvas.create_polygon(200, 190, 300, 300, 100, 300, outline='green', fill='green', width=2) # Bottom

# Trunk (centered under tree)
canvas.create_rectangle(175, 300, 225, 350, outline='brown', fill='brown', width=2)


# Draw ornaments (circles)
canvas.create_oval(180, 120, 190, 130, outline='red', fill='red', width=2)
canvas.create_oval(210, 160, 220, 170, outline='blue', fill='blue', width=2)
canvas.create_oval(150, 180, 160, 190, outline='yellow', fill='yellow', width=2)

# Add text
canvas.create_text(200, 380, text="Happy Holidays!", font=('Arial', 20), fill='black')

# Start the Tkinter event loop
root.mainloop()