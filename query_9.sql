-- Знайти список курсів, які відвідує студент
SELECT subjects.subject_name, students.first_name, students.last_name
FROM grades, students
JOIN subjects ON grades.subject_id = subjects.subject_id
WHERE grades.student_id = 2;
