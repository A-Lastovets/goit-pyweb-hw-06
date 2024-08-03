-- Список курсів, які певному студенту читає певний викладач
SELECT DISTINCT subjects.subject_id, subjects.subject_name AS subject_name
FROM subjects
JOIN grades ON subjects.subject_id = grades.subject_id
JOIN teachers ON subjects.subject_id = teachers.subject_id
WHERE grades.student_id = 3 AND teachers.teacher_id = 6;
