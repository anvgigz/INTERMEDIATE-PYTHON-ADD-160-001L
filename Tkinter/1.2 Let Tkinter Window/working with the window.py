
"""Window with title only"""
# import tkinter

# skylight = tkinter.Tk()
# skylight.title("Skylight")
# skylight.mainloop()


"""adding button but it doesn't do anything yet"""

# import tkinter

# skylight = tkinter.Tk()
# skylight.title("Skylight")
# button = tkinter.Button(skylight, text="Bye!")
# button.place(x=10, y=10)
# skylight.mainloop()



""".destro() is used to close the window when button is clicked"""
# import tkinter

# def Click():
#     skylight.destroy();

# skylight = tkinter.Tk()
# skylight.title("Skylight")
# button = tkinter.Button(skylight, text="Bye!", command=Click)
# button.place(x=10, y=10)
# skylight.mainloop()




"""adding a messagebox to confirm if user wants to quit"""
import tkinter
from tkinter import messagebox


def Click():
    replay = messagebox.askquestion("Quit?", "Are you sure?")
    if replay == 'yes':
        skylight.destroy();


skylight = tkinter.Tk()
skylight.title("Skylight")
button = tkinter.Button(skylight, text="Bye!", command=Click)
button.place(x=10, y=10)
skylight.mainloop()
