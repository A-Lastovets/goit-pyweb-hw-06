-- Знайти оцінки студентів у окремій групі з певного предмета
SELECT students.first_name, students.last_name, grades.grade
FROM students
JOIN grades ON students.id = grades.student_id
WHERE students.group_id = ? AND grades.subject_id = ?;