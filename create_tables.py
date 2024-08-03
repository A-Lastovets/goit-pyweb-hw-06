import sqlite3

def create_tables():
    try:
        # Підключення до бази даних (створення файлу бази даних)
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()

        # Створення таблиць
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            group_id INTEGER,
            FOREIGN KEY (group_id) REFERENCES groups (group_id)
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS groups (
            group_id INTEGER PRIMARY KEY,
            group_name TEXT NOT NULL
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS teachers (
            teacher_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            subject_id INTEGER,
            FOREIGN KEY (subject_id) REFERENCES subjects (subject_id)
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS subjects (
            subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject_name TEXT NOT NULL,
            teacher_id INTEGER
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS grades (
            grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            subject_id INTEGER,
            teacher_id INTEGER,
            grade INTEGER,
            date_received DATE NOT NULL,
            FOREIGN KEY (student_id) REFERENCES students (student_id),
            FOREIGN KEY (subject_id) REFERENCES subjects (subject_id),
            FOREIGN KEY (teacher_id) REFERENCES teachers (teacher_id)
        )
        ''')

        conn.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()