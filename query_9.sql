-- Знайти список курсів, які відвідує студент
SELECT subjects.subject_name
FROM grades
JOIN subjects ON grades.subject_id = subjects.id
WHERE grades.student_id = ?;
