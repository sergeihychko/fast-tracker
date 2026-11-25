import os
import re
import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import ftdataclasses
from configparser import ConfigParser
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

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

        # 3. Create a 'Reports' submenu
        reports_menu = tk.Menu(menubar, tearoff=0)
        reports_menu.add_command(label="Monthly Calorie Averages", command=lambda: report_monthly_calories())
        reports_menu.add_command(label="Monthly Protein Averages", command=lambda: report_monthly_protein())
        reports_menu.add_command(label="Monthly Fiber Averages", command=lambda: report_monthly_fiber())
        reports_menu.add_command(label="Monthly Carb Averages", command=lambda: report_monthly_carbs())
        reports_menu.add_command(label="Monthly Fat Averages", command=lambda: report_monthly_fat())
        reports_menu.add_separator()
        reports_menu.add_command(label="Monthly Heart rate Averages", command=lambda: report_monthly_hr())
        reports_menu.add_command(label="Monthly BP Averages", command=lambda: report_monthly_bp())
        reports_menu.add_separator()
        reports_menu.add_command(label="Monthly Full Report", command=lambda: report_monthly_full())
        reports_menu.add_separator()
        reports_menu.add_command(label="Exit", command=root.quit)

        # 4. Add the submenu to the menu bar
        menubar.add_cascade(label="Entry", menu=entry_menu)
        menubar.add_cascade(label="User", menu=logout_menu)
        menubar.add_cascade(label="Reports", menu=reports_menu)


        # Initialize global user data container in the controller
        self.root = root
        self.current_user = 0
        self.current_day = 0
        self.frame = tk.Frame(root, background="#333333")
        self.entry_frame = tk.Frame(root, background="#333333")
        self.day_frame = tk.Frame(root, background="#333333")
        self.edit_d_frame = tk.Frame(root, background="#333333")
        self.edit_fs_frame = tk.Frame(root, background="#333333")
        self.report_frame = tk.Frame(root, background="#333333")
        self.report_month = 11
        self.report_year = 2026
        self.popup = None
        self.inner_frame = None
        self.geometry = "600x550"
        self.geometry_full = "1200x500"

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
            if int(self.debug) < 1:
                user_id = database_driver.check_login(username_entru.get(), password_entry.get())
                print(f"User ID: {user_id}")
                if (user_id == 0):
                    messagebox.showerror("Error", "Login Failed")
                else:
                    self.current_user = user_id
                    create_entry_frame()
            else:
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
            print("user : " + str(self.current_user))

            row_offset = 2
            def rdn_on_change(event):
                self.rdn = combo.get()

            # Define options for retrieve days number combo box
            options = ["10", "20", "100"]
            # Create the retrieve days number combo box
            combo = ttk.Combobox(self.entry_frame, values=options, state="readonly")
            combo.current(0)
            combo.grid(row=1, column=1, sticky='w', pady=20)
            # Bind the selection change event
            combo.bind("<<ComboboxSelected>>", rdn_on_change)

            data = database_driver.get_user_data(self.current_user, self.rdn)
            # Iterate through rows and columns to place widgets
            for row_idx, row_data in enumerate(data):
                date_id = row_data[0]
                for col_idx, value in enumerate(row_data):
                    # Create a Label widget for each cell
                    label = tk.Label(self.entry_frame, text=str(value), relief="solid", borderwidth=1, padx=5, pady=5)
                    # Place the widget in the grid
                    label.grid(row=row_idx + row_offset, column=col_idx, sticky="nsew")
                btn = tk.Button(self.entry_frame, text="Edit day " + str(date_id), relief="solid", borderwidth=1, padx=5, pady=5, bg="dark blue",
                                fg="white", command=lambda date_id=date_id: page(date_id))
                # Place the widget in the grid
                btn.grid(row=row_idx + row_offset, column=col_idx + 1, sticky="nsew")
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
            day_total_carbs = 0
            day_total_protein = 0
            day_total_fiber = 0
            day_total_fat = 0
            day_data = database_driver.get_day_entry(date_id)
            entries = database_driver.get_days_detail(date_id)
            print(" date_id : " + str(date_id)  + " /   day_data : " + str(day_data))

            day_label = tkinter.Label(self.day_frame, text=day_data[1], bg="#333333", fg="#FFFFFF", font={"Ariel", 16})
            date_label = tkinter.Label(self.day_frame, text=day_data[3], bg="#333333", fg="#FFFFFF", font={"Ariel", 16})

            day_label.grid(row=0, column=0)
            date_label.grid(row=0, column=1)
            row_idx = 0

            columns = ["Description", "Servings", "Calories", "Carbs", "Protein", "Fiber", "Fat"]
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
                        if col_idx == 3: day_total_carbs += int(value)
                        if col_idx == 4: day_total_protein += int(value)
                        if col_idx == 5: day_total_fiber += int(value)
                        if col_idx == 5: day_total_fat += int(value)

                back_button = tk.Button(self.day_frame, text="Edit day", relief="solid", borderwidth=1, padx=5, pady=5,
                                        bg="dark blue", fg="white", command=backToDays)
                back_button.grid(row=row_idx + 4, column=0, columnspan=2)
                # Totals row
                tk.Label(self.day_frame, text="Totals").grid(row=row_idx + 3, column=0)
                tk.Label(self.day_frame, text=str(day_total_calories)).grid(row=row_idx + 3, column=2)
                if day_total_carbs <= self.carbs_threshold:
                    tk.Label(self.day_frame, text=str(day_total_carbs), fg="green").grid(row=row_idx + 3, column=3)
                else:
                    tk.Label(self.day_frame, text=str(day_total_carbs), fg="orange").grid(row=row_idx + 3, column=3)
                if day_total_protein >= self.protein_threshold:
                    tk.Label(self.day_frame, text=str(day_total_protein), fg="green").grid(row=row_idx + 3, column=4)
                else:
                    tk.Label(self.day_frame, text=str(day_total_protein), fg="red").grid(row=row_idx + 3, column=4)
                if day_total_fiber >= self.fiber_threshold:
                    tk.Label(self.day_frame, text=str(day_total_fiber), fg="green").grid(row=row_idx + 3, column=5)
                else:
                    tk.Label(self.day_frame, text=str(day_total_fiber), fg="red").grid(row=row_idx + 3, column=5)
                tk.Label(self.day_frame, text=str(day_total_fat)).grid(row=row_idx + 3, column=6)
            else:
                back_button = tk.Button(self.day_frame, text="Edit day", relief="solid", borderwidth=1, padx=5, pady=5,
                                        bg="dark blue", fg="white", command=backToDays)
                back_button.grid(row=3, column=0, columnspan=2)


            calories_label = tkinter.Label(self.day_frame, text='Calories: ' + str(day_total_calories), bg="#333333", fg="#FFFFFF", font={"Ariel", 16})
            calories_label.grid(row=0, column=2, columnspan=3)
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
            next_foodstuff_id = database_driver.find_next_id("foodstuffs")
            defualt_serving = 1

            # 1. Create the secondary window
            popup = tk.Toplevel(self.root, bg="dark blue")
            popup.title("Enter Data")
            popup.geometry("400x350")

            self.edit_fs_frame = tk.Frame(popup, background="#333333")

            fields = ('Food_ID', 'Description', 'Serving', 'Calories', 'Carbs', 'Protein', 'Fiber', 'Fat')

            foodstuffs_id_label = tk.Label(self.edit_fs_frame, text=fields[0]).grid(row=1, column=0, sticky='e')
            entry_foodstuffs_id = tk.Entry(self.edit_fs_frame, width=10)
            entry_foodstuffs_id.insert(0, str(next_foodstuff_id))
            entry_foodstuffs_id.config(state="readonly")
            entry_foodstuffs_id.grid(row=1, column=1, sticky='w')
            foodstuff_desc_label= tk.Label(self.edit_fs_frame, text=fields[1]).grid(row=2, column=0, sticky='e')
            entry_foodstuff_desc = tk.Entry(self.edit_fs_frame, width=10)
            entry_foodstuff_desc.grid(row=2, column=1, sticky='w')
            foodstuffs_serving_label = tk.Label(self.edit_fs_frame, text=fields[2]).grid(row=3, column=0, sticky='e')
            entry_foodstuffs_serving = tk.Entry(self.edit_fs_frame, width=10)
            entry_foodstuffs_serving.insert(0, str(defualt_serving))
            entry_foodstuffs_serving.config(state="readonly")
            entry_foodstuffs_serving.grid(row=3, column=1, sticky='w')
            foodstuff_calories_label = tk.Label(self.edit_fs_frame, text=fields[3]).grid(row=4, column=0, sticky='e')
            entry_foodstuff_calories = tk.Entry(self.edit_fs_frame, width=10)
            entry_foodstuff_calories.grid(row=4, column=1, sticky='w')
            foodstuffs_carbs_label = tk.Label(self.edit_fs_frame, text=fields[4]).grid(row=5, column=0, sticky='e')
            entry_foodstuffs_carbs = tk.Entry(self.edit_fs_frame, width=10)
            entry_foodstuffs_carbs.grid(row=5, column=1, sticky='w')
            foodstuff_protein_label = tk.Label(self.edit_fs_frame, text=fields[5]).grid(row=6, column=0, sticky='e')
            entry_foodstuff_protein = tk.Entry(self.edit_fs_frame, width=10)
            entry_foodstuff_protein.grid(row=6, column=1, sticky='w')
            foodstuffs_fiber_label = tk.Label(self.edit_fs_frame, text=fields[6]).grid(row=7, column=0, sticky='e')
            entry_foodstuffs_fiber = tk.Entry(self.edit_fs_frame, width=10)
            entry_foodstuffs_fiber.grid(row=7, column=1, sticky='w')
            foodstuff_fat_label = tk.Label(self.edit_fs_frame, text=fields[7]).grid(row=8, column=0, sticky='e')
            entry_foodstuff_fat = tk.Entry(self.edit_fs_frame, width=10)
            entry_foodstuff_fat.grid(row=8, column=1, sticky='w')

            def submit_data(foodstuff_id, foodstuff_desc, serving, calories, carbs, protein, fiber, fat):
                foodstuff = ftdataclasses.Foodstuff(id=foodstuff_id, description=foodstuff_desc, serving_size=serving, calories=calories, carbs=carbs, protein=protein, fiber=fiber, fat=fat)
                print("submit_data with foodstuff id : " + str(foodstuff.id) + " f_id :  " + str(foodstuff.description))
                #TODO: actually call the database insert method
                db_update = database_driver.insert_foodstuff(foodstuff)
                print(f"Created: {foodstuff}")
                messagebox.showinfo("Created: Inserted into Foodstuffs table")
                popup.destroy()

            def cancel():
                self.edit_fs_frame.pack_forget()
                for child in self.edit_fs_frame.winfo_children():
                    child.destroy()
                popup.destroy()

            tk.Button(self.edit_fs_frame, text="Submit", bg="#333333", fg="#FFFFFF",
                      command=lambda: submit_data(entry_foodstuffs_id.get(), entry_foodstuff_desc.get(),
                                                  entry_foodstuffs_serving.get(), entry_foodstuff_calories.get(),
                                                  entry_foodstuffs_carbs.get(), entry_foodstuff_protein.get(),
                                                  entry_foodstuffs_fiber.get(), entry_foodstuffs_fiber.get())).grid(
                row=9,
                column=0,
                padx=5)
            tk.Button(self.edit_fs_frame, text="Cancel", bg="#333333", fg="#FFFFFF", command=cancel).grid(row=9,
                                                                                                            column=1,
                                                                                                            padx=5)
            self.edit_fs_frame.pack()

        def edit_meal():
            next_meal_id = database_driver.find_next_id("meals")
            # Create StringVar to track entry content
            entry_var = tk.StringVar()
            foodstuff_var = tk.StringVar()

            # 1. Create the secondary window
            popup = tk.Toplevel(self.root, bg="dark blue")
            popup.title("Enter Data")
            popup.geometry("400x350")
            results = []
            def fetch_data(*args):
                results = database_driver.find_foodstuff_by_partial(entry_var.get())
                if results:
                    combo.configure(values=results)
                    combo.set(results[0])
                    print("results : " + str(results))

            def set_foodstuff(event):
                print("attempting to set foodstuff_id from combo box select")
                match = re.search(r'\d+', combo.selection_get())
                foodstuff_selected_id = match.group()
                foodstuff_var.set(foodstuff_selected_id)

            self.edit_meal_frame = tk.Frame(popup, background="#333333")

            fields = ('Meal ID', 'Food_ID')

            meal_id_label = tk.Label(self.edit_meal_frame, text=fields[0]).grid(row=1, column=0, sticky='w')
            entry_meal_id = tk.Entry(self.edit_meal_frame, width=10)
            entry_meal_id.insert(0, str(next_meal_id))
            entry_meal_id.config(state="readonly")
            entry_meal_id.grid(row=1, column=1, sticky='w')
            meal_foodstuff_label= tk.Label(self.edit_meal_frame, text=fields[1]).grid(row=2, column=0, sticky='w')
            entry_foodstuff_id = tk.Entry(self.edit_meal_frame, textvariable=foodstuff_var, width=10)
            entry_foodstuff_id.insert(0, 0)
            entry_foodstuff_id.grid(row=2, column=1, sticky='w')
            meal_foodstuff_llokup_label = tk.Label(self.edit_meal_frame, text="Lookup existing foods", bg="#333333", fg="#FFFFFF").grid(row=3, column=0, columnspan=2, sticky='w')
            entry_foodstuff_lookup = tk.Entry(self.edit_meal_frame, textvariable=entry_var, width=20)
            entry_foodstuff_lookup.grid(row=4, column=0, sticky='e')
            combo = ttk.Combobox(self.edit_meal_frame, values=results)
            #combo.current(0)  # Set default selection (optional)
            combo.grid(row=4, column=1, sticky='w')
            combo.bind("<KeyRelease>", set_foodstuff)
            # Optional: Bind to <FocusIn> to catch mouse selections immediately
            combo.bind("<FocusIn>", set_foodstuff)
            # Register the trace callback
            entry_var.trace_add("write", fetch_data)


            # 4. Function to handle selection (optional)
            def on_select(event):
                selected_value = combo.get()[0]
                print(f"Selected: {selected_value}")

            # Bind the selection event
            combo.bind("<<ComboboxSelected>>", on_select)

            def submit_data(meal_id, foodstuff_id):
                meal = ftdataclasses.Meal(id=meal_id, foodstuff_id=foodstuff_id)
                print("submit_data with meal id : " + str(meal.id) + " f_id :  " + str(meal.foodstuff_id))
                db_update = database_driver.insert_meal(meal)
                print(f"Created: {meal}")
                messagebox.showinfo("Created: Inserted into Meal table")
                popup.destroy()

            def cancel():
                self.edit_meal_frame.pack_forget()
                for child in self.edit_meal_frame.winfo_children():
                    child.destroy()
                popup.destroy()

            tk.Button(self.edit_meal_frame, text="Submit", bg="#333333", fg="#FFFFFF", command = lambda: submit_data(entry_meal_id.get(), entry_foodstuff_id.get())).grid(row=5,
                                                                                                                 column=0,
                                                                                                                 padx=5)
            tk.Button(self.edit_meal_frame, text="Cancel", bg="#333333", fg="#FFFFFF", command=cancel).grid(row=5,
                                                                                                            column=1,
                                                                                                            padx=5)

            self.edit_meal_frame.pack()

        def create_rep_widget(dataset, parent_frame, col_header, column_offset):
            #report canvas
            # 1. Convert to Pandas DataFrame
            df = pd.DataFrame(dataset, columns=[col_header, 'Day'])

            # 2. Create the Matplotlib Figure
            fig = Figure(figsize=(5, 4), dpi=100)
            ax = fig.add_subplot(111)

            # 3. Plot the DataFrame using Pandas
            df.plot(ax=ax, marker='o')
            ax.set_title("Monthly Value over day Graph")
            ax.set_xlabel("Index")
            ax.set_ylabel("Values")

            # 4. Embed in Tkinter
            canvas = FigureCanvasTkAgg(fig, master=parent_frame)
            canvas.draw()

            # 5. Use .grid() to place the widget
            canvas.get_tk_widget().grid(row=0, column=0+column_offset, columnspan=2, padx=10, pady=10)

        def output_average(filtered_list, parent_frame, meta_type, column_offset):
            day_average = get_average_from_dataset(filtered_list)
            ALabel = tk.Label(parent_frame, text="Average daily " + str(meta_type), fg="white", bg="#333333",
                              font={"Ariel", 30})
            ALabel.grid(row=4, column=0+column_offset, sticky='w')
            AverageValue = tk.Label(parent_frame, text=str(day_average), fg="white", bg="#333333", font={"Ariel", 30})
            AverageValue.grid(row=4, column=1+column_offset, sticky='w')
            tk.Button(parent_frame, text="Close", bg="#333333", fg="#FFFFFF", command=cancel).grid(row=5,
                                                                                                        column=1,
                                                                                                        padx=5)

        def get_average_from_dataset(filtered_list):
            data = np.array(filtered_list)
            x, y = data.T
            tcal = np.array(x)
            day_average = round(np.sum(tcal) / len(x), 2)
            return day_average

        def create_reports_window_widget(header, geometry):
            # Create the secondary window
            self.popup = tk.Toplevel(self.root, bg="dark blue")
            self.popup.title("Monthly " + header + " Report")
            self.popup.geometry("600x550")
            self.report_frame = tk.Frame(self.popup, background="#333333")

            # 3. Create Canvas and Horizontal Scrollbar
            #p_canvas = tk.Canvas(self.popup)
            #h_scrollbar = tk.Scrollbar(self.popup, orient="horizontal", command=p_canvas.xview)

            # 4. Grid the canvas and scrollbar
            #p_canvas.grid(row=0, column=0, sticky="nsew")
            #h_scrollbar.grid(row=1, column=0, sticky="ew")
            # Inner frame where you grid your widgets
            #self.inner_frame = tk.Frame(p_canvas)
            # 5. Link scrollbar to canvas
            #p_canvas.configure(xscrollcommand=h_scrollbar.set)
            #p_canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")


            # Update scroll region when inner frame resizes
            #self.report_frame.bind("<Configure>", lambda e: p_canvas.configure(scrollregion=p_canvas.bbox("all")))


        def cleanup_rep_widget():
            try:
                self.report_frame.pack_forget()
                for child in self.report_frame.winfo_children():
                    child.destroy()
                self.report_frame.pack()
            except tkinter.TclError:
                pass  # Widget already destroyed

        def cancel():
            self.report_frame.pack_forget()
            for child in self.report_frame.winfo_children():
                child.destroy()
            self.popup.destroy()

        def report_monthly_calories():
            meta_type = "Calories"
            cleanup_rep_widget()
            create_reports_window_widget(meta_type, self.geometry)

            month = self.report_month
            year = self.report_year
            print("\n Reports / Monthly averages called \n")
            ids = database_driver.get_monthly_averages(month, year)
            datapoints = database_driver.get_daily_calorie_totals(month, year, ids)
            filtered_list = [tup for tup in datapoints if tup[0] != 0]

            # call generic graph method
            create_rep_widget(filtered_list, self.report_frame, "Calories", 0)

            output_average(filtered_list, self.report_frame, meta_type, 0)

            self.report_frame.grid(row=0, column=0, sticky="nsew")

        def report_monthly_protein():
            meta_type = "Protein"
            cleanup_rep_widget()
            create_reports_window_widget(meta_type, self.geometry)

            month = self.report_month
            year = self.report_year
            ids = database_driver.get_monthly_averages(month, year)
            datapoints = database_driver.get_daily_protein_totals(month, year, ids)
            filtered_list = [tup for tup in datapoints if tup[0] != 0]

            # call generic graph method
            create_rep_widget(filtered_list, self.report_frame, "Protein", 0)

            output_average(filtered_list, self.report_frame, meta_type, 0)
            self.report_frame.pack()

        def report_monthly_fiber():
            meta_type = "Fiber"
            cleanup_rep_widget()
            create_reports_window_widget(meta_type, self.geometry)

            month = self.report_month
            year = self.report_year
            print("\n Reports / Monthly averages called \n")
            ids = database_driver.get_monthly_averages(month, year)
            datapoints = database_driver.get_daily_fiber_totals(month, year, ids)
            filtered_list = [tup for tup in datapoints if tup[0] != 0]

            # call generic graph method
            create_rep_widget(filtered_list, self.report_frame, "Fiber", 0)

            output_average(filtered_list, self.report_frame, meta_type, 0)
            self.report_frame.pack()

        def report_monthly_carbs():
            meta_type = "Carbohydrates"
            cleanup_rep_widget()
            create_reports_window_widget(meta_type, self.geometry)

            month = self.report_month
            year = self.report_year
            print("\n Reports / Monthly averages called \n")
            ids = database_driver.get_monthly_averages(month, year)
            datapoints = database_driver.get_daily_carb_totals(month, year, ids)
            filtered_list = [tup for tup in datapoints if tup[0] != 0]

            # call generic graph method
            create_rep_widget(filtered_list, self.report_frame, "Carbohydrates", 0)

            output_average(filtered_list, self.report_frame, meta_type, 0)
            self.report_frame.pack()

        def report_monthly_fat():
            meta_type = "Fat"
            cleanup_rep_widget()
            create_reports_window_widget(meta_type, self.geometry_full)

            month = self.report_month
            year = self.report_year
            print("\n Reports / Monthly averages called \n")
            ids = database_driver.get_monthly_averages(month, year)
            datapoints = database_driver.get_daily_fat_totals(month, year, ids)
            filtered_list = [tup for tup in datapoints if tup[0] != 0]

            # call generic graph method
            create_rep_widget(filtered_list, self.report_frame, "Fat", 0)

            output_average(filtered_list, self.report_frame, meta_type, 0)
            self.report_frame.pack()

        def report_monthly_hr():
            meta_type = "Fat"
            cleanup_rep_widget()
            create_reports_window_widget(meta_type, self.geometry_full)

            month = self.report_month
            year = self.report_year
            print("\n Reports / Monthly averages called \n")
            ids = database_driver.get_month_ids_hr(month, year, self.current_user)
            datapoints = database_driver.get_daily_hr_totals(month, year, ids)
            filtered_list = [tup for tup in datapoints if tup[0] != 0]
            print("heart rate filtered list : " +str(filtered_list))

            # call generic graph method
            create_rep_widget(filtered_list, self.report_frame, "Heart Rate", 0)

            output_average(filtered_list, self.report_frame, meta_type, 0)
            self.report_frame.pack()

        def report_monthly_bp():
            meta_type = "Fat"
            cleanup_rep_widget()
            create_reports_window_widget(meta_type, self.geometry_full)

            month = self.report_month
            year = self.report_year
            print("\n Reports / Monthly averages called \n")
            ids = database_driver.get_month_ids_bp(month, year, self.current_user)
            datapoints = database_driver.get_daily_bp_totals(month, year, ids)
            filtered_list = [tup for tup in datapoints if tup[0] != 0]

            # call generic graph method
            create_rep_widget(filtered_list, self.report_frame, "Blood Pressure", 0)

            output_average(filtered_list, self.report_frame, meta_type, 0)
            self.report_frame.pack()

        def report_monthly_full():
            meta_types = ['Calories', 'Protein', 'Fiber', 'Carbohydrates', 'Fat']
            cleanup_rep_widget()
            create_reports_window_widget("Complete", self.geometry)
            column_offset = 0

            for meta_type in meta_types:
                column_offset += 1
                print("column offset : " + str(column_offset))
                month = self.report_month
                year = self.report_year
                ids = database_driver.get_monthly_averages(month, year)
                datapoints = database_driver.get_daily_calorie_totals(month, year, ids)
                filtered_list = [tup for tup in datapoints if tup[0] != 0]

                # call generic graph method
                create_rep_widget(filtered_list, self.report_frame, meta_type, column_offset)

                output_average(filtered_list, self.report_frame, meta_type, column_offset)
            self.report_frame.pack()

        # Config
        config = ConfigParser()
        script_dir = os.path.dirname(os.path.abspath(__file__))
        config_file_path = os.path.join(script_dir, "..", "settings.ini")
        config.read(config_file_path)

        self.debug = config.get('main-section', 'debug_level', fallback=None)
        self.protein_threshold = int(config.get('main-section', 'protein_threshold', fallback=None))
        self.fiber_threshold = int(config.get('main-section', 'fiber_threshold', fallback=None))
        self.carbs_threshold = int(config.get('main-section', 'carbs_threshold', fallback=None))
        self.rdn = int(config.get('main-section', 'default_days_size', fallback=None))

        if int(self.debug) == 1:
            self.current_user = 1

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
