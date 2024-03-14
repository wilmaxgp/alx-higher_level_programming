-- SQL script to change the name California to Cali on the states table
UPDATE states SET name = 'Cali' WHERE name = 'California';
