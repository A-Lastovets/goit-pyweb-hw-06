-- Знайти середній бал, який ставить певний викладач зі своїх предметів
SELECT AVG(grades.grade) as avg_grade, subject_name, name
FROM grades, teachers
JOIN subjects ON grades.subject_id = subjects.subject_id
WHERE teachers.teacher_id = 6;