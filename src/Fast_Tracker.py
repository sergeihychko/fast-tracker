import os
import tkinter as tk
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

#tk._test()
root = tk.Tk()
root.title("Fast Tracker")

root.mainloop()



