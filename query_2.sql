-- Знайти студента із найвищим середнім балом з певного предмета
SELECT students.first_name, students.last_name, AVG(grades.grade) as avg_grade
FROM students
JOIN grades ON students.id = grades.student_id
WHERE grades.subject_id = ?
GROUP BY students.id
ORDER BY avg_grade DESC
LIMIT 1;
