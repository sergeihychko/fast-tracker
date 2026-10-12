import os
import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from pandastable import Table, TableModel
import pandas as pd

from pywin.dialogs import login

import database_driver


class MainApp(tk.Tk):
    def __init__(self):
        #super().__init__()

        #self.title_font = tk.font.Font(family='Helvetica', size=18, weight="bold")

        # 1. Initialize global user data container in the controller
        self.current_user = 0


        # Define the database file path
        db_path = "../data/fast-tracker.db"

        # Check if the file exists before attempting to delete
        #TODO remove after initial testing
        if os.path.exists(db_path):
            os.remove(db_path)
            print(f"Database '{db_path}' has been deleted.")
        else:
            print(f"Database '{db_path}' does not exist.")

        user_id = 0
        database_driver.init()
        database_driver.create_user()
        database_driver.create_test_days()

        def login():
            user_id = database_driver.check_login(username_entru.get(), password_entry.get())
            print(f"User ID: {user_id}")
            if (user_id == 0):
                messagebox.showerror("Error", "Login Failed")
            else:
                self.current_user = user_id
                create_entry_frame()


        def create_entry_frame():
            frame.pack_forget()
            data = database_driver.get_user_data(self.current_user)
            # Iterate through rows and columns to place widgets
            for row_idx, row_data in enumerate(data):
                date_id = 0
                date_name = ""
                date_text = ""
                date_id = row_data[0]
                date_name = row_data[1]
                date_text = row_data[3]
                for col_idx, value in enumerate(row_data):
                    # Create a Label widget for each cell
                    label = tk.Label(entry_frame, text=str(value), relief="solid", borderwidth=1, padx=5, pady=5)
                    # Place the widget in the grid
                    label.grid(row=row_idx, column=col_idx, sticky="nsew")
                btn = tk.Button(entry_frame, text="Edit day", relief="solid", borderwidth=1, padx=5, pady=5, bg="dark blue",
                                fg="white", command=lambda: page(date_id, date_name, date_text))
                # Place the widget in the grid
                btn.grid(row=row_idx, column=col_idx + 1, sticky="nsew")
            entry_frame.pack()

        def backToDays():
            day_frame.pack_forget()
            create_entry_frame()

        def page(date_id, date_name, date_text):
            day_frame.pack_forget()
            print("Edit day button clicked : ")
            entries = database_driver.get_days_detail(date_id, self.current_user)
            print("entries : " + str(entries))
            entry_frame.pack_forget()

            day_label = tkinter.Label(day_frame, text=date_name, bg="#333333", fg="#FFFFFF", font={"Ariel", 16})
            date_label = tkinter.Label(day_frame, text=date_text, bg="#333333", fg="#FFFFFF", font={"Ariel", 16})

            day_label.grid(row=0, column=0)
            date_label.grid(row=0, column=1)

            df = pd.DataFrame(data=entries)
            df.columns = ["Description", "Servings", "Calories", "Protein", "Carbs", "Fiber", "Fat"]

            pt = Table(day_frame, dataframe=df, showtoolbar=True, showstatusbar=True)
            pt.show()

            #print("entries for the date : " + str(entries))
            # for row_idx, row_data in enumerate(entries):
            #     for col_idx, value in enumerate(row_data):
            #         # Create a Label widget for each cell
            #         label = tk.Label(day_frame, text=str(value), relief="solid", borderwidth=1, padx=5, pady=5)
            #         # Place the widget in the grid
            #         label.grid(row=row_idx, column=col_idx, sticky="nsew")

            back_button = tk.Button(day_frame, text="Edit day", relief="solid", borderwidth=1, padx=5, pady=5, bg="dark blue", fg="white", command=backToDays)
            back_button.grid(row=1, column=0, columnspan=2)

            day_frame.pack()

        #tk._test()
        root = tk.Tk()
        root.title("Fast Tracker")
        root.minsize(340,440)
        #root.geometry("340x440")
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

        # General day form
        day_frame = tk.Frame(root, background="#333333")

        root.mainloop()


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
