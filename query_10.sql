-- Список курсів, які певному студенту читає певний викладач
SELECT subjects.subject_name
FROM grades
JOIN subjects ON grades.subject_id = subjects.id
WHERE grades.student_id = ? AND subjects.teacher_id = ?;
