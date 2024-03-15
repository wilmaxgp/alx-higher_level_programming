-- SQL script to display the max temperature of each state ordered by state name

SELECT state, MAX(temp) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
