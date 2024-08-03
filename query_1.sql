-- Знайти 5 студентів із найбільшим середнім балом з усіх предметів
SELECT students.first_name, students.last_name, AVG(grades.grade) as avg_grade
FROM students
JOIN grades ON students.student_id = grades.student_id
GROUP BY students.student_id
ORDER BY avg_grade DESC
LIMIT 5;
