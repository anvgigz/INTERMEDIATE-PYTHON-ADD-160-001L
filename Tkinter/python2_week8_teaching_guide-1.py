"""
================================================================================
TKINTER GUI EVENTS - COMPREHENSIVE TEACHING GUIDE
================================================================================

This teaching guide provides detailed explanations of tkinter events and methods.
Each section includes:
- Concept explanation
- Why it's useful
- How it works
- Best practices
- Common use cases

Author: For Python GUI Programming Students
Purpose: Learn tkinter event handling and widget methods
================================================================================
"""

import tkinter as tk
from tkinter import messagebox

"""
================================================================================
CONCEPT 1: MESSAGEBOX
================================================================================

WHAT IS IT?
-----------
A messagebox is a popup dialog window that displays information to the user
or asks for simple input (yes/no, ok/cancel, etc.)

WHY USE IT?
-----------
- Provide feedback to users about actions they've taken
- Alert users to errors or warnings
- Ask for confirmation before performing critical actions
- Simple way to get yes/no answers without creating custom dialogs

TYPES OF MESSAGEBOXES:
----------------------
1. showinfo()     - Display informational messages
2. showwarning()  - Display warning messages  
3. showerror()    - Display error messages
4. askquestion()  - Ask a question (returns 'yes' or 'no')
5. askyesno()     - Ask yes/no question (returns True or False)
6. askokcancel()  - Ask ok/cancel question (returns True or False)
7. askyesnocancel() - Ask yes/no/cancel (returns True/False/None)
8. askretrycancel() - Ask retry/cancel (returns True or False)

SYNTAX:
-------
messagebox.showinfo(title, message)
messagebox.askyesno(title, message) -> returns True or False

BEST PRACTICES:
---------------
- Use clear, concise messages
- Choose appropriate type for the situation (error for errors, warning for warnings)
- Don't overuse - too many popups annoy users
- Always handle the return value for ask* functions
"""

class MessageBoxDemo:
    """Demonstrates various types of messageboxes"""
    
    def __init__(self, parent):
        frame = tk.LabelFrame(parent, text="1. MESSAGEBOX - User Notifications", 
                             padx=10, pady=5, bg="white")
        frame.pack(fill=tk.X, pady=5)
        
        # Info message - use for general information
        tk.Button(frame, text="Info", 
                 command=self.show_info).pack(side=tk.LEFT, padx=5)
        
        # Warning message - use for warnings that aren't critical errors
        tk.Button(frame, text="Warning", 
                 command=self.show_warning).pack(side=tk.LEFT, padx=5)
        
        # Error message - use for errors and problems
        tk.Button(frame, text="Error", 
                 command=self.show_error).pack(side=tk.LEFT, padx=5)
        
        # Yes/No question - use when you need a binary decision
        tk.Button(frame, text="Yes/No Question", 
                 command=self.ask_yes_no).pack(side=tk.LEFT, padx=5)
    
    def show_info(self):
        # Returns 'ok' when user clicks OK
        messagebox.showinfo("Info", "This is an informational message!")
    
    def show_warning(self):
        # Returns 'ok' when user clicks OK
        messagebox.showwarning("Warning", "This is a warning message!")
    
    def show_error(self):
        # Returns 'ok' when user clicks OK
        messagebox.showerror("Error", "This is an error message!")
    
    def ask_yes_no(self):
        # Returns True for Yes, False for No
        result = messagebox.askyesno("Question", "Do you like Python?")
        if result:
            messagebox.showinfo("Result", "Great choice!")
        else:
            messagebox.showinfo("Result", "Give it another try!")


"""
================================================================================
CONCEPT 2: BUTTON COMMAND PARAMETER
================================================================================

WHAT IS IT?
-----------
The 'command' parameter is a way to specify a function (callback) that should
be executed when a button is clicked.

HOW IT WORKS:
-------------
1. When creating a button, you pass a function name to the command parameter
2. When the button is clicked, tkinter automatically calls that function
3. The function executes and can perform any actions you want

SYNTAX:
-------
Button(parent, text="Click", command=function_name)
Button(parent, text="Click", command=lambda: function_with_args(arg1, arg2))

IMPORTANT NOTES:
----------------
- Use function_name WITHOUT parentheses: command=my_function (correct)
- DON'T use: command=my_function() - this calls it immediately!
- To pass arguments, use lambda: command=lambda: my_function(arg)
- Lambda creates an anonymous function that calls your function with arguments

WHEN TO USE:
------------
- Button clicks (most common)
- Menu items
- Any widget that supports command parameter
- Simple, direct action responses

ALTERNATIVE:
------------
You can also use .bind('<Button-1>', function) for more control over events
(see Mouse Click section below)
"""

class ButtonCommandDemo:
    """Demonstrates using the command parameter for button callbacks"""
    
    def __init__(self, parent):
        frame = tk.LabelFrame(parent, text="2. BUTTON COMMAND - Simple Callbacks", 
                             padx=10, pady=5, bg="white")
        frame.pack(fill=tk.X, pady=5)
        
        self.command_label = tk.Label(frame, text="Click buttons to see callbacks", 
                                     bg="white")
        self.command_label.pack(side=tk.LEFT, padx=10)
        
        # Method 1: Direct function reference (no arguments)
        # The button_clicked method needs a parameter, so we use lambda
        
        # Method 2: Using lambda to pass arguments
        # Lambda syntax: lambda: function(arguments)
        tk.Button(frame, text="Button 1", 
                 command=lambda: self.button_clicked("Button 1")).pack(side=tk.LEFT, padx=5)
        
        tk.Button(frame, text="Button 2", 
                 command=lambda: self.button_clicked("Button 2")).pack(side=tk.LEFT, padx=5)
        
        # You could also create a button without lambda if the function takes no args:
        # tk.Button(frame, text="No Args", command=self.no_args_function).pack()
    
    def button_clicked(self, button_name):
        """
        This is a callback function.
        It gets called when a button is clicked.
        The button_name parameter tells us which button was clicked.
        """
        self.command_label.config(text=f"{button_name} was clicked!")


