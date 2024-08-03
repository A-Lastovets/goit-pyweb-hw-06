-- Знайти які курси читає певний викладач
SELECT subjects.subject_name, teachers.name
FROM subjects, teachers
WHERE teachers.teacher_id = 4;
