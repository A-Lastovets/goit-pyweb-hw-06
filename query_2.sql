-- Знайти студента із найвищим середнім балом з певного предмета
SELECT students.first_name, students.last_name as student_name, subject_name as subject_name, AVG(grades.grade) as avg_grade
FROM students
JOIN grades ON students.student_id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.subject_id
WHERE grades.subject_id = 3
GROUP BY students.student_id
ORDER BY avg_grade DESC
LIMIT 1;