"""
================================================================================
CONCEPT 3: BIND METHOD AND MOUSE EVENTS
================================================================================

WHAT IS IT?
-----------
The .bind() method connects an event (like a mouse click) to a function.
Unlike 'command', bind gives you detailed event information.

SYNTAX:
-------
widget.bind(event_pattern, callback_function)

COMMON MOUSE EVENTS:
--------------------
'<Button-1>'        - Left mouse button click
'<Button-2>'        - Middle mouse button click
'<Button-3>'        - Right mouse button click
'<Double-Button-1>' - Double-click with left button
'<ButtonRelease-1>' - Left button release
'<B1-Motion>'       - Mouse moved while left button held down
'<Enter>'           - Mouse enters widget area
'<Leave>'           - Mouse leaves widget area
'<Motion>'          - Mouse moves over widget

EVENT OBJECT:
-------------
When the event occurs, tkinter creates an Event object and passes it to
your callback function. This object contains useful information:
- event.x, event.y - mouse position relative to the widget
- event.x_root, event.y_root - mouse position on the screen
- event.widget - which widget received the event
- event.num - which mouse button (1=left, 2=middle, 3=right)

WHY USE BIND INSTEAD OF COMMAND?
---------------------------------
- Works with any widget (labels, frames, canvas, etc.), not just buttons
- Gives you event details (position, which button, etc.)
- Can bind multiple different events to the same widget
- More flexible and powerful

BEST PRACTICES:
---------------
- Function must accept one parameter: the event object
- Event patterns are case-sensitive: '<Button-1>' not '<button-1>'
- Use descriptive function names: handle_click, on_mouse_enter, etc.
"""

class MouseClickDemo:
    """Demonstrates mouse event binding"""
    
    def __init__(self, parent):
        frame = tk.LabelFrame(parent, text="3. BIND - Mouse Click Events", 
                             padx=10, pady=5, bg="white")
        frame.pack(fill=tk.X, pady=5)
        
        self.click_label = tk.Label(frame, text="Click anywhere in this box!", 
                                   bg="lightblue", width=50, height=3, relief=tk.RAISED)
        self.click_label.pack(padx=10, pady=5)
        
        # Bind left mouse click to the label
        # Note: The callback function MUST accept an event parameter
        self.click_label.bind('<Button-1>', self.handle_left_click)
        
        # You can bind multiple events to the same widget:
        self.click_label.bind('<Button-3>', self.handle_right_click)
        self.click_label.bind('<Enter>', self.handle_mouse_enter)
        self.click_label.bind('<Leave>', self.handle_mouse_leave)
    
    def handle_left_click(self, event):
        """
        Called when left mouse button is clicked.
        The event object contains information about the click.
        """
        # event.x and event.y give position relative to the widget
        self.click_label.config(text=f"Left clicked at: x={event.x}, y={event.y}")
    
    def handle_right_click(self, event):
        """Called when right mouse button is clicked"""
        self.click_label.config(text=f"Right clicked at: x={event.x}, y={event.y}")
    
    def handle_mouse_enter(self, event):
        """Called when mouse enters the widget area"""
        self.click_label.config(bg="yellow")
    
    def handle_mouse_leave(self, event):
        """Called when mouse leaves the widget area"""
        self.click_label.config(bg="lightblue")


"""
================================================================================
CONCEPT 4: KEYBOARD EVENTS AND FRAME.BIND()
================================================================================

WHAT IS IT?
-----------
Keyboard events occur when users press keys. You can bind these events to
widgets using the .bind() method, just like mouse events.

COMMON KEYBOARD EVENT PATTERNS:
-------------------------------
'<Key>'         - Any key press
'<KeyRelease>'  - Any key release
'<Return>'      - Enter/Return key
'<space>'       - Space bar
'<BackSpace>'   - Backspace key
'<Tab>'         - Tab key
'<Escape>'      - Escape key
'<Up>', '<Down>', '<Left>', '<Right>' - Arrow keys
'<F1>' to '<F12>' - Function keys
'a', 'b', 'A', 'B' - Specific letter keys
'<Control-c>'   - Ctrl+C (and other combos)
'<Shift-A>'     - Shift+A (and other combos)

EVENT OBJECT PROPERTIES FOR KEYS:
----------------------------------
- event.char - The character of the key pressed (empty for special keys)
- event.keysym - The symbolic name of the key ('Return', 'a', 'F1', etc.)
- event.keycode - Numeric code for the key (platform dependent)
- event.state - Modifier keys held down (Shift, Ctrl, Alt)

IMPORTANT: FOCUS
----------------
A widget must have keyboard focus to receive keyboard events!
- Click on a widget to give it focus
- Or call widget.focus_set() to programmatically set focus
- Only one widget can have focus at a time

WHY BIND TO FRAMES?
-------------------
- Frames can receive keyboard events just like other widgets
- Useful for creating keyboard shortcuts for a section of your GUI
- Can create clickable areas that also respond to keyboard input

BEST PRACTICES:
---------------
- Make sure the widget has focus (use focus_set() or let user click it)
- Use specific key bindings ('<Return>') before general ones ('<Key>')
- Provide visual feedback so users know which widget has focus
- Document keyboard shortcuts for users
"""

