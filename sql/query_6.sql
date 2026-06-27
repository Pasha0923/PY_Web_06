-- Знайти список студентів у певній групі.('Group-1')
SELECT s.fullname, gr.name AS group_name
FROM students s
JOIN groups gr ON gr.id = s.group_id
WHERE gr.name = 'Group-1';