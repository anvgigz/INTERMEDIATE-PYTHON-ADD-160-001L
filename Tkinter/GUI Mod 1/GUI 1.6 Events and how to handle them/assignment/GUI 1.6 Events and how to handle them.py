import tkinter as tk
from datetime import datetime


root = tk.Tk()

root.title("Login🪵")

root.geometry("800x700")
root.configure(bg="lightblue")

def background_change():
    current_color = root.cget("bg")

    if current_color == "teal":
        root.configure(bg="lightblue")
    else:
        root.configure(bg="teal")

def display_the_song():
    doors_lyric = "When the music\'s over, turn out the lights."
    if button_2_label.cget("text") == "":
        button_2_label.config(text=doors_lyric)
    else:
        button_2_label.config(text="")

def display_date():
    button_3_label.config(text=datetime.now())


button_1 = tk.Button(root, text="Change Background", command=background_change)
button_1.pack()

button_2 = tk.Button(root, text="Display Lyric", command=display_the_song)
button_2.pack()



button_2_label = tk.Label(root, text="", font=("Arial", 14))
button_2_label.pack()  # This places the button_2_label directly below button_2

button_3 = tk.Button(root, text="display current date", command=display_date)
button_3.pack()

button_3_label = tk.Label(root, text="", font=("Ariel, 14"))
button_3_label.pack()




root.mainloop()