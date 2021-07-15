-- list number of records with the same score in table x
-- displays score and number of records with that score, desc sort
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score DESC;
