-- SQL script to display the cities and states in alphabetical order by city, followed by state
SELECT cities.name AS city_name, states.name AS state_name
FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY cities.name ASC, states.name ASC;
