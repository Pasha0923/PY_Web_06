-- Знайти оцінки студентів у окремій групі з певного предмета. (по назві групи та предмету )
SELECT s.fullname, g.grade
FROM students s
JOIN groups gr ON gr.id = s.group_id
JOIN grades g ON g.student_id = s.id
JOIN subjects sub ON sub.id = g.subject_id
WHERE gr.name = 'Group-1'
  AND sub.name = 'SQL';