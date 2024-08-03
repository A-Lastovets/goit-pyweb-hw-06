-- Знайти оцінки студентів у окремій групі з певного предмета
SELECT students.first_name, students.last_name, grades.grade, subjects.subject_name
FROM students, subjects
JOIN grades ON students.student_id = grades.student_id
WHERE students.group_id = 1 AND grades.subject_id = 2;