class KeyPressDemo:
    """Demonstrates keyboard event binding on frames"""
    
    def __init__(self, parent):
        frame = tk.LabelFrame(parent, text="4. KEYBOARD EVENTS - Frame.bind()", 
                             padx=10, pady=5, bg="white")
        frame.pack(fill=tk.X, pady=5)
        
        instruction = tk.Label(frame, text="Click in the colored area and press keys:", 
                              bg="white")
        instruction.pack()
        
        # Create a frame that will receive keyboard events
        self.key_frame = tk.Frame(frame, bg="lightyellow", width=400, height=60)
        self.key_frame.pack(padx=10, pady=5)
        self.key_frame.pack_propagate(False)  # Maintain fixed size
        
        self.key_label = tk.Label(self.key_frame, text="Press any key...", 
                                 bg="lightyellow", font=("Arial", 12))
        self.key_label.pack(expand=True)
        
        # Bind keyboard events to the FRAME (not the label)
        # The frame must have focus to receive these events
        
        # Specific key bindings - these take precedence over general '<Key>'
        self.key_frame.bind('<Return>', self.handle_return_key)
        self.key_frame.bind('<space>', self.handle_space_key)
        self.key_frame.bind('<Escape>', self.handle_escape_key)
        
        # General key binding - catches all other keys
        # Put this AFTER specific bindings
        self.key_frame.bind('<Key>', self.handle_key_press)
        
        # IMPORTANT: Give the frame keyboard focus so it can receive key events
        self.key_frame.focus_set()
        
        # Visual feedback when frame has/loses focus
        self.key_frame.bind('<FocusIn>', lambda e: self.key_frame.config(bg="lightyellow"))
        self.key_frame.bind('<FocusOut>', lambda e: self.key_frame.config(bg="lightgray"))
    
    def handle_key_press(self, event):
        """
        Handles general key presses.
        event.char contains the character typed (if printable)
        event.keysym contains the symbolic name of the key
        """
        self.key_label.config(text=f"Key: '{event.char}' | Symbol: {event.keysym} | Code: {event.keycode}")
    
    def handle_return_key(self, event):
        """Specific handler for Return/Enter key"""
        self.key_label.config(text="RETURN key pressed! (Enter to submit)")
    
    def handle_space_key(self, event):
        """Specific handler for Space bar"""
        self.key_label.config(text="SPACE bar pressed!")
    
    def handle_escape_key(self, event):
        """Specific handler for Escape key"""
        self.key_label.config(text="ESCAPE pressed! (often used to cancel)")


"""
================================================================================
CONCEPT 5: EVENT OBJECT PROPERTIES
================================================================================

WHAT IS IT?
-----------
Every time an event occurs (mouse click, key press, etc.), tkinter creates
an Event object containing detailed information about the event.

WHY IS IT USEFUL?
-----------------
The Event object tells you:
- WHERE the event happened (x, y coordinates)
- WHAT caused the event (which widget, which key/button)
- WHEN it happened (timestamp)
- HOW it happened (modifier keys like Shift, Ctrl)

COMMON EVENT PROPERTIES:
------------------------
MOUSE-RELATED:
- x, y           - Position relative to the widget
- x_root, y_root - Position on the screen
- num            - Mouse button number (1=left, 2=middle, 3=right)

KEYBOARD-RELATED:
- char           - Character typed (for printable keys)
- keysym         - Symbolic name ('Return', 'Escape', 'a', 'F1')
- keycode        - Numeric key code (platform-specific)

GENERAL:
- widget         - The widget that received the event
- type           - Type of event (EventType.ButtonPress, etc.)
- state          - Modifier keys (Shift=1, Ctrl=4, Alt=8, etc.)
- time           - When event occurred (milliseconds)

HOW TO USE:
-----------
Your event callback function receives the event object as a parameter.
You can access these properties using dot notation: event.x, event.char, etc.

PRACTICAL USES:
---------------
- Drawing applications: use x, y to draw at click position
- Form validation: check which key was pressed
- Context menus: use x_root, y_root to position menu at cursor
- Keyboard shortcuts: check event.state for Ctrl+Key combinations
"""

class EventPropertiesDemo:
    """Demonstrates all the properties available in an Event object"""
    
    def __init__(self, parent):
        frame = tk.LabelFrame(parent, text="5. EVENT OBJECT - Properties & Information", 
                             padx=10, pady=5, bg="white")
        frame.pack(fill=tk.X, pady=5)
        
        instruction = tk.Label(frame, text="Click or type to see event properties:", 
                              bg="white")
        instruction.pack()
        
        # Button to show mouse event properties
        event_button = tk.Button(frame, text="Click to See Mouse Event Properties", 
                                bg="orange", fg="white", font=("Arial", 10, "bold"))
        event_button.pack(padx=10, pady=5)
        event_button.bind('<Button-1>', self.show_mouse_event_properties)
        
        # Entry to show keyboard event properties
        event_entry = tk.Entry(frame, width=40, font=("Arial", 10))
        event_entry.pack(padx=10, pady=5)
        event_entry.insert(0, "Type here to see keyboard event properties")
        event_entry.bind('<Key>', self.show_keyboard_event_properties)
    
    def show_mouse_event_properties(self, event):
        """
        Display all interesting properties of a mouse event.
        This helps you understand what information is available.
        """
        properties = f"""MOUSE EVENT OBJECT PROPERTIES:

POSITION (relative to widget):
  x: {event.x}
  y: {event.y}

POSITION (on screen):
  x_root: {event.x_root}
  y_root: {event.y_root}

MOUSE BUTTON:
  num: {event.num} (1=left, 2=middle, 3=right)

WIDGET:
  widget: {event.widget}
  widget class: {event.widget.winfo_class()}

EVENT TYPE:
  type: {event.type}

TIME:
  time: {event.time} (milliseconds since system start)

MODIFIERS:
  state: {event.state}
  (1=Shift, 4=Ctrl, 8=Alt, add them for combinations)
        """
        messagebox.showinfo("Mouse Event Properties", properties)
    
    def show_keyboard_event_properties(self, event):
        """Display properties of a keyboard event"""
        properties = f"""KEYBOARD EVENT OBJECT PROPERTIES:

CHARACTER:
  char: '{event.char}' (the actual character)

KEY SYMBOL:
  keysym: {event.keysym} (symbolic name)
  
KEY CODE:
  keycode: {event.keycode} (numeric code)

WIDGET:
  widget: {event.widget}

EVENT TYPE:
  type: {event.type}

MODIFIERS:
  state: {event.state}
  (1=Shift, 4=Ctrl, 8=Alt)

POSITION (where cursor was):
  x: {event.x}, y: {event.y}
        """
        messagebox.showinfo("Keyboard Event Properties", properties)


