import sqlite3

def init():

    sql_statements = [
        """CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY, 
                user_name text NOT NULL,
                email text NOT NULL,
                password TEXT NOT NULL
            );""",

        """CREATE TABLE IF NOT EXISTS days (
                id INTEGER PRIMARY KEY, 
                name text NOT NULL, 
                user_id INTEGER NOT NULL, 
                actual_date DATE, 
                FOREIGN KEY (user_id) REFERENCES user (id)
            );""",

        """CREATE TABLE IF NOT EXISTS foodstuffs (
                id INTEGER PRIMARY KEY, 
                description TEXT NOT NULL,
                serving TEXT NOT NULL, 
                calories INT, 
                protein INT NOT NULL, 
                carbs INT NOT NULL, 
                fiber INT NOT NULL,
                fat INT NOT NULL
            );"""
    ]

    # create a database connection
    try:
        with sqlite3.connect('../data/fast-tracker.db') as conn:
            # create a cursor
            cursor = conn.cursor()

            # execute statements
            for statement in sql_statements:
                cursor.execute(statement)

            # commit the changes
            conn.commit()

            print("Tables created successfully.")
    except sqlite3.OperationalError as e:
        print("Failed to create tables:", e)

def create_user():

    # create a database connection
    try:
        with sqlite3.connect('../data/fast-tracker.db') as conn:
            # create a cursor
            cursor = conn.cursor()

            users_data = [
                (1, 'Test_user', 'test_user@example.com', 'test_password'),
            ]
            cursor.executemany("INSERT INTO users (id, user_name, email, password) VALUES (?, ?, ?, ?)", users_data)

            # commit the changes
            conn.commit()

            print("USER table updated successfully.")
    except sqlite3.OperationalError as e:
        print("Failed to update user table:", e)