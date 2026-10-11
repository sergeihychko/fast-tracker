import sqlite3
import ftdataclasses

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
                entry1 text,
                entry2 text,
                entry3 text,
                entry4 text,
                entry5 text,
                entry6 text,
                entry7 text,
                entry8 text,
                entry9 text,
                entry10 text,
                entry11 text,
                entry12 text,
                FOREIGN KEY (entry1) REFERENCES foodstuffs (id),
                FOREIGN KEY (entry2) REFERENCES foodstuffs (id),
                FOREIGN KEY (entry3) REFERENCES foodstuffs (id),
                FOREIGN KEY (entry4) REFERENCES foodstuffs (id),
                FOREIGN KEY (entry5) REFERENCES foodstuffs (id),
                FOREIGN KEY (entry6) REFERENCES foodstuffs (id),
                FOREIGN KEY (entry7) REFERENCES foodstuffs (id),
                FOREIGN KEY (entry8) REFERENCES foodstuffs (id),
                FOREIGN KEY (entry9) REFERENCES foodstuffs (id),
                FOREIGN KEY (entry10) REFERENCES foodstuffs (id),
                FOREIGN KEY (entry11) REFERENCES foodstuffs (id),
                FOREIGN KEY (entry12) REFERENCES foodstuffs (id),
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

def create_test_days():

    # create a database connection
    try:
        with sqlite3.connect('../data/fast-tracker.db') as conn:
            # create a cursor
            cursor = conn.cursor()

            days_data = [
                (1, 'Saturday', 1, '2026-10-10', 1 ,2 ,3, 4, 5, 6, 0),
                (2, 'Sunday', 1, '2026-10-11', 1 , 2, 7, 8, 9, 0, 0)
            ]
            foodstuffs_data = [
                (1, 'Wheat Bagel', 1, 220, 10, 45, 6, 2),
                (2, 'Light cream cheese', 1, 60, 2, 2, 0 ,5),
                (3, 'Lentil Roasted Veg soup', 1, 180, 13, 42, 15, 1),
                (4, 'Catfish fillet', 1, 150, 17, 0, 0, 7),
                (5, 'brown rice 1cup', 1, 220, 4, 41, 2, 5),
                (6, 'Brussel sprouts', 1, 180, 12, 32, 12, 0),
                (7, 'fiberone soft 2 pack', 1, 140, 4, 34, 12, 6),
                (8, 'wheat thins crackers', 1, 140, 2, 23, 2, 5),
                (9, 'Progresso Chicken Noodle', 1, 130, 11, 19, 2, 3)
            ]
            cursor.executemany("INSERT INTO days (id, name, user_id, actual_date, entry1, entry2, entry3, entry4, entry5, entry6, entry7) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", days_data)
            cursor.executemany("INSERT INTO foodstuffs (id, description, serving, calories, protein, carbs, fiber, fat) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", foodstuffs_data)

            # commit the changes
            conn.commit()

            print("DAYS and FOODSTUFFS table updated successfully.")
    except sqlite3.OperationalError as e:
        print("Failed to update days table:", e)

def check_login(username, password):

            # create a database connection
            try:
                with sqlite3.connect('../data/fast-tracker.db') as conn:
                    # create a cursor
                    cursor = conn.cursor()
                    userid = 0

                    # Parameterized query using ? placeholder
                    cursor.execute("SELECT id, user_name, password FROM users WHERE user_name = ? AND password = ?", (username, password))
                    row = cursor.fetchone()
                    if row:
                        userid = row[0]
                        print("Found row:", row)

                    # close connection
                    #conn.close()

                    return userid

            except sqlite3.OperationalError as e:
                print("Error finding user:", e)


def get_user_data(user_id):
    # create a database connection
    try:
        with sqlite3.connect('../data/fast-tracker.db') as conn:
            # create a cursor
            cursor = conn.cursor()

            # Parameterized query using ? placeholder
            cursor.execute("SELECT * FROM days WHERE days.user_id = ?", (user_id, ))
            rows = cursor.fetchall()
            if rows:
                print("Found rows:", rows)
                return rows

    except sqlite3.OperationalError as e:
        print("Error finding user:", e)


def get_days_detail(day_id, user_id):
    # create a database connection
    try:
        with sqlite3.connect('../data/fast-tracker.db') as conn:
            # create a cursor
            cursor = conn.cursor()

            # Parameterized query using ? placeholder
            query_statement = """
                SELECT f.id, f.description, f.serving, f.calories, f.protein, f.carbs, f.fiber, f.fat            
                FROM foodstuffs f, days d
                WHERE f.id IN(d.entry1, d.entry2, d.entry3, d.entry4, d.entry5, d.entry6, d.entry7) AND d.id = ?;
            """
            #                INNER JOIN days d ON d.id = ? AND d.entry1 = f.id;
            print("query : " + query_statement)
            print("day_id : " + str(day_id) + " : user_id : " + str(user_id))
            #cursor.execute("SELECT * FROM foodstuffs WHERE days.user_id = ? AND days.id = ?", (user_id, day_id))
            cursor.execute(query_statement, str(day_id))

            rows = cursor.fetchall()
            if rows:
                print("Found rows:", rows)
                # Populate Dataclass instances
                #entries = [ftdataclasses.Foodstuff(*row) for row in rows]
                entries = rows
                return entries
            else:
                print("No rows returned for day_id : " + str(day_id))

    except sqlite3.OperationalError as e:
        print("Error finding foodstuffs for day entry:", e)