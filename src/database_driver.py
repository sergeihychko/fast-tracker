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
                meal1 INT,
                meal2 INT,
                meal3 INT,
                meal4 INT,
                meal5 INT,
                FOREIGN KEY (meal1) REFERENCES foodstuffs (id),
                FOREIGN KEY (meal2) REFERENCES foodstuffs (id),
                FOREIGN KEY (meal3) REFERENCES foodstuffs (id),
                FOREIGN KEY (meal4) REFERENCES foodstuffs (id),
                FOREIGN KEY (meal5) REFERENCES foodstuffs (id),
                FOREIGN KEY (user_id) REFERENCES user (id)
            );""",

        """CREATE TABLE IF NOT EXISTS foodstuffs (
            id INTEGER PRIMARY KEY, 
            description TEXT NOT NULL,
            serving TEXT NOT NULL, 
            calories INT, 
            carbs INT NOT NULL, 
            protein INT NOT NULL, 
            fiber INT NOT NULL,
            fat INT NOT NULL
        );""",

        """CREATE TABLE IF NOT EXISTS meals (
            id INTEGER, 
            foodstuff_id text,
            FOREIGN KEY (foodstuff_id) REFERENCES foodstuffs (id)
        );""",
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
                (1, 'Saturday', 1, '2026-10-10', 1 ,2 ,3, 0, 0),
                (2, 'Sunday', 1, '2026-10-11', 4, 5, 6, 0, 0),
                (3, 'Monday', 1, '2026-10-12', 7, 8, 0, 0, 0),
                (4, 'Tuesday', 1, '2026-10-13', 0, 0, 0, 0, 0),
                (5, 'Wednesday', 1, '2026-10-14', 9, 10, 11, 0, 0),
                (6, 'Thursday', 1, '2026-10-15', 12, 13, 14, 0, 0),
                (7, 'Friday', 1, '2026-10-16', 15, 16, 0, 0, 0),
                (8, 'Saturday', 1, '2026-10-17', 17, 18, 19, 20, 0),
                (9, 'Sunday', 1, '2026-10-18', 21, 22, 23, 0, 0),
                (10, 'Monday', 1, '2026-10-19', 24, 25, 26, 0, 0),
                (11, 'Tuesday', 1, '2026-10-20', 27, 28, 29, 0, 0),
                (12, 'Wednesday', 1, '2026-10-21', 30, 31, 0, 0, 0),
                (13, 'Thursday', 1, '2026-10-22', 32, 33, 0, 0, 0),
                (14, 'Friday', 1, '2026-10-23', 34, 35, 0, 0, 0),
                (15, 'Saturday', 1, '2026-10-24', 36, 37, 0, 0, 0)
            ]
            meals_data = [
                (1, 1),
                (1, 2),
                (2, 3),
                (3, 4),
                (3, 5),
                (3, 6),
                (4, 1),
                (4, 2),
                (5, 7),
                (5, 8),
                (5, 9),
                (6, 4),
                (6, 6),
                (7, 9),
                (7, 10),
                (7, 11),
                (8, 7),
                (9, 12),
                (9, 13),
                (9, 14),
                (10, 18),
                (10, 18),
                (10, 16),
                (10, 17),
                (11, 19),
                (11, 20),
                (12, 12),
                (12, 13),
                (12, 14),
                (13, 16),
                (13, 17),
                (13, 16),
                (13, 17),
                (14, 18),
                (14, 18),
                (15, 12),
                (15, 13),
                (16, 15),
                (16, 16),
                (16, 17),
                (17, 12),
                (17, 13),
                (18, 16),
                (18, 17),
                (19, 21),
                (19, 19),
                (20, 22),
                (20, 23),
                (20, 24),
                (21, 1),
                (21, 2),
                (22, 23),
                (22, 24),
                (23, 9),
                (23, 12),
                (24, 25),
                (25, 26),
                (25, 27),
                (26, 24),
                (26, 28),
                (27, 12),
                (28, 24),
                (28, 3),
                (29, 17),
                (29, 29),
                (29, 12),
                (30, 25),
                (30, 24),
                (30, 30),
                (31, 6),
                (31, 4),
                (32, 12),
                (32, 24),
                (33, 31),
                (33, 32),
                (33, 32),
                (34, 32),
                (34, 33),
                (34, 35),
                (35, 26),
                (35, 5),
                (35, 32),
                (36, 32),
                (37, 34),
                (37, 26),
                (37, 35),
                (37, 26),
                (37, 5)
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
                (9, 'Progresso Chicken Noodle', 1, 130, 11, 19, 2, 3),
                (10, 'Teriyaki sauce', 1, 50, 2, 10, 0, 0),
                (11, 'Tilapia fillet', 1, 220, 46, 0, 0, 4),
                (12, 'cottage cheese 4%', 1, 110, 13, 5, 0, 5),
                (13, 'fruit mix', 1, 40, 1, 13, 3, 0),
                (14, 'banana', 1, 121, 1, 31, 4, 0),
                (15, 'maple bourbon salad', 1, 525, 35, 10, 7, 42),
                (16, 'light breaded chicken', 1, 210, 14, 22, 0, 8),
                (17, 'wheat roll', 1, 120, 25, 6, 4, 1),
                (18, 'Ham black forest 2oz', 1, 60, 1, 9, 0, 2),
                (19, 'baked potato large', 1, 278, 63, 7, 7, 0),
                (20, 'sharp cheddar 10z', 1, 110, 2, 6, 0, 9),
                (21, 'Chicken Noodle Campbell Healthy', 1, 240, 27, 16, 3, 7),
                (22, 'sour cream light', 1, 40, 1, 3, 0, 3),
                (23, 'quinoa & spinach', 1, 340, 58, 9, 8, 8),
                (24, 'burrito chick, carb balance', 1, 400, 25, 20, 25, 3),
                (25, 'greek yogurt nonfat 365', 1, 120, 17, 12, 0, 0),
                (26, 'chicken breast chunks', 1, 120, 2, 22, 0, 3),
                (27, 'brown rice & quinoa', 1, 220, 42, 4, 4, 4),
                (28, 'split pea progresso', 1, 270, 51, 18, 8, 2),
                (29, 'albacore plus light mayo', 1, 140, 4, 22, 0, 4),
                (30, 'Progresso brocolli cheese', 1, 230, 21, 9, 2, 12),
                (31, 'Momofuku Spicy Soy Ramen', 1, 320, 63, 11, 2, 1),
                (32, 'vanilla greek yogurt', 1, 140, 19, 15, 0, 0),
                (33, 'Chicken Noodle Amazon - traditional', 1, 200, 25, 13, 3, 5),
                (34, 'Broccoli Florets 12 Oz', 1 , 120, 16, 4, 8, 0),
                (35, 'Honey Hot Sauce mango 1tsp', 1, 10, 2, 0, 0, 0)
            ]

            cursor.executemany("INSERT INTO days (id, name, user_id, actual_date, meal1, meal2, meal3, meal4, meal5) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", days_data)
            cursor.executemany("INSERT INTO meals (id, foodstuff_id) VALUES (?, ?)", meals_data)
            cursor.executemany("INSERT INTO foodstuffs (id, description, serving, calories, carbs, protein, fiber, fat) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", foodstuffs_data)

            # commit the changes
            conn.commit()

            print("DAYS, MEALS and FOODSTUFFS table updated successfully.")
    except sqlite3.OperationalError as e:
        print("Failed to update days, meals and foodstuffs table:", e)

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

                    return userid

            except sqlite3.OperationalError as e:
                print("Error finding user:", e)

def get_day_entry(day_id):
    # create a database connection
    val1 = str(day_id)
    try:
        with sqlite3.connect('../data/fast-tracker.db') as conn:
            # create a cursor
            cursor = conn.cursor()

            # Parameterized query using ? placeholder
            cursor.execute("SELECT * FROM days WHERE days.id = ?", (val1, ))
            rows = cursor.fetchone()
            if rows:
                #print("get_day_entry : " + str(rows))
                return rows

    except sqlite3.OperationalError as e:
        print("Error finding day data : ", e)

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
                #print("Found rows:", rows)
                return rows

    except sqlite3.OperationalError as e:
        print("Error finding user:", e)


def get_days_detail(day_id):
    # create a database connection
    val1 = str(day_id)
    try:
        with sqlite3.connect('../data/fast-tracker.db') as conn:
            # create a cursor
            cursor = conn.cursor()

            # Parameterized query using ? placeholder
            query_statement = """
                SELECT f.description, f.serving, f.calories, f.protein, f.carbs, f.fiber, f.fat, d.id         
                FROM foodstuffs f
                INNER JOIN meals m ON m.id IN (d.meal1, d.meal2, d.meal3, d.meal4, d.meal5)
                INNER JOIN days d
                WHERE 
                    d.id = ? AND (f.id = m.foodstuff_id);
            """
            print("calling cursor with : " + str(val1))
            cursor.execute(query_statement, (val1, ))

            rows = cursor.fetchall()
            if rows:
                #print("get_days_detail:", rows)
                # Populate Dataclass instances
                #entries = [ftdataclasses.Foodstuff(*row) for row in rows]
                entries = rows
                return entries
            else:
                print("No rows returned for day_id : " + str(day_id))

    except sqlite3.OperationalError as e:
        print("Error finding foodstuffs for day entry:", e)

def find_next_id(table_name):
    try:
        with sqlite3.connect('../data/fast-tracker.db') as conn:
            cursor = conn.cursor()

            # Query the table to find the last used ID
            #cursor.execute("SELECT * FROM ? ORDER BY id DESC LIMIT 1;", (table_name, ))
            query = f"SELECT * FROM {table_name} WHERE id = (SELECT MAX(id) FROM {table_name})"
            cursor.execute(query)
            highest_id = cursor.fetchone()[0]
            result = cursor.fetchone()

            if result and result[0] is not None:
                next_id = result[0] + 1
            else:
                next_id = 1  # Default if table is empty or has no autoincrement history
            print(f"Next sequential ID: {next_id}")
            return next_id
    except sqlite3.OperationalError as e:
        print("Error finding next ID sequence : " + str(e))

def insert_meal(meal):
    try:
        with sqlite3.connect('../data/fast-tracker.db') as conn:
            cursor = conn.cursor()

            # Insert single row
            cursor.execute(
                "INSERT INTO meals (id, foodstuff_id) VALUES (?, ?)",
                (meal.id, meal.foodstuff_id),
            )
            conn.commit()
            cursor.close()
            #conn.close()
            print(f"Inserted Meal ID: {meal.id}")
    except sqlite3.OperationalError as e:
        print("Error inserting into Meals table")

def insert_foodstuff(foodstuff):
    try:
        with sqlite3.connect('../data/fast-tracker.db') as conn:
            cursor = conn.cursor()

            # Insert single row
            cursor.execute(
                "INSERT INTO foodstuffs (id, description, serving, calories, carbs, protein, fiber, fat) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (foodstuff.id, foodstuff.description, foodstuff.serving_size, foodstuff.calories, foodstuff.carbs, foodstuff.protein, foodstuff.fiber, foodstuff.fat),
            )
            conn.commit()
            cursor.close()
            #conn.close()
            print(f"Inserted Meal ID: {foodstuff.id}")
    except sqlite3.OperationalError as e:
        print("Error inserting into Foodstuffs table")
