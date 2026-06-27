-- Знайти які курси читає певний викладач.(по id)
SELECT t.fullname, sub.name AS subject
FROM teachers t
JOIN subjects sub ON sub.teacher_id = t.id
WHERE t.id = 1;