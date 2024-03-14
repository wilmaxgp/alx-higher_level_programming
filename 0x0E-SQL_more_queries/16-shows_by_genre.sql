-- SQL script to add a city to the cities table named `Palo Alto` in California
INSERT INTO cities (state_id, name)
VALUES ((SELECT id FROM states WHERE name = 'California'), 'Palo Alto');