"""
================================================================================
CONCEPT 6: BIND_ALL() AND UNBIND()
================================================================================

BIND_ALL():
-----------
WHAT: Binds an event to ALL widgets in the entire application
SYNTAX: widget.bind_all(event_pattern, callback)
        or root.bind_all(event_pattern, callback)

WHY USE IT?
- Create global keyboard shortcuts (F1 for help, Ctrl+S for save)
- Catch events no matter which widget has focus
- Implement application-wide features

DIFFERENCE FROM BIND():
- bind(): only affects one specific widget
- bind_all(): affects every widget in the application
- bind_all() events trigger regardless of which widget has focus

UNBIND():
---------
WHAT: Removes a previously bound event
SYNTAX: widget.unbind(event_pattern)
        widget.unbind_all(event_pattern)

WHY USE IT?
- Disable features temporarily
- Change behavior dynamically
- Prevent unwanted events in certain application states
- Clean up when destroying widgets

IMPORTANT NOTES:
----------------
- unbind() only removes bindings created with bind()
- unbind_all() only removes bindings created with bind_all()
- If you bind multiple functions to the same event, unbind removes all of them
- To re-enable, you must call bind() or bind_all() again

BEST PRACTICES:
---------------
- Document global shortcuts for users
- Provide a way to disable shortcuts if needed
- Be careful with bind_all - it affects EVERYTHING
- Use unbind when a feature is no longer available
"""

class BindUnbindDemo:
    """Demonstrates bind_all() for global events and unbind() to remove them"""
    
    def __init__(self, parent, root):
        self.root = root
        
        frame = tk.LabelFrame(parent, text="6. BIND_ALL & UNBIND - Global Events", 
                             padx=10, pady=5, bg="white")
        frame.pack(fill=tk.X, pady=5)
        
        self.bind_status_label = tk.Label(frame, 
                                         text="Press F1 anywhere in the window for help", 
                                         bg="white", fg="blue")
        self.bind_status_label.pack()
        
        self.toggle_button = tk.Button(frame, text="Disable F1 (unbind)", 
                                      command=self.toggle_f1_binding, 
                                      bg="lightgreen", width=20)
        self.toggle_button.pack(padx=10, pady=5)
        
        # bind_all - binds to ALL widgets in the application
        # F1 will work no matter which widget has focus
        self.root.bind_all('<F1>', self.handle_f1)
        self.f1_bound = True
        
        # You can also bind other global shortcuts:
        # self.root.bind_all('<Control-s>', self.save_file)
        # self.root.bind_all('<Control-q>', self.quit_application)
    
    def handle_f1(self, event):
        """
        F1 is commonly used for help in applications.
        Because we used bind_all(), this works from anywhere.
        """
        help_text = """HELP - Keyboard Shortcuts:

F1 - Show this help
(You can add more shortcuts here)

This works from anywhere in the application
because it uses bind_all()!"""
        messagebox.showinfo("Help (F1)", help_text)
    
    def toggle_f1_binding(self):
        """Toggle the F1 binding on and off"""
        if self.f1_bound:
            # Remove the F1 binding - it will no longer work
            self.root.unbind_all('<F1>')
            self.f1_bound = False
            self.toggle_button.config(text="Enable F1 (bind)", bg="lightcoral")
            self.bind_status_label.config(text="F1 is disabled (press button to re-enable)", 
                                         fg="red")
        else:
            # Re-bind F1 - it will work again
            self.root.bind_all('<F1>', self.handle_f1)
            self.f1_bound = True
            self.toggle_button.config(text="Disable F1 (unbind)", bg="lightgreen")
            self.bind_status_label.config(text="F1 is enabled (press it to see help)", 
                                         fg="blue")


"""
================================================================================
CONCEPT 7: AFTER() METHOD - SCHEDULING DELAYED ACTIONS
================================================================================

WHAT IS IT?
-----------
The .after() method schedules a function to be called after a specified
delay (in milliseconds).

SYNTAX:
-------
widget.after(delay_ms, function)
widget.after(delay_ms, function, arg1, arg2, ...)

delay_ms: number of milliseconds to wait (1000ms = 1 second)
function: the function to call after the delay

WHY USE IT?
-----------
- Create animations and timers
- Auto-update displays (clocks, counters, status)
- Implement delays between actions
- Create auto-save features
- Polling/checking for updates
- Non-blocking delays (doesn't freeze the GUI)

HOW IT WORKS:
-------------
1. You call after() with a delay and function
2. Tkinter schedules the function to run after the delay
3. Your GUI remains responsive during the wait
4. When time expires, the function is called
5. For continuous updates, have the function call after() again (recursion)

IMPORTANT: NON-BLOCKING
-----------------------
Unlike time.sleep(), after() doesn't freeze your GUI!
- time.sleep(5) - freezes GUI for 5 seconds (BAD)
- after(5000, func) - GUI stays responsive (GOOD)

AFTER_CANCEL():
---------------
You can cancel a scheduled after() call:
  id = widget.after(1000, function)
  widget.after_cancel(id)

BEST PRACTICES:
---------------
- Use 1000 for 1 second, 500 for half second, etc.
- For continuous updates, call after() recursively
- Store after() ID if you need to cancel it later
- Don't use time.sleep() in GUI apps - use after() instead!
"""

