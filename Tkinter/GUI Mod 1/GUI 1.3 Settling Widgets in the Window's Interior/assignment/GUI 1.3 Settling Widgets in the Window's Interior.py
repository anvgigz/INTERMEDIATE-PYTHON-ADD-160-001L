import tkinter as tk

root = tk.Tk()

root.title("login")

#label Widgets
name_label = tk.Label(root, text="Name:")
email_label = tk.Label(root, text="Email:")
password_label = tk.Label(root,text="Password:")


#entry widgets
name_entry = tk.Entry(root)
email_entry = tk.Entry(root)
password_entry = tk.Entry(root, show="*")


#place Label/entry widgets
#name V
name_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
name_entry.grid(row=0, column=1, padx=10, pady=5)
#email V
email_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
email_entry.grid(row=1, column=1, padx=10, pady=5)
#password V
password_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
password_entry.grid(row=2, column=1, padx=10, pady=5)


root.mainloop()