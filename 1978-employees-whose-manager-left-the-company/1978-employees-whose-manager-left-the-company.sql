# Write your MySQL query statement below
SELECT a.employee_id
FROM Employees AS a
LEFT JOIN Employees AS b
ON a.manager_id = b.employee_id
WHERE a.salary < 30000 AND (a.manager_id IS NOT NULL AND b.name IS NULL)
ORDER BY a.employee_id