class AfterDemo:
    """Demonstrates scheduling delayed actions with .after()"""
    
    def __init__(self, parent, root):
        self.root = root
        
        frame = tk.LabelFrame(parent, text="7. AFTER() - Delayed Actions & Timers", 
                             padx=10, pady=5, bg="white")
        frame.pack(fill=tk.X, pady=5)
        
        # Example 1: Auto-incrementing counter
        self.after_counter = 0
        self.counting = False
        
        self.after_label = tk.Label(frame, text="Counter: 0", 
                                   bg="white", font=("Arial", 12, "bold"))
        self.after_label.pack(side=tk.LEFT, padx=10)
        
        tk.Button(frame, text="Start Counter", 
                 command=self.start_counter).pack(side=tk.LEFT, padx=5)
        
        # Example 2: One-time delayed message
        tk.Button(frame, text="Delayed Message (3s)", 
                 command=self.show_delayed_message).pack(side=tk.LEFT, padx=5)
        
        # Example 3: Countdown timer
        self.countdown_label = tk.Label(frame, text="", bg="white")
        self.countdown_label.pack(side=tk.LEFT, padx=10)
        
        tk.Button(frame, text="Countdown from 5", 
                 command=self.start_countdown).pack(side=tk.LEFT, padx=5)
    
    def start_counter(self):
        """
        Auto-incrementing counter using recursive after() calls.
        This pattern is common for animations and live updates.
        """
        if not self.counting:
            self.counting = True
            self.after_counter = 0
        
        self.after_counter += 1
        self.after_label.config(text=f"Counter: {self.after_counter}")
        
        # Schedule this function to run again after 1000ms (1 second)
        # This creates a continuous loop without blocking the GUI
        self.root.after(1000, self.start_counter)
        
        # In a real app, you'd want a way to stop this:
        # if self.counting:
        #     self.after_id = self.root.after(1000, self.start_counter)
        # Then later: self.root.after_cancel(self.after_id)
    
    def show_delayed_message(self):
        """
        One-time delayed action.
        Good for: "Save successful" messages, timeouts, auto-hide notifications
        """
        self.after_label.config(text="Message coming in 3 seconds...")
        
        # Schedule a function to run once after 3000ms (3 seconds)
        # Using lambda to call messagebox.showinfo with arguments
        self.root.after(3000, lambda: messagebox.showinfo("Delayed", "3 seconds have passed!"))
        
        # Reset the label after 4 seconds
        self.root.after(4000, lambda: self.after_label.config(text=f"Counter: {self.after_counter}"))
    
    def start_countdown(self):
        """
        Countdown timer example.
        Shows how to create a decreasing timer.
        """
        self.countdown_value = 5
        self.update_countdown()
    
    def update_countdown(self):
        """Recursive countdown updater"""
        if self.countdown_value > 0:
            self.countdown_label.config(text=f"Countdown: {self.countdown_value}")
            self.countdown_value -= 1
            # Call again in 1 second
            self.root.after(1000, self.update_countdown)
        else:
            self.countdown_label.config(text="Done!")
            # Clear after 2 seconds
            self.root.after(2000, lambda: self.countdown_label.config(text=""))


"""
================================================================================
CONCEPT 8: DESTROY() METHOD - DYNAMICALLY REMOVING WIDGETS
================================================================================

WHAT IS IT?
-----------
The .destroy() method permanently removes a widget and all its children
from the GUI and frees up its resources.

SYNTAX:
-------
widget.destroy()

WHY USE IT?
-----------
- Create dynamic interfaces that change based on user actions
- Remove temporary widgets (dialogs, notifications, tooltips)
- Clean up when closing windows
- Implement "dismiss" or "close" buttons
- Remove items from dynamic lists
- Free memory by removing unused widgets

HOW IT WORKS:
-------------
1. When you call destroy() on a widget:
   - The widget is removed from the screen
   - All child widgets are also destroyed
   - Memory is freed
   - The widget object is gone - you can't use it anymore!

IMPORTANT WARNINGS:
-------------------
- After destroy(), you can't access the widget anymore!
- If you destroy a widget that other code references, you'll get errors
- Destroying a parent destroys all its children
- You can't "undo" a destroy - the widget is gone forever

DESTROYING THE ROOT WINDOW:
---------------------------
root.destroy() - closes the entire application and exits mainloop()

ALTERNATIVE: GRID_FORGET(), PACK_FORGET()
------------------------------------------
If you want to hide a widget temporarily (not destroy it):
- widget.pack_forget() - removes from pack geometry manager
- widget.grid_forget() - removes from grid geometry manager
- Later you can pack() or grid() it again to show it

BEST PRACTICES:
---------------
- Use destroy() for widgets you won't need again
- Use pack_forget()/grid_forget() for widgets you'll show again
- Be careful with references to destroyed widgets
- Consider asking for confirmation before destroying important content
"""

