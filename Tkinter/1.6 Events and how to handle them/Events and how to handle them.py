# import tkinter
# from tkinter import messagebox


# def clicked():
#     messagebox.showinfo("info", "some\ninfo")


# window = tkinter.Tk()
# button_1 = tkinter.Button(window, text="Show info", command=clicked)
# button_1.pack()
# button_2 = tkinter.Button(window, text="Quit", command=window.destroy)
# button_2.pack()
# window.mainloop()


"""In the editor we've provided a very simple code demonstrating how showinfo() works:

Note the \n embedded inside the info string.

And this is what the final message box looks like:
"""

# import tkinter as tk
# from tkinter import messagebox


# def click():
#     tk.messagebox.showinfo("Click!","I love clicks!")


# window = tk.Tk()
# label = tk.Label(window, text="Label")
# label.pack()

# button = tk.Button(window, text="Button", command=click)
# button.pack(fill=tk.X)

# frame = tk.Frame(window, height=30, width=100, bg="#55BF40")
# frame.pack();

# window.mainloop()

"""
If your widget is a clickable one, you can connect a callback to it using its command property, while the property can be initially set by the constructor invocation.

We’ve already practiced this, so the snippet in the editor won’t be a surprise to you.

Note – there are three widgets in all, but only one of them (the Button) is clickable by nature. Such a widget’s constructor is equipped with the command parameter, which is used to bind a callback.
"""
# import tkinter as tk
# from tkinter import messagebox


# def click(event=None):
#     tk.messagebox.showinfo("Click!", "I love clicks!")


# window = tk.Tk()
# label = tk.Label(window, text="Label")
# label.bind("<Button-1>", click)   # Line I
# label.pack()

# button = tk.Button(window, text="Button", command=click)
# button.pack(fill=tk.X)

# frame = tk.Frame(window, height=30, width=100, bg="#55BF40")
# frame.bind("<Button-1>", click)   # Line II
# frame.pack()

# window.mainloop()


"""
Note:

a callback designed for usage with the command property/parameter is a parameterless function;
a callback intended to cooperate with the bind() method is a one-parameter function (the callback’s argument carries some info about the captured event)
fortunately, it doesn’t mean that you have to define two different callbacks for those two applications, and this is how we’ll cope with the above requirements:

def callback(ev=None):
    :
    :

the callback will work flawlessly in both of these contexts, and moreover, it’ll give you the chance to identify which one of the two possible styles of launch has just occurred.
We’re going to change our previous example a bit by making it sensitive to more than just one click.

We've provided the newer version of our code in the editor.

Pay attention to Line I and Line II in the above code. They show the way in which you can bind your callback to any of non-clickable widgets. The bind remains active to the end of the application’s work, but you can also manually unbind the event at any moment (and bind it again when you wish).
"""

# import tkinter as tk
# from tkinter import messagebox


# def click(event=None):
#     if event is None:
#         tk.messagebox.showinfo("Click!", "I love clicks!")
#     else:
#         string = "x=" + str(event.x) + ",y=" + str(event.y) + \
#                  ",num=" + str(event.num) + ",type=" + event.type
#         tk.messagebox.showinfo("Click!", string)        


# window = tk.Tk()
# label = tk.Label(window, text="Label")
# label.bind("<Button-1>", click)
# label.pack()

# button = tk.Button(window, text="Button", command=click)
# button.pack(fill=tk.X)

# frame = tk.Frame(window, height=30, width=100, bg="#55BF40")
# frame.bind("<Button-1>", click)
# frame.pack()

# window.mainloop()

