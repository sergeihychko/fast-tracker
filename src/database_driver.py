import sqlite3
import ftdataclasses
import numpy as np

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
                (15, 'Saturday', 1, '2026-10-24', 36, 37, 0, 0, 0),
                (16, 'Sunday', 1, '2026-10-25', 38, 39, 0, 0, 0),
                (17, 'Monday', 1, '2026-10-26', 0, 0, 0, 0, 0),
                (18, 'Tuesday', 1, '2026-10-27', 40, 41, 0, 0, 0),
                (19, 'Wednesday', 1, '2026-10-28', 43, 0, 0, 0, 0),
                (20, 'Thursday', 1, '2026-10-29', 44, 45, 46, 0, 0),
                (21, 'Friday', 1, '2026-10-30', 47, 48, 0, 0, 0),
                (22, 'Saturday', 1, '2026-10-31', 49, 50, 0, 0, 0),
                (23, 'Sunday', 1, '2026-11-01', 51, 0, 0, 0, 0),
                (24, 'Monday', 1, '2026-11-02', 52, 53, 0, 0, 0),
                (25, 'Tuesday', 1, '2026-11-03', 54, 0, 0, 0, 0),
                (26, 'Wednesday', 1, '2026-11-04', 55, 0, 0, 0, 0),
                (27, 'Thursday', 1, '2026-11-05', 56, 0, 0, 0, 0),
                (28, 'Friday', 1, '2026-11-06', 0, 0, 0, 0, 0),
                (29, 'Saturday', 1, '2026-11-07', 57, 58, 0, 0, 0),
                (30, 'Sunday', 1, '2026-11-08', 60, 59, 61, 0, 0),
                (31, 'Monday', 1, '2026-11-09', 62, 63, 0, 0, 0),
                (32, 'Tuesday', 1, '2026-11-10', 64, 65, 66, 0, 0),
                (33, 'Wednesday', 1, '2026-11-11', 67, 68, 0, 0, 0),
                (34, 'Thursday', 1, '2026-11-12', 69, 70, 0, 0, 0),
                (35, 'Friday', 1, '2026-11-13', 71, 72, 0, 0, 0),
                (36, 'Saturday', 1, '2026-11-14', 73, 74, 0, 0, 0),
                (37, 'Sunday', 1, '2026-11-15', 0, 0, 0, 0, 0),
                (38, 'Monday', 1, '2026-11-16', 75, 76, 0, 0, 0),
                (39, 'Tuesday', 1, '2026-11-17', 77, 78, 79, 0, 0),
                (40, 'Wednesday', 1, '2026-11-18', 80, 81, 0, 0, 0),
                (41, 'Thursday', 1, '2026-11-19', 82, 83, 0, 0, 0),
                (42, 'Friday', 1, '2026-11-20', 84, 85, 0, 0, 0),
                (43, 'Saturday', 1, '2026-11-21', 86, 87, 0, 0, 0),
                (44, 'Sunday', 1, '2026-11-22', 88, 0, 0, 0, 0),
                (45, 'Monday', 1, '2026-11-23', 89, 90, 0, 0, 0),
                (46, 'Tuesday', 1, '2026-11-24', 91, 92, 0, 0, 0),
                (47, 'Wedesday', 1, '2026-11-25', 0, 0, 0, 0, 0)
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
                (35, 36),
                (36, 32),
                (37, 34),
                (37, 26),
                (37, 35),
                (37, 26),
                (37, 5),
                (37, 24),
                (38,37 ),
                (38, 5),
                (39, 19),
                (39, 22),
                (39, 20),
                (39, 38),
                (40, 39),
                (41, 40),
                (41, 20),
                (41, 20),
                (42, 21),
                (43, 6),
                (43, 41),
                (44, 42),
                (44, 42),
                (44, 42),
                (44, 36),
                (45, 9),
                (45, 37),
                (45, 10),
                (45, 5),
                (46, 43),
                (46, 43),
                (47, 44),
                (48, 40),
                (48, 20),
                (48, 37),
                (48, 37),
                (49, 43),
                (49, 42),
                (49, 42),
                (49, 42),
                (50, 9),
                (50, 19),
                (50, 22),
                (51, 43),
                (51, 43),
                (51, 3),
                (51, 45),
                (51, 41),
                (52, 43),
                (53, 47),
                (53, 46),
                (53, 46),
                (53, 46),
                (53, 46),
                (53, 46),
                (54, 47),
                (54, 48),
                (54, 49),
                (55, 50),
                (55, 51),
                (56, 48),
                (56, 48),
                (56, 43),
                (57, 52),
                (57, 53),
                (57, 7),
                (57, 52),
                (58, 54),
                (58, 55),
                (58, 52),
                (58, 56),
                (58, 57),
                (59, 1),
                (59, 58),
                (59, 59),
                (59, 56),
                (59, 57),
                (60, 54),
                (60, 55),
                (60, 52),
                (61, 60),
                (61, 61),
                (61, 61),
                (62, 54),
                (62, 55),
                (62, 62),
                (63, 56),
                (63, 57),
                (63, 63),
                (63, 64),
                (63, 1),
                (63, 58),
                (63, 59),
                (63, 7),
                (64, 54),
                (64, 55),
                (64, 65),
                (65, 1),
                (65, 58),
                (65, 59),
                (65, 34),
                (65, 61),
                (65, 7),
                (66, 66),
                (66, 10),
                (66, 67),
                (67, 68),
                (67, 55),
                (67, 62),
                (68, 70),
                (68, 70),
                (68, 71),
                (68, 72),
                (68, 20),
                (68, 7),
                (68, 73),
                (69, 69),
                (69, 69),
                (69, 58),
                (69, 59),
                (69, 54),
                (69, 55),
                (69, 74),
                (69, 74),
                (69, 74),
                (69, 74),
                (70, 70),
                (70, 70),
                (70, 71),
                (70, 72),
                (70, 7),
                (71, 55),
                (71, 68),
                (72, 69),
                (72, 69),
                (72, 58),
                (72, 58),
                (72, 63),
                (72, 45),
                (72, 61),
                (72, 74),
                (72, 74),
                (72, 74),
                (72, 74),
                (72, 7),
                (72, 62),
                (73, 54),
                (73, 55),
                (73, 7),
                (74, 75),
                (74, 76),
                (74, 77),
                (74, 61),
                (74, 63),
                (74, 70),
                (74, 70),
                (74, 20),
                (74, 20),
                (75, 7),
                (75, 14),
                (75, 14),
                (75, 56),
                (75, 57),
                (76, 5),
                (76, 67),
                (77, 54),
                (77, 54),
                (77, 55),
                (77, 55),
                (77, 7),
                (78, 67),
                (78, 5),
                (78, 10),
                (79, 56),
                (79, 57),
                (79, 19),
                (80, 69),
                (80, 69),
                (80, 43),
                (80, 7),
                (81, 56),
                (81, 57),
                (81, 68),
                (81, 78),
                (81, 69),
                (81, 69),
                (81, 63),
                (82, 7),
                (82, 54),
                (82, 79),
                (83, 70),
                (83, 70),
                (83, 80),
                (83, 63),
                (83, 39),
                (83, 81),
                (83, 75),
                (83, 67),
                (84, 54),
                (84, 54),
                (84, 78),
                (84, 7),
                (85, 5),
                (85, 76),
                (85, 3),
                (86, 68),
                (86, 68),
                (86, 78),
                (86, 7),
                (86, 69),
                (86, 69),
                (86, 80),
                (86, 63),
                (86, 34),
                (86, 61),
                (87, 69),
                (87, 69),
                (87, 69),
                (87, 2),
                (87, 43),
                (87, 82),
                (88, 54),
                (88, 79),
                (88, 7),
                (88, 69),
                (88, 69),
                (88, 63),
                (88, 83),
                (88, 26),
                (88, 5),
                (89, 68),
                (89, 84),
                (89, 86),
                (89, 7),
                (90, 75),
                (90, 37),
                (90, 37),
                (90, 10),
                (90, 6),
                (90, 61),
                (90, 65),
                (91, 87),
                (91, 68),
                (91, 86),
                (92, 70),
                (92, 70),
                (92, 63),
                (92, 81),
                (92, 80),
                (92, 39),
                (92, 7)
            ]
            foodstuffs_data = [
                (1, 'Wheat Bagel', 1, 220, 45, 10, 6, 2),
                (2, 'Light cream cheese', 1, 60, 2, 2, 0 ,5),
                (3, 'Lentil Roasted Veg soup', 1, 180, 42, 13, 15, 1),
                (4, 'Catfish fillet', 1, 150, 0, 17, 0, 7),
                (5, 'brown rice 1cup', 1, 220, 4, 41, 2, 5),
                (6, 'Brussel sprouts', 1, 180, 32, 12, 12, 0),
                (7, 'fiberone soft 2 pack', 1, 140, 34, 4, 14, 6),
                (8, 'wheat thins crackers', 1, 140, 2, 23, 2, 5),
                (9, 'Progresso Chicken Noodle', 1, 130, 11, 19, 2, 3),
                (10, 'Teriyaki sauce', 1, 50, 10, 2, 0, 0),
                (11, 'Tilapia fillet', 1, 220, 46, 0, 0, 4),
                (12, 'cottage cheese 4%', 1, 110, 13, 5, 0, 5),
                (13, 'fruit mix', 1, 40, 13, 1, 3, 0),
                (14, 'banana', 1, 121, 31, 1, 4, 0),
                (15, 'maple bourbon salad', 1, 525, 35, 10, 7, 42),
                (16, 'light breaded chicken', 1, 210, 14, 22, 0, 8),
                (17, 'wheat roll', 1, 120, 25, 6, 4, 1),
                (18, 'Ham black forest 2oz', 1, 60, 1, 9, 0, 2),
                (19, 'baked potato large', 1, 278, 63, 7, 7, 0),
                (20, 'sharp cheddar 1oz', 1, 110, 2, 6, 0, 9),
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
                (35, 'Honey Hot Sauce mango 1tsp', 1, 10, 2, 0, 0, 0),
                (36, 'Raspberries', 1, 80, 18, 2, 6, 1),
                (37, 'Shrimp 4oz', 1, 80, 1, 15, 0, 1),
                (38, 'Channa Masala organic', 1, 330, 44, 12, 17, 12),
                (39, 'Corn frozen', 1, 90, 19, 3, 2, 0),
                (40, 'Plant based chili with beans', 1, 290, 45, 22, 10, 2),
                (41, '1tbsp butter', 1, 100, 0, 0, 0, 11),
                (42, 'instant quaker oatmeal fruit and cream', 1, 110, 23, 3, 2, 2),
                (43, 'Creamy Natural Peanut Butter Spread', 1, 190, 8, 7, 2, 15),
                (44, '1/2 serving Peanut Butter Spread', 1, 95, 4, 3, 1, 7),
                (45, 'california mix 12 oz', 1, 120, 20, 8, 8, 0),
                (46, 'Stouffers Mac n cheese', 1, 310, 34, 13, 1, 14),
                (47, 'Beefaroni 15oz', 1, 350, 48, 10, 2, 13),
                (48, 'Ravioli 15oz', 1, 320, 52, 9, 2, 8),
                (49, 'Beef with veg soup', 1, 220, 37, 12, 7, 3),
                (50, 'Philly cheesesteak', 1, 1146, 84, 65, 6, 61),
                (51, 'cheese fries', 1, 610, 91, 9, 4, 23),
                (52, 'banana small', 1, 90, 23, 1, 3, 0),
                (53, 'Kodiak Muffin blueberry', 1, 260, 40, 12, 4, 6),
                (54, 'cottage cheese low fat', 1, 90, 5, 13, 0, 2),
                (55, 'strawberies sliced 1/2 serving', 1, 25, 6, 0, 1, 0),
                (56, 'pasta sauce spicy vodka', 1, 110, 11, 2, 2, 6),
                (57, 'cheese tortelini', 1, 250, 43, 9, 2, 5),
                (58, 'horseradish sauce 1tsb', 1, 20, 0, 0, 0, 2),
                (59, 'ham ', 1, 70, 4, 9, 0, 2),
                (60, 'cauliflower 12oz', 1, 120, 16, 4, 8, 0),
                (61, 'nacho cheese sauce', 1, 50, 5, 1, 0, 3),
                (62, 'Pure protein bar', 1, 180, 20, 20, 0, 3),
                (63, 'Chicken Breast Strips 4oz', 1, 125, 1, 25, 0, 3),
                (64, 'quinoa, brown rice, garlic 1/2 packet', 1, 220, 42, 4, 4, 4),
                (65, 'Probiotic Blueberry FruiChias', 1, 60, 19, 0, 3, 0),
                (66, 'Muscle Milk Strawberry', 1, 270, 21, 32, 6, 9),
                (67, 'Catfish 4 oz amazon', 1, 130, 0, 17, 0, 7),
                (68, 'Greek Yogurt, Plain Nonfat', 1, 100, 6, 17, 0, 0),
                (69, 'Oroweat Multi Grain Bread', 1, 110, 19, 4, 4, 2),
                (70, 'Soft Taco Whole Wheat Tortillas', 1, 110, 22, 4, 5, 2),
                (71, 'corn 1 serving', 1, 90, 19, 3, 2 ,0),
                (72, 'black beans', 1, 110, 21, 7, 5, 0),
                (73, 'peas 12 oz', 1, 280, 28, 16, 16, 0),
                (74, 'planters peanuts', 1, 170, 9, 6, 2, 12),
                (75, 'quinoa, brown and red rice, 1/2 packet', 1, 200, 42, 4, 3, 4),
                (76, 'salmon atlantic 6oz', 1, 370, 0, 34, 0, 26),
                (77, 'green beans 12 oz', 1, 120, 24, 4, 8, 0),
                (78, 'cherries dark sweet 20', 1, 90, 22, 1, 3, 0),
                (79, 'cherries dark sweet 10', 1, 45, 11, 1,2,0),
                (80, 'Mexican-Style Four Cheese 1oz', 1, 110, 2, 6, 0, 8),
                (81, 'salsa fresh Amazon 4 tbs', 1, 10, 2, 0, 0, 0),
                (82, 'strawberry preservest 2 tbs', 1, 100, 26, 0, 0, 0),
                (83, 'Pataks Tikka Masala All Purpose Sauce',1, 40, 5, 1, 1, 2),
                (84, 'Flax and Chia Seed Blend 1.5 tbsp', 1, 70, 4, 3, 3, 4),
                (85, 'Triple Berry Mix, 1.25 cups', 1, 80, 18, 1, 5, 1),
                (86, 'Triple Berry Mix, 1/2 serving', 1, 40, 9, 0, 3, 0),
                (87, 'Buldak Spicy Instant Ramen Noodles', 1, 530, 85, 12, 4, 16),
                (88, 'Quinoa boil in bag whole', 1, 310, 48, 12, 9, 6)
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

def get_user_data(user_id, limit):
    # create a database connection
    try:
        with sqlite3.connect('../data/fast-tracker.db') as conn:
            # create a cursor
            cursor = conn.cursor()

            # Parameterized query using ? placeholder
            cursor.execute("SELECT * FROM days WHERE days.user_id = ? ORDER BY id DESC LIMIT ?", (user_id, limit))
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
                SELECT f.description, f.serving, f.calories, f.carbs, f.protein, f.fiber, f.fat, d.id         
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
            #query = f"SELECT * FROM {table_name} WHERE id = (SELECT MAX(id) FROM {table_name})"
            query = f"SELECT MAX(id) FROM {table_name}"
            cursor.execute(query)
            max_id = cursor.fetchone()[0]

            if max_id is not None:
                next_id = max_id + 1
                print(f"Next sequential ID: {next_id}")
            else:
                next_id = 1  # Default if table is empty or has no autoincrement history
                print(f"Next sequential NOT FOUND for table {table_name}")
            return next_id
    except sqlite3.OperationalError as e:
        print("Error finding next ID sequence : " + str(e))

def get_month_ids(month, year):
    with sqlite3.connect('../data/fast-tracker.db') as conn:
        cursor = conn.cursor()
        query = """
            SELECT id 
            FROM days 
            WHERE CAST(strftime('%Y', actual_date) AS INTEGER) = ? 
            AND CAST(strftime('%m', actual_date) AS INTEGER) = ?
        """
        #print("query : " + str(query))
        cursor.execute(query, (year, month))
        ids = cursor.fetchall()
        return ids

def get_monthly_averages(month, year):
    ids = get_month_ids(month, year)
    print("IDs for the month : " + str(month) + " : " + str(ids))
    return ids

def get_daily_calorie_totals(month, year, ids):
    calories = []
    print("in stub get_daily_calorie_totals(month, year)")
    for id in ids:
        daily_c = get_daily_calories(id)
        calories.append(daily_c)
        #print(" : " + str(calories))
    print("complete list of days in ids array : " + str(calories))
    return calories

def get_daily_calories(day_id):
    val1 = str(day_id[0])
    day_total = 0
    with sqlite3.connect('../data/fast-tracker.db') as conn:
        cursor = conn.cursor()
        query_statement = """
            SELECT f.calories         
                FROM foodstuffs f
                INNER JOIN meals m ON m.id IN (d.meal1, d.meal2, d.meal3, d.meal4, d.meal5)
                INNER JOIN days d
                WHERE 
                    d.id = ? AND (f.id = m.foodstuff_id);
        """
        cursor.execute(query_statement, (val1, ))
        calories = cursor.fetchall()
        if len(calories) > 1:
            dt = np.array(calories)
            day_total = np.sum(dt)
        t = int(str(day_total))
        return [t, day_id[0]]

def get_daily_protein_totals(month, year, ids):
    protein = []
    print("in stub get_daily_protein_totals(month, year)")
    for id in ids:
        daily_p = get_daily_protein(id)
        protein.append(daily_p)
        #print(" : " + str(calories))
    print("complete list of days in ids array : " + str(protein))
    return protein

def get_daily_protein(day_id):
    val1 = str(day_id[0])
    day_total = 0
    print("in get_daily_protein() :" + str(day_id) + ":")
    calories = 0
    with sqlite3.connect('../data/fast-tracker.db') as conn:
        cursor = conn.cursor()
        query_statement = """
            SELECT f.protein         
                FROM foodstuffs f
                INNER JOIN meals m ON m.id IN (d.meal1, d.meal2, d.meal3, d.meal4, d.meal5)
                INNER JOIN days d
                WHERE 
                    d.id = ? AND (f.id = m.foodstuff_id);
        """
        cursor.execute(query_statement, (val1, ))
        protein = cursor.fetchall()
        if len(protein) > 1:
            dt = np.array(protein)
            day_total = np.sum(dt)
        t = int(str(day_total))
        return [t, day_id[0]]

def get_daily_fiber_totals(month, year, ids):
    fiber = []
    print("in stub get_daily_fiber_totals(month, year)")
    for id in ids:
        daily_f = get_daily_fiber(id)
        fiber.append(daily_f)
        #print(" : " + str(calories))
    print("complete list of days in ids array : " + str(fiber))
    return fiber

def get_daily_fiber(day_id):
    val1 = str(day_id[0])
    day_total = 0
    print("in get_daily_fiber() :" + str(day_id) + ":")
    with sqlite3.connect('../data/fast-tracker.db') as conn:
        cursor = conn.cursor()
        query_statement = """
            SELECT f.fiber         
                FROM foodstuffs f
                INNER JOIN meals m ON m.id IN (d.meal1, d.meal2, d.meal3, d.meal4, d.meal5)
                INNER JOIN days d
                WHERE 
                    d.id = ? AND (f.id = m.foodstuff_id);
        """
        cursor.execute(query_statement, (val1, ))
        fiber = cursor.fetchall()
        print("debug fiber array to be totalled : " + str(fiber))
        if len(fiber) > 1:
            dt = np.array(fiber)
            day_total = np.sum(dt)
        t = int(str(day_total))
        print("debug t = " + str(t))
        return [t, day_id[0]]

def get_daily_carb_totals(month, year, ids):
    carbs = []
    print("in stub get_daily_carb_totals(month, year)")
    for id in ids:
        daily_f = get_daily_carbs(id)
        carbs.append(daily_f)
        #print(" : " + str(calories))
    print("complete list of days in ids array : " + str(carbs))
    return carbs

def get_daily_carbs(day_id):
    val1 = str(day_id[0])
    print("in get_monthly_averages() :" + str(day_id) + ":")
    day_total = 0
    with sqlite3.connect('../data/fast-tracker.db') as conn:
        cursor = conn.cursor()
        query_statement = """
            SELECT f.carbs         
                FROM foodstuffs f
                INNER JOIN meals m ON m.id IN (d.meal1, d.meal2, d.meal3, d.meal4, d.meal5)
                INNER JOIN days d
                WHERE 
                    d.id = ? AND (f.id = m.foodstuff_id);
        """
        cursor.execute(query_statement, (val1, ))
        carbs = cursor.fetchall()
        if len(carbs) > 1:
            dt = np.array(carbs)
            day_total = np.sum(dt)
        t = int(str(day_total))
        return [t, day_id[0]]

def get_daily_fat_totals(month, year, ids):
    fat = []
    print("in stub get_daily_fat_totals(month, year)")
    for id in ids:
        daily_f = get_daily_fat(id)
        fat.append(daily_f)
        #print(" : " + str(calories))
    print("complete list of days in ids array : " + str(fat))
    return fat

def get_daily_fat(day_id):
    val1 = str(day_id[0])
    print("in get_monthly_averages() :" + str(day_id) + ":")
    day_total = 0
    with sqlite3.connect('../data/fast-tracker.db') as conn:
        cursor = conn.cursor()
        query_statement = """
            SELECT f.fat         
                FROM foodstuffs f
                INNER JOIN meals m ON m.id IN (d.meal1, d.meal2, d.meal3, d.meal4, d.meal5)
                INNER JOIN days d
                WHERE 
                    d.id = ? AND (f.id = m.foodstuff_id);
        """
        cursor.execute(query_statement, (val1, ))
        fat = cursor.fetchall()
        if len(fat) > 1:
            dt = np.array(fat)
            day_total = np.sum(dt)
        t = int(str(day_total))
        return [t, day_id[0]]

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

def find_foodstuff_by_partial(search_term):
    try:
        with sqlite3.connect('../data/fast-tracker.db') as conn:
            cursor = conn.cursor()

            # Query the foodstuffs table to find matches based on partial text input
            query = f"SELECT * from foodstuffs f WHERE UPPER(f.description) LIKE UPPER('%{search_term}%')"
            cursor.execute(query)
            rows = cursor.fetchall()
            if rows:
                entries = rows
                return entries
            else:
                print("No rows returned for foodstuff description : " + str(search_term))
    except sqlite3.OperationalError as e:
        print("Error finding next ID sequence : " + str(e))