class DestroyDemo:
    """Demonstrates dynamically creating and destroying widgets"""
    
    def __init__(self, parent):
        frame = tk.LabelFrame(parent, text="8. DESTROY() - Create & Remove Widgets", 
                             padx=10, pady=5, bg="white")
        frame.pack(fill=tk.X, pady=5)
        
        instruction = tk.Label(frame, text="Create buttons, then click them to destroy:", 
                              bg="white")
        instruction.pack()
        
        # Container for dynamically created widgets
        self.destroy_container = tk.Frame(frame, bg="white")
        self.destroy_container.pack()
        
        # Button to create new widgets
        tk.Button(frame, text="Create New Button", 
                 command=self.create_dynamic_button,
                 bg="lightgreen").pack(pady=5)
        
        # Counter for unique button names
        self.button_count = 0
    
    def create_dynamic_button(self):
        """
        Creates a new button dynamically.
        The button can destroy itself when clicked.
        """
        self.button_count += 1
        
        # Create a new button
        new_button = tk.Button(self.destroy_container, 
                              text=f"Button {self.button_count} - Click to Remove", 
                              bg="lightpink",
                              padx=10, pady=5)
        
        # Configure the button to destroy itself when clicked
        # We use lambda to pass the button itself to the destroy method
        new_button.config(command=lambda btn=new_button: self.destroy_button(btn))
        
        new_button.pack(side=tk.LEFT, padx=5, pady=5)
    
    def destroy_button(self, button):
        """
        Destroys a specific button.
        After this, the button is gone and can't be used anymore.
        """
        # Optional: confirm before destroying
        # result = messagebox.askyesno("Confirm", "Remove this button?")
        # if result:
        #     button.destroy()
        
        button.destroy()
        
        # Note: After destroy(), the 'button' variable still exists,
        # but it refers to a destroyed widget. Don't try to use it!
        # This would cause an error: button.config(text="new text")


"""
================================================================================
CONCEPT 9: FOCUS_SET() METHOD - MANAGING KEYBOARD FOCUS
================================================================================

WHAT IS IT?
-----------
.focus_set() gives keyboard focus to a specific widget, making it active
and able to receive keyboard events.

SYNTAX:
-------
widget.focus_set()

WHY IS FOCUS IMPORTANT?
-----------------------
- Only ONE widget can have focus at a time
- The focused widget receives keyboard events (key presses)
- The focused widget often shows a visual indicator (border, cursor)
- Users expect certain behaviors: Tab key moves focus, Enter submits forms

FOCUS CHANGES WHEN:
-------------------
- User clicks on a widget
- User presses Tab (moves to next widget)
- You call focus_set() programmatically
- A widget is destroyed while having focus

VISUAL INDICATORS:
------------------
Different widgets show focus differently:
- Entry: blinking cursor appears
- Button: dotted border or highlight
- Frame: may show colored border (if configured)

RELATED METHODS:
----------------
- focus_set() - Give this widget focus
- focus_get() - Returns which widget currently has focus
- focus_force() - Force focus (even if window isn't active)

PRACTICAL USES:
---------------
- Auto-focus on first input field when form appears
- Return focus to search box after search
- Focus "OK" button in dialogs for keyboard navigation
- Implement custom Tab key behavior
- Create keyboard-friendly interfaces

BEST PRACTICES:
---------------
- Focus the most important input when a form/window opens
- Make sure users can see which widget has focus
- Don't fight with the user's focus changes
- Support Tab key for natural focus movement
- Test your app with keyboard-only navigation
"""

class FocusDemo:
    """Demonstrates managing keyboard focus with .focus_set()"""
    
    def __init__(self, parent):
        frame = tk.LabelFrame(parent, text="9. FOCUS_SET() - Managing Keyboard Focus", 
                             padx=10, pady=5, bg="white")
        frame.pack(fill=tk.X, pady=5)
        
        instruction = tk.Label(frame, 
                              text="Click buttons to set focus, or watch focus change as you type:", 
                              bg="white")
        instruction.pack()
        
        # Create entry fields
        entry_frame = tk.Frame(frame, bg="white")
        entry_frame.pack(pady=5)
        
        tk.Label(entry_frame, text="Username:", bg="white").grid(row=0, column=0, padx=5, pady=5)
        self.entry1 = tk.Entry(entry_frame, width=20)
        self.entry1.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(entry_frame, text="Password:", bg="white").grid(row=1, column=0, padx=5, pady=5)
        self.entry2 = tk.Entry(entry_frame, width=20, show="*")
        self.entry2.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(entry_frame, text="Email:", bg="white").grid(row=2, column=0, padx=5, pady=5)
        self.entry3 = tk.Entry(entry_frame, width=20)
        self.entry3.grid(row=2, column=1, padx=5, pady=5)
        
        # Buttons to control focus
        button_frame = tk.Frame(frame, bg="white")
        button_frame.pack(pady=5)
        
        tk.Button(button_frame, text="Focus Username", 
                 command=lambda: self.entry1.focus_set(),
                 bg="lightblue").pack(side=tk.LEFT, padx=5)
        
        tk.Button(button_frame, text="Focus Password", 
                 command=lambda: self.entry2.focus_set(),
                 bg="lightblue").pack(side=tk.LEFT, padx=5)
        
        tk.Button(button_frame, text="Focus Email", 
                 command=lambda: self.entry3.focus_set(),
                 bg="lightblue").pack(side=tk.LEFT, padx=5)
        
        tk.Button(button_frame, text="Show Which Has Focus", 
                 command=self.show_focused_widget,
                 bg="lightyellow").pack(side=tk.LEFT, padx=5)
        
        # Automatically focus the first entry (good UX practice)
        self.entry1.focus_set()
        
        # Bind Enter key to move between fields (custom Tab behavior)
        self.entry1.bind('<Return>', lambda e: self.entry2.focus_set())
        self.entry2.bind('<Return>', lambda e: self.entry3.focus_set())
        self.entry3.bind('<Return>', lambda e: self.submit_form())
    
    def show_focused_widget(self):
        """
        Demonstrates focus_get() to see which widget has focus.
        Useful for debugging focus issues.
        """
        focused = self.entry1.focus_get()
        
        # Figure out which entry has focus
        if focused == self.entry1:
            widget_name = "Username field"
        elif focused == self.entry2:
            widget_name = "Password field"
        elif focused == self.entry3:
            widget_name = "Email field"
        else:
            widget_name = str(focused)
        
        messagebox.showinfo("Focus", f"Current focus: {widget_name}")
    
    def submit_form(self):
        """Example of what might happen when form is submitted"""
        messagebox.showinfo("Submit", "Form would be submitted!\n(Pressing Enter in Email field)")


