# import tkinter as tk

# window = tk.Tk()
# button_1 = tk.Button(window, text="Button #1")
# button_2 = tk.Button(window, text="Button #2")
# button_3 = tk.Button(window, text="Button #3")
# button_1.grid(row=0, column=0)
# button_2.grid(row=1, column=1)
# button_3.grid(row=2, column=2)
# window.mainloop()


"""
The most commonly used grid() method parameters are gathered below (as, previously, all of them are passed as keyword arguments):

column=c – deploys the widget in the column number c; note: the columns' numbers start from zero, and if you omit this argument, the manager will assume 0 (the left-most column)
row=r – deploys the widget in the row number r; if you omit this argument, the manager will assume the first free row starting from the top;
columnspan=cs – determines how many neighboring columns the widget occupies; the parameter defaults to 1 (the widget won't cross a single grid's cell)
rowspan=rs – works as columnspan but refers to rows.
Let's see them all in action.

Analyze the snippet in the editor and determine the resulting number of columns and rows. That's essential if you want to imagine the resulting window's appearance.

Are you ready to solve the puzzle? Did you imagine the window that way?

We're sure you did. Look. The window is divided into nine cells: three rows and three columns. The buttons are settled on the grid's diagonal.

Now we’re going to affect the buttons’ relation to the cells’ boundaries.

"""


import tkinter as tk

window = tk.Tk()
button_1 = tk.Button(window, text="Button #1")
button_2 = tk.Button(window, text="Button #2")
button_3 = tk.Button(window, text="Button #3")
button_1.grid(row=0, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=2, column=0, columnspan=2)
window.mainloop()


"""
Can you see what we changed in the code?

Yes, we modified the third grid() invocation a bit. We wanted to deploy the button inside the cell located in the third (actually, the lowest) row and the first (the left-most) column, but we also did something else – we wanted the widget to span across two horizontally neighboring cells.

We admit that this puzzle is somewhat harder than the previous ones. Don't rush through this – think it over carefully.

Note: the manager noticed that the total number of columns is actually two, not three as in the previous code. This is why the window looks different.

The third, fully automatic geometry manager is named pack() as it packs subsequent widgets into the window's interior. This means that the order in which the widgets are packed matters – in contrast to grid() and place().

Let's take a look at it.

"""