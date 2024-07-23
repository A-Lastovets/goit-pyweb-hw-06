import sqlite3

def create_tables():
    try:
        # Підключення до бази даних (створення файлу бази даних)
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()

        # Створення таблиць
        cursor.execute('''
        CREATE TABLE students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            group_id INTEGER
        )
        ''')

        cursor.execute('''
        CREATE TABLE groups (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            group_name TEXT
        )
        ''')

        cursor.execute('''
        REATE TABLE teachers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT
        )
        ''')

        cursor.execute('''
        CREATE TABLE subjects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject_name TEXT,
            teacher_id INTEGER
        )
        ''')

        cursor.execute('''
        CREATE TABLE grades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            subject_id INTEGER,
            grade INTEGER,
            date_received DATE
        )
        ''')

        conn.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()