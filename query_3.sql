-- Знайти середній бал у групах з певного предмета
SELECT groups.group_name, subject_name, AVG(grades.grade) as avg_grade
FROM students
JOIN groups ON students.group_id = groups.group_id
JOIN grades ON students.student_id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.subject_id
WHERE grades.subject_id = 4
GROUP BY groups.group_id, subject_name
ORDER BY groups.group_id ASC;
