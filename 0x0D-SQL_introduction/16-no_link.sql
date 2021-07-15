-- lists all records of table x of db x
-- no rows without name, disp score and name, sort desc
SELECT score, name FROM second_table
WHERE name IS NOT NULL ORDER BY score DESC;
