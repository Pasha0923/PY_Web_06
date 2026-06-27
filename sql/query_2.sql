-- Знайти студента із найвищим середнім балом з певного предмета -- 
SELECT s.fullname, AVG(g.grade) AS avg_grade
FROM students s
JOIN grades g ON g.student_id = s.id
JOIN subjects sub ON sub.id = g.subject_id
WHERE sub.name = 'Python'
GROUP BY s.id, s.fullname
ORDER BY avg_grade DESC
LIMIT 1;