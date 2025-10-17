import tkinter as tk
from datetime import datetime

root = tk.Tk()
root.title("Login🪵")
root.geometry("800x700")
root.configure(bg="teal")

def change_bg_color():
    """Toggle background color automatically every 3 seconds"""
    if not hasattr(root, "bg_toggle"):
        root.bg_toggle = False
    if root.bg_toggle:
        root.configure(bg="plum")
    else:
        root.configure(bg="teal")
    root.bg_toggle = not root.bg_toggle
    root.after(3000, change_bg_color)

def window_size():
    """Toggle background manually with button"""
    current_color = root.cget("bg")
    if current_color == "teal":
        root.configure(bg="lightblue")
    else:
        root.configure(bg="teal")

# def display_the_song():
#     doors_lyric = "When the music's over, turn out the lights."
#     if button_2_label.cget("text") == "":
#         button_2_label.config(text=doors_lyric)
#     else:
#         button_2_label.config(text="")

# def display_date():
#     button_3_label.config(text=datetime.now())

def resize_window():
    """Toggle window size back and forth on each click"""
    if not hasattr(root, "resized"):
        root.resized = False
    if root.resized:
        root.geometry("800x700")
    else:
        root.geometry("1000x500")
    root.resized = not root.resized

def change_goodbye_text():
    """Toggle Goodbye button text back and forth"""
    if goodbye_button.cget("text") == "Goodbye!":
        goodbye_button.config(text="See you later!")
    else:
        goodbye_button.config(text="Goodbye!")

# --- Buttons and Labels ---
button_1 = tk.Button(root, text="Change Background", command=window_size)
button_1.pack()

# button_2 = tk.Button(root, text="Display Lyric", command=display_the_song)
# button_2.pack()

# button_2_label = tk.Label(root, text="", font=("Arial", 14))
# button_2_label.pack()

# button_3 = tk.Button(root, text="Display Current Date", command=display_date)
# button_3.pack()

# button_3_label = tk.Label(root, text="", font=("Arial", 14))
# button_3_label.pack()

resize_button = tk.Button(root, text="Resize Window", command=resize_window)
resize_button.pack()

goodbye_button = tk.Button(root, text="Goodbye!", command=root.quit)
goodbye_button.pack()

change_text_button = tk.Button(root, text="Change Goodbye Text", command=change_goodbye_text)
change_text_button.pack()

# --- Start background color toggle loop ---
change_bg_color()

root.mainloop()