"""
================================================================================
CONCEPT 10: OBSERVABLE VARIABLES (StringVar, IntVar, DoubleVar, BooleanVar)
================================================================================

WHAT ARE THEY?
--------------
Observable variables are special tkinter objects that:
1. Store a value (string, int, double, or boolean)
2. Can be linked to widgets (Entry, Label, Scale, Checkbutton, etc.)
3. Automatically update the widget when the value changes
4. Notify you (via observers) when the value changes

TYPES OF VARIABLES:
-------------------
- StringVar() - stores strings
- IntVar() - stores integers
- DoubleVar() - stores floating-point numbers
- BooleanVar() - stores True/False

WHY USE THEM?
-------------
- Two-way data binding: widget updates when variable changes, and vice versa
- Observer pattern: run code automatically when values change
- Cleaner code: no need to manually sync widgets and data
- Form validation: check values as user types
- Model-View separation: separate data from UI

BASIC METHODS:
--------------
.get() - Get the current value
.set(value) - Set a new value (automatically updates linked widgets!)

CREATING AND USING:
-------------------
# Create the variable
my_var = tk.StringVar()
my_var.set("initial value")

# Link it to a widget
entry = tk.Entry(root, textvariable=my_var)

# Now the entry and variable are synchronized:
# - Typing in entry updates my_var
# - Calling my_var.set() updates entry

OBSERVER PATTERN - TRACE_ADD():
-------------------------------
You can add an observer function that gets called when the value changes:

def on_change(*args):
    print(f"Value changed to: {my_var.get()}")

my_var.trace_add('write', on_change)

TRACE MODES:
------------
'write' - called when value is written/changed
'read' - called when value is read
'unset' - called when variable is deleted

OLD METHOD (deprecated but still seen):
---------------------------------------
my_var.trace('w', callback) - old way, use trace_add() instead

WIDGETS THAT SUPPORT TEXTVARIABLE/VARIABLE:
--------------------------------------------
- Entry(textvariable=var)
- Label(textvariable=var)
- Button(textvariable=var)
- Checkbutton(variable=var)
- Radiobutton(variable=var)
- Scale(variable=var)
- Spinbox(textvariable=var)

BEST PRACTICES:
---------------
- Use observers for validation, not for every keystroke display
- Remember: observer function needs *args parameter
- Set initial values with .set() after creating variable
- Use appropriate type: IntVar for numbers, StringVar for text
- Don't create new variables in loops - reuse them
"""

