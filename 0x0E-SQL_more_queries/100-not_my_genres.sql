-- SQL script to display the number of cities in each state in descending order
SELECT states.name AS state_name, COUNT(cities.id) AS number_of_cities
FROM states
LEFT JOIN cities ON states.id = cities.state_id
GROUP BY states.name
ORDER BY number_of_cities DESC;
