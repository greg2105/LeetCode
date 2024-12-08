# Write your MySQL query statement below
SELECT e.name, b.bonus
FROM Employee e
LEFT JOIN Bonus b

# relate the tables using the primary/foreign key
ON e.empID = b.empID

# pick using this criteria
WHERE b.bonus < 1000 OR b.bonus IS NULL;