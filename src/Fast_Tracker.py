import os
import tkinter
import tkinter as tk
from tkinter import messagebox

from pywin.dialogs import login

import database_driver

# Define the database file path
db_path = "../data/fast-tracker.db"

# Check if the file exists before attempting to delete
#TODO remove after initial testing
if os.path.exists(db_path):
    os.remove(db_path)
    print(f"Database '{db_path}' has been deleted.")
else:
    print(f"Database '{db_path}' does not exist.")

database_driver.init()
database_driver.create_user()
database_driver.create_test_days()

def login():
    user_id = database_driver.check_login(username_entru.get(), password_entry.get())
    print(f"User ID: {user_id}")
    if (user_id == 0):
        messagebox.showerror("Error", "Login Failed")
    else:
        frame.pack_forget()
        data = database_driver.get_user_data(user_id)
        # Iterate through rows and columns to place widgets
        for row_idx, row_data in enumerate(data):
            for col_idx, value in enumerate(row_data):
                # Create a Label widget for each cell
                label = tk.Label(entry_frame, text=str(value), relief="solid", borderwidth=1, padx=5, pady=5)
                # Place the widget in the grid
                label.grid(row=row_idx, column=col_idx, sticky="nsew")
        entry_frame.pack()

#tk._test()
root = tk.Tk()
root.title("Fast Tracker")
root.geometry("340x440")
root.configure(background="#333333")

frame = tk.Frame(root, background="#333333")

# Create widgets
login_label = tkinter.Label(frame, text="Login", bg="#333333", fg="#FFFFFF", font={"Ariel", 25})
username_label = tkinter.Label(frame, text="Username", bg="#333333", fg="#FFFFFF", font={"Ariel", 16})
username_entru =tkinter.Entry(frame)
password_entry = tkinter.Entry(frame, show="*")
password_label = tkinter.Label(frame, text="Password", bg="#333333", fg="#FFFFFF", font={"Ariel", 16})
login_button = tkinter.Button(frame, text="Login", bg="#FF3399", command=login, font={"Ariel", 16})

login_label.grid(row=0, column=0, columnspan=2)
username_label.grid(row=1, column=0)
username_entru.grid(row=1, column=1)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1)
login_button.grid(row=3, column=0, columnspan=2)

frame.pack()

# General data page
entry_frame = tk.Frame(root, background="#333333")

root.mainloop()