class ObservableVariablesDemo:
    """Comprehensive demonstration of tkinter observable variables"""
    
    def __init__(self, parent):
        frame = tk.LabelFrame(parent, text="10. OBSERVABLE VARIABLES - StringVar, IntVar with Observers", 
                             padx=10, pady=5, bg="white")
        frame.pack(fill=tk.X, pady=5)
        
        # === STRINGVAR EXAMPLE ===
        tk.Label(frame, text="StringVar Example:", bg="white", 
                font=("Arial", 10, "bold")).grid(row=0, column=0, columnspan=3, sticky='w', padx=5)
        
        tk.Label(frame, text="Type here:", bg="white").grid(row=1, column=0, padx=5, pady=5)
        
        # Create StringVar
        self.string_var = tk.StringVar()
        self.string_var.set("Hello")  # Set initial value
        
        # Entry linked to StringVar
        # When you type, string_var automatically updates!
        entry = tk.Entry(frame, textvariable=self.string_var, width=20)
        entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Label that shows the value
        self.string_display = tk.Label(frame, text=f"Value: {self.string_var.get()}", 
                                      bg="lightgreen", width=30)
        self.string_display.grid(row=1, column=2, padx=5, pady=5)
        
        # Add observer - this function is called whenever string_var changes
        # The observer automatically updates the display label
        self.string_var.trace_add('write', self.on_string_var_change)
        
        # === INTVAR EXAMPLE ===
        tk.Label(frame, text="IntVar Example:", bg="white", 
                font=("Arial", 10, "bold")).grid(row=2, column=0, columnspan=3, sticky='w', padx=5, pady=(10, 0))
        
        tk.Label(frame, text="Move slider:", bg="white").grid(row=3, column=0, padx=5, pady=5)
        
        # Create IntVar
        self.int_var = tk.IntVar()
        self.int_var.set(50)  # Set initial value
        
        # Scale (slider) linked to IntVar
        # Moving the slider automatically updates int_var!
        scale = tk.Scale(frame, from_=0, to=100, orient=tk.HORIZONTAL, 
                        variable=self.int_var, length=200)
        scale.grid(row=3, column=1, padx=5, pady=5)
        
        # Label that shows the value
        self.int_display = tk.Label(frame, text=f"Value: {self.int_var.get()}", 
                                   bg="lightblue", width=30)
        self.int_display.grid(row=3, column=2, padx=5, pady=5)
        
        # Add observer to IntVar
        self.int_var.trace_add('write', self.on_int_var_change)
        
        # === BOOLEANVAR EXAMPLE ===
        tk.Label(frame, text="BooleanVar Example:", bg="white", 
                font=("Arial", 10, "bold")).grid(row=4, column=0, columnspan=3, sticky='w', padx=5, pady=(10, 0))
        
        # Create BooleanVar
        self.bool_var = tk.BooleanVar()
        self.bool_var.set(False)
        
        # Checkbutton linked to BooleanVar
        check = tk.Checkbutton(frame, text="Enable Feature", 
                              variable=self.bool_var, bg="white")
        check.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky='w')
        
        # Label that shows the value
        self.bool_display = tk.Label(frame, text="Status: Disabled", 
                                    bg="lightcoral", width=30)
        self.bool_display.grid(row=5, column=2, padx=5, pady=5)
        
        # Add observer to BooleanVar
        self.bool_var.trace_add('write', self.on_bool_var_change)
        
        # === DEMONSTRATION BUTTONS ===
        tk.Label(frame, text="Methods Demo (.get() and .set()):", bg="white", 
                font=("Arial", 10, "bold")).grid(row=6, column=0, columnspan=3, sticky='w', padx=5, pady=(10, 0))
        
        button_frame = tk.Frame(frame, bg="white")
        button_frame.grid(row=7, column=0, columnspan=3, pady=5)
        
        # Get methods - retrieve current values
        tk.Button(button_frame, text="Get StringVar", 
                 command=self.demo_get_string,
                 bg="lightyellow").pack(side=tk.LEFT, padx=5)
        
        tk.Button(button_frame, text="Get IntVar", 
                 command=self.demo_get_int,
                 bg="lightyellow").pack(side=tk.LEFT, padx=5)
        
        # Set methods - change values programmatically
        tk.Button(button_frame, text="Set String to 'Python'", 
                 command=lambda: self.string_var.set("Python"),
                 bg="lightgreen").pack(side=tk.LEFT, padx=5)
        
        tk.Button(button_frame, text="Set Int to 75", 
                 command=lambda: self.int_var.set(75),
                 bg="lightgreen").pack(side=tk.LEFT, padx=5)
    
    def on_string_var_change(self, *args):
        """
        This observer is triggered AUTOMATICALLY whenever string_var changes.
        The *args parameter is required but usually not used.
        
        This is called when:
        - User types in the Entry widget
        - You call string_var.set() programmatically
        """
        new_value = self.string_var.get()
        length = len(new_value)
        
        # Update the display label
        self.string_display.config(text=f"Value: '{new_value}' (length: {length})")
        
        # You could add validation here:
        # if length > 20:
        #     messagebox.showwarning("Too Long", "Text is too long!")
    
    def on_int_var_change(self, *args):
        """
        Observer for IntVar - called whenever the slider moves
        or when int_var.set() is called.
        """
        new_value = self.int_var.get()
        doubled = new_value * 2
        
        # Update display with the value and some calculation
        self.int_display.config(text=f"Value: {new_value} | Doubled: {doubled}")
        
        # Example: change color based on value
        if new_value < 30:
            self.int_display.config(bg="lightcoral")
        elif new_value < 70:
            self.int_display.config(bg="lightyellow")
        else:
            self.int_display.config(bg="lightgreen")
    
    def on_bool_var_change(self, *args):
        """Observer for BooleanVar - called when checkbox is toggled"""
        is_enabled = self.bool_var.get()
        
        if is_enabled:
            self.bool_display.config(text="Status: Enabled", bg="lightgreen")
        else:
            self.bool_display.config(text="Status: Disabled", bg="lightcoral")
    
    def demo_get_string(self):
        """Demonstrates .get() method - retrieve current value"""
        current_value = self.string_var.get()
        messagebox.showinfo("Get Method", 
                           f"StringVar.get() returned:\n'{current_value}'")
    
    def demo_get_int(self):
        """Demonstrates .get() method for IntVar"""
        current_value = self.int_var.get()
        messagebox.showinfo("Get Method", 
                           f"IntVar.get() returned:\n{current_value}\n\nType: {type(current_value)}")


"""
================================================================================
MAIN APPLICATION
================================================================================
"""

class TkinterTeachingApp:
    """Main application that demonstrates all concepts"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Events & Methods - Teaching Guide")
        self.root.geometry("900x700")
        
        # Create scrollable main container
        canvas = tk.Canvas(root, bg="lightgray")
        scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="lightgray", padx=10, pady=10)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Title
        title = tk.Label(scrollable_frame, 
                        text="Tkinter Events & Methods - Comprehensive Teaching Guide", 
                        font=("Arial", 16, "bold"), bg="lightgray", pady=10)
        title.pack()
        
        info = tk.Label(scrollable_frame, 
                       text="Interactive examples with detailed explanations of each concept", 
                       font=("Arial", 10, "italic"), bg="lightgray")
        info.pack()
        
        # Initialize all demos
        MessageBoxDemo(scrollable_frame)
        ButtonCommandDemo(scrollable_frame)
        MouseClickDemo(scrollable_frame)
        KeyPressDemo(scrollable_frame)
        EventPropertiesDemo(scrollable_frame)
        BindUnbindDemo(scrollable_frame, root)
        AfterDemo(scrollable_frame, root)
        DestroyDemo(scrollable_frame)
        FocusDemo(scrollable_frame)
        ObservableVariablesDemo(scrollable_frame)
        
        # Pack canvas and scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Enable mouse wheel scrolling
        def on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", on_mousewheel)


# ============================================================================
# RUN THE APPLICATION
# ============================================================================

if __name__ == "__main__":
    root = tk.Tk()
    app = TkinterTeachingApp(root)
    
    print("\n" + "="*80)
    print("TKINTER TEACHING GUIDE STARTED")
    print("="*80)
    print("\nThis application demonstrates 10 key tkinter concepts:")
    print("1. MessageBox - User notifications")
    print("2. Button Command - Simple callbacks")
    print("3. Bind & Mouse Events - Interactive mouse handling")
    print("4. Keyboard Events - Key press handling")
    print("5. Event Object Properties - Event details")
    print("6. bind_all() & unbind() - Global events")
    print("7. after() - Delayed actions and timers")
    print("8. destroy() - Dynamic widget management")
    print("9. focus_set() - Keyboard focus control")
    print("10. Observable Variables - Data binding with observers")
    print("\nRead the source code comments for detailed explanations!")
    print("="*80 + "\n")
    
    root.mainloop()

