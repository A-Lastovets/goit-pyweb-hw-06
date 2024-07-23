-- Знайти середній бал у групах з певного предмета
SELECT groups.group_name, AVG(grades.grade) as avg_grade
FROM students
JOIN groups ON students.group_id = groups.id
JOIN grades ON students.id = grades.student_id
WHERE grades.subject_id = ?
GROUP BY groups.id;
