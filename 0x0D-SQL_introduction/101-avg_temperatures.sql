-- imp table dumb
-- display avg temp by city sort by temp desc
SELECT city, AVG(value)
AS avg_temp
FROM temperatures
GROUP BY city ORDER BY avg_temp DESC;
