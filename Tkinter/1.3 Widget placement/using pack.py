# import tkinter as tk


# window = tk.Tk()
# button_1 = tk.Button(window, text="Button #1")
# button_2 = tk.Button(window, text="Button #2")
# button_3 = tk.Button(window, text="Button #3")
# button_1.pack()
# button_2.pack()
# button_3.pack()
# window.mainloop()

"""The default pack's operation tends to deploy all subsequent widgets in one column, one below the other. You can change this behavior to a limited extent by using the following parameters:

side=s – forces the manager to pack the widgets in a specified direction, where s can be specified as:
TOP – the widget is packed toward the window's top (it's manager's default behavior)
BOTTOM – the widget is packed toward the window's bottom;
LEFT – toward the window's left boundary;
RIGHT – toward the window's right boundary;
fill=f – suggests to the manager how to expand the widget if you want it to occupy more space than the default,
while f should be specified as:
NONE – do not expand the widget (default behavior)
X – expand it in the horizontal direction;
Y – expand it in the vertical direction;
BOTH – expand it in both directions;
We want to warn you that the results produced by pack() can be extremely surprising,
and you should spend some time on your own experimenting with all its vices.

We suggest you use it only as a temporary solution to help you get a working application quickly,
but if you want your application to look nice and to be legible and clear (of course, you would want that!)
you'd better forget about pack() and use either grid() (in simpler cases) or place().

Let pack() show us what it can do for us. Look at the code in the editor.

As you can see, using pack() simplifies the code – you don't need to specify any coordinates
– but that doesn't mean this will simplify the developer's life. You may expect that pack() will know how to handle your widgets,
but sometimes it's work results are like a lottery.

Let's look at the window we get. The window looks different.

Very different. For example, the window fits its size to the area occupied by the widgets.
The buttons are located one after the other, from top to bottom.

Let's play a little game with pack's arguments."""



# import tkinter as tk

# window = tk.Tk()
# button_1 = tk.Button(window, text="Button #1")
# button_2 = tk.Button(window, text="Button #2")
# button_3 = tk.Button(window, text="Button #3")
# button_1.pack(side=tk.RIGHT)
# button_2.pack()
# button_3.pack()
# window.mainloop()


"""
We've ordered pack() to push the button_1 button to the right window's boundary.

Can you predict the window's appearance? We admit that it may be difficult.

Is this what you expected?


No? Are you surprised? You have the right to be. Pack is the least intuitive geometry manager for sure, 
and you really need to spend some time testing its whims.

We have one more experiment left to carry out.


"""


import tkinter as tk

window = tk.Tk()
button_1 = tk.Button(window, text="Button #1")
button_2 = tk.Button(window, text="Button #2")
button_3 = tk.Button(window, text="Button #3")
button_1.pack(side=tk.RIGHT, fill=tk.Y)
button_2.pack()
button_3.pack()
window.mainloop()


"""
Note: we want the button_1 button to be filled (expanded) in the vertical direction:

This puzzle is a bit easier than the previous one. Think for a moment.

Yes, you're right – this is the expected answer.



We think that there is one intriguing question that can be asked here and now: do these buttons have to be gray? 
It's boring. Very boring.

We're going to clear up this issue soon.

"""