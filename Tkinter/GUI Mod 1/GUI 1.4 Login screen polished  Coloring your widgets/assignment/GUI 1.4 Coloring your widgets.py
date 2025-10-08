import tkinter as tk
from tkinter import messagebox

# Dummy credentials for demonstration
CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "secret123"

# Function to handle login
def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
    else:
        show_error_popup()

# Function to show error popup with recovery option
def show_error_popup():
    popup = tk.Toplevel(root)
    popup.title("Login Error")
    popup.geometry("300x180")
    popup.resizable(False, False)

    error_label = tk.Label(popup, text="Incorrect username or password.", fg="red", font=("Arial", 10))
    error_label.pack(pady=10)

    recovery_label = tk.Label(popup, text="Forgot your password?", font=("Arial", 10))
    recovery_label.pack()

    reset_button = tk.Button(popup, text="Reset Password", bg="#4DB6AC", activebackground="#00796B", fg="white", font=("Arial", 10), relief="raised")
    reset_button.config(command=reset_password)
    reset_button.pack(pady=10)

    close_button = tk.Button(popup, text="Close", bg="#B0BEC5", activebackground="#455A64", fg="black", font=("Arial", 10), relief="raised")
    close_button.config(command=popup.destroy)
    close_button.pack()

# Simulated password reset
def reset_password():
    messagebox.showinfo("Password Recovery", "Recovery instructions sent to your email.")

# Main window setup
root = tk.Tk()
root.title("Login Portal")
root.geometry("320x200")
root.resizable(False, False)

# Labels and entry fields
tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Login button with color states
login_button = tk.Button(root, text="Login", width=15, bg="#5C6BC0", activebackground="#3949AB", fg="white", font=("Arial", 10), relief="raised", command=login)
login_button.grid(row=2, column=1, pady=20)

# Run the application
root.mainloop()