-- lists all records of table x of database x
-- display score then name ordered by score
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC
