
USE hbtn_0d_usa;
SELECT cities.* 
FROM cities
JOIN states ON cities.state_id = states.id
WHERE states.name = 'California'
ORDER BY cities.id ASC;
