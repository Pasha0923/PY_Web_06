-- Знайти 5 студентів із найбільшим середнім балом з усіх предметів --
SELECT s.fullname, AVG(g.grade) AS avg_grade
FROM students s
JOIN grades g ON g.student_id = s.id
GROUP BY s.id
ORDER BY avg_grade DESC
LIMIT 5;

