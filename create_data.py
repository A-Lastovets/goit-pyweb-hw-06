import sqlite3
from faker import Faker
import random
from datetime import datetime, timedelta

def create_data():
    try:
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()

        fake = Faker()

        # Заповнення таблиці groups
        groups = ['Group A', 'Group B', 'Group C']
        for group in groups:
            cursor.execute('INSERT INTO groups (group_name) VALUES (?)', (group,))

        # Заповнення таблиці teachers
        for _ in range(4):
            cursor.execute('INSERT INTO teachers (first_name, last_name) VALUES (?, ?)', (fake.first_name(), fake.last_name()))

        # Заповнення таблиці subjects
        subject_names = ['Mathematics', 'Physics', 'Chemistry', 'Biology', 'History', 'Geography', 'Literature']
        for subject_name in subject_names:
            cursor.execute('INSERT INTO subjects (subject_name, teacher_id) VALUES (?, ?)', (subject_name, random.randint(1, 4)))

        # Заповнення таблиці students
        for _ in range(40):
            cursor.execute('INSERT INTO students (first_name, last_name, group_id) VALUES (?, ?, ?)', 
                    (fake.first_name(), fake.last_name(), random.randint(1, 3)))

        # Заповнення таблиці grades
        start_date = datetime.now() - timedelta(days=365)
        end_date = datetime.now()

        for student_id in range(1, 41):
            for subject_id in range(1, 8):
                for _ in range(20):
                    date_received = fake.date_between(start_date=start_date, end_date=end_date)
                    grade = random.randint(2, 5)
                    cursor.execute('INSERT INTO grades (student_id, subject_id, grade, date_received) VALUES (?, ?, ?, ?)',
                        (student_id, subject_id, grade, date_received))

        conn.commit()

    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()