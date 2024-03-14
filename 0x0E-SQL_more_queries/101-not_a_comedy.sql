-- SQL script to display the latest data from the database
SELECT cities.id AS city_id, cities.name AS city_name, states.name AS state_name
FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY cities.id DESC
LIMIT 10;
