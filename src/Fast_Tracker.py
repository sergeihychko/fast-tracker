import os
import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from pandastable import Table, TableModel
import pandas as pd
import ftdataclasses

from pywin.dialogs import login

import database_driver


class MainApp(tk.Tk):
    def __init__(self):
        #super().__init__()

        #self.title_font = tk.font.Font(family='Helvetica', size=18, weight="bold")
        # tk._test()
        root = tk.Tk()
        root.title("Fast Tracker")
        root.minsize(340, 440)
        # root.geometry("340x440")
        root.configure(background="#333333")

        # 1. Create the main menu bar
        menubar = tk.Menu(root)
        root.config(menu=menubar)

        # 2. Create a 'Entry' submenu
        entry_menu = tk.Menu(menubar, tearoff=0)
        entry_menu.add_command(label="Edit Day", command=lambda: edit_day())
        entry_menu.add_command(label="New Meal", command=lambda: edit_meal())
        entry_menu.add_command(label="New Food", command=lambda: edit_foodstuff())
        entry_menu.add_separator()
        entry_menu.add_command(label="Exit", command=root.quit)

        # 2. Create a 'Login/Out' submenu
        logout_menu = tk.Menu(menubar, tearoff=0)
        logout_menu.add_command(label="Logout", command=lambda: print("Logout"))
        logout_menu.add_separator()
        logout_menu.add_command(label="Exit", command=root.quit)

        # 3. Add the submenu to the menu bar
        menubar.add_cascade(label="Entry", menu=entry_menu)
        menubar.add_cascade(label="User", menu=logout_menu)


        # Initialize global user data container in the controller
        self.current_user = 0
        self.current_day = 0
        self.frame = tk.Frame(root, background="#333333")
        self.entry_frame = tk.Frame(root, background="#333333")
        self.day_frame = tk.Frame(root, background="#333333")
        self.edit_d_frame = tk.Frame(root, background="#333333")
        self.edit_fs_frame = tk.Frame(root, background="#333333")
        self.edit_meal_frame = tk.Frame(root, background="#333333")

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
            self.frame.pack_forget()
            # Remove all existing child widgets
            self.frame.pack_forget()
            self.entry_frame.pack_forget()
            for child in self.frame.winfo_children():
                child.destroy()
            for child in self.entry_frame.winfo_children():
                child.destroy()
            data = database_driver.get_user_data(self.current_user)
            print("back from get_user_data call with data : " + str(data))
            # Iterate through rows and columns to place widgets
            for row_idx, row_data in enumerate(data):
                date_id = row_data[0]
                for col_idx, value in enumerate(row_data):
                    # Create a Label widget for each cell
                    label = tk.Label(self.entry_frame, text=str(value), relief="solid", borderwidth=1, padx=5, pady=5)
                    # Place the widget in the grid
                    label.grid(row=row_idx, column=col_idx, sticky="nsew")
                btn = tk.Button(self.entry_frame, text="Edit day " + str(date_id), relief="solid", borderwidth=1, padx=5, pady=5, bg="dark blue",
                                fg="white", command=lambda date_id=date_id: page(date_id))
                #print("just wrote out the button call page({date_id})" + str(date_id))
                # Place the widget in the grid
                btn.grid(row=row_idx, column=col_idx + 1, sticky="nsew")
            self.entry_frame.pack()

        def backToDays():
            # Remove all existing child widgets
            self.entry_frame.pack_forget()
            self.day_frame.pack_forget()
            for child in self.entry_frame.winfo_children():
                child.destroy()
            for child in self.day_frame.winfo_children():
                child.destroy()
            create_entry_frame()

        def page(date_id):
            # Remove all existing child widgets
            self.entry_frame.pack_forget()
            self.day_frame.pack_forget()
            for child in self.entry_frame.winfo_children():
                child.destroy()
            for child in self.day_frame.winfo_children():
                child.destroy()

            day_total_calories = 0
            day_data = database_driver.get_day_entry(date_id)
            entries = database_driver.get_days_detail(date_id)
            print(" date_id : " + str(date_id)  + " /   day_data : " + str(day_data))

            day_label = tkinter.Label(self.day_frame, text=day_data[1], bg="#333333", fg="#FFFFFF", font={"Ariel", 16})
            date_label = tkinter.Label(self.day_frame, text=day_data[3], bg="#333333", fg="#FFFFFF", font={"Ariel", 16})

            day_label.grid(row=0, column=0)
            date_label.grid(row=0, column=1)
            row_idx = 0

            # df = pd.DataFrame(data=entries)
            # df.columns = ["Description", "Servings", "Calories", "Protein", "Carbs", "Fiber", "Fat"]
            #
            # pt = Table(day_frame, dataframe=df, showtoolbar=False, showstatusbar=False)
            # pt.show()
            # Iterate through headers to place widgets
            columns = ["Description", "Servings", "Calories", "Protein", "Carbs", "Fiber", "Fat"]
            for head_idx, value in enumerate(columns):
                header_label = tk.Label(self.day_frame, text=str(value), relief="solid", borderwidth=1, padx=5, pady=5)
                header_label.grid(row=1, column=head_idx, sticky="nsew")

            if entries:
                # Iterate through rows and columns to place widgets
                for row_idx, row_data in enumerate(entries):
                    date_id = row_data[0]
                    print(" a day's values : " + str(date_id))
                    for col_idx, value in enumerate(row_data):
                        # Create a Label widget for each cell
                        label = tk.Label(self.day_frame, text=str(value), relief="solid", borderwidth=1, padx=5, pady=5)
                        # Place the widget in the grid
                        label.grid(row=row_idx + 2, column=col_idx, sticky="nsew")
                        if col_idx == 2: day_total_calories += int(value)

                back_button = tk.Button(self.day_frame, text="Edit day", relief="solid", borderwidth=1, padx=5, pady=5,
                                        bg="dark blue", fg="white", command=backToDays)
                back_button.grid(row=row_idx + 3, column=0, columnspan=2)
            else:
                back_button = tk.Button(self.day_frame, text="Edit day", relief="solid", borderwidth=1, padx=5, pady=5,
                                        bg="dark blue", fg="white", command=backToDays)
                back_button.grid(row=3, column=0, columnspan=2)

            calories_label = tkinter.Label(self.day_frame, text='Calories: ' + str(day_total_calories), bg="#333333", fg="#FFFFFF", font={"Ariel", 16})
            calories_label.grid(row=0, column=2, columnspan=3       )
            self.day_frame.pack()

        def edit_day():
            self.edit_d_frame.pack_forget()
            for child in self.edit_d_frame.winfo_children():
                child.destroy()
            self.edit_d_frame.pack()

        def edit_foodstuff():
            self.edit_fs_frame.pack_forget()
            for child in self.edit_fs_frame.winfo_children():
                child.destroy()
            self.edit_fs_frame.pack()

        def edit_meal():
            self.edit_meal_frame.pack_forget()
            for child in self.edit_meal_frame.winfo_children():
                child.destroy()
            self.edit_meal_frame.pack()
            fields = ('Meal ID', 'Food_ID')
            entries = {}

            def submit_data():
                # Retrieve values from Entry widgets
                meal = ftdataclasses.Meal(
                    id=entries['id'].get(),
                    name=entries['name'].get()
                )
                print(f"Created: {meal}")

            for idx, field in enumerate(fields):
                # Header
                tk.Label(self.edit_meal_frame, text=field.title()).grid(row=idx, column=0, sticky='w')
                # Input Box
                e = tk.Entry(root)
                e.grid(row=idx, column=1)
                entries[field] = e

            tk.Button(self.edit_meal_frame, text="Submit", command=submit_data).grid(row=len(fields), column=1)

        # Create widgets
        login_label = tkinter.Label(self.frame, text="Login", bg="#333333", fg="#FFFFFF", font={"Ariel", 25})
        username_label = tkinter.Label(self.frame, text="Username", bg="#333333", fg="#FFFFFF", font={"Ariel", 16})
        username_entru =tkinter.Entry(self.frame)
        password_entry = tkinter.Entry(self.frame, show="*")
        password_label = tkinter.Label(self.frame, text="Password", bg="#333333", fg="#FFFFFF", font={"Ariel", 16})
        login_button = tkinter.Button(self.frame, text="Login", bg="#FF3399", command=login, font={"Ariel", 16})

        login_label.grid(row=0, column=0, columnspan=2)
        username_label.grid(row=1, column=0)
        username_entru.grid(row=1, column=1)
        password_label.grid(row=2, column=0)
        password_entry.grid(row=2, column=1)
        login_button.grid(row=3, column=0, columnspan=2)

        self.frame.pack()

        root.mainloop()


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