"""
Let’s modify our code again. We want it to unveil some info coming in with the event object. Look at the code in the editor.

We encourage you again to carry out some experiments with this code. Use it to discover the event’s anatomy in detail.


A callback bound to a certain event may be unbound at any moment.

Let’s analyze the process in relation to clickable widgets i.e., those having the command property and using the command constructor’s parameter.

If you unbind a callback from an event, the widget stops reacting to the event. If you want to reverse this action, you must bind the callback again.

We haven’t said a word on modifying a widget’s properties, and we’re going to discuss it thoroughly in the next section, so please forgive us for only doing it briefly now.

If you want to modify a property named prop, existing within a widget named wid, and you’re going set its value to val, you can use the config() method, just like here:

wid.config(prop=val)

This means that if you want to unbind your current callback from a Button named b1, you would use an invocation like this one:

b1.config(command=lambda:None)

This binds an empty (i.e., doing absolutely nothing) function to the widget’s callback.
"""

import tkinter as tk
from tkinter import messagebox


# def on_off():
#     global switch
#     if switch:
#         button_2.config(command=lambda: None)
#         button_2.config(text="Gee!")
#     else:
#         button_2.config(command=peekaboo)
#         button_2.config(text="Peekaboo!")
#     switch = not switch


# def peekaboo():
#     messagebox.showinfo("", "PEEKABOO!")


# def do_nothing():
#     pass


# switch = True
# window = tk.Tk()
# buton_1 = tk.Button(window, text="On/Off", command=on_off)
# buton_1.pack()
# button_2 = tk.Button(window, text="Peekaboo!", command=peekaboo)
# button_2.pack()
# window.mainloop()

"""Our application creates a window with two buttons in it. The first one works as an on/off switch, while the switch changes the behavior of the second button. When the switch is ON, clicking the second button activates a message box. When the switch if OFF, clicking the second button has no effect. Moreover, the second button’s title changes according to the switch’s state.

Note the method we use to change the button’s title.


The two faces of our window look like this:

Now we’ll do the same trick again, but this time with the non-clickable widget.

To unbind a callback previously bound with the bind() method invocation, you need to use the unbind() method:

widget.unbind(event)

The method requires one argument identifying the event being unbound.

Note: the information about a previously used callback is lost. You cannot retrieve it automatically and you must repeat the bind() invocation.
"""


# import tkinter as tk


# def on_off():
#     global switch
#     if switch:
#         label.unbind("<Button-1>")
#     else:
#         label.bind("<Button-1>", rhyme)
#     switch = not switch


# def rhyme(dummy):
#     global word_no, words
#     word_no += 1
#     label.config(text=words[word_no % len(words)])


# switch = True
# words = ["Old", "McDonald", "Had", "A", "Farm"]
# word_no = 0
# window = tk.Tk()
# button = tk.Button(window, text="On/Off", command=on_off)
# button.pack()
# label = tk.Label(window, text=words[0])
# label.bind("<Button-1>", rhyme)
# label.pack()
# window.mainloop()


"""
The application contains two widgets: one Button (clickable) and one Label (non-clickable).

We bind a callback to the Label, causing it to display (in a loop) the first five words of this old but good rhyme (please dive into the rhyme() function to check out how we’ve done it).

This functionality can be turned off and on by clicking the button. As you can see, the on_off() callback binds and unbinds the label’s callback.

Try to modify the code to use a few other events to trigger the switch.

"""

import tkinter as tk
from tkinter import messagebox


def hello(dummy):
    messagebox.showinfo("", "Hello!")


window = tk.Tk()
button = tk.Button(window, text="On/Off")
button.pack()
label = tk.Label(window, text="Label")
label.pack()
frame = tk.Frame(window, bg="yellow", width=100, height=20)
frame.pack()
window.bind_all("<Button-1>", hello)
window.mainloop()


"""
The main tkinter window has a method named bind_all() which binds a callback to all currently existing widgets.

There is also a method named unbind_all() which reverts the first method’s effects.

window.bind_all(event, callback)
window.unbind_all(event)


We used the bind_all() method to bind the one and the same callback to all three widgets, whether clickable or not. Look at the code we've provided in the editor.

Play with the code. Don’t worry, it’s safe.

Now we’re going to take you on a trip to Widget land. It’ll be an exciting journey, we promise.


"""