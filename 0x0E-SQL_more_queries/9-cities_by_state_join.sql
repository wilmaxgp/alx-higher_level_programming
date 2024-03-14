-- SQL script to create the database hbtn_0d_usa and add San Francisco to the cities table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

INSERT INTO cities (state_id, name) VALUES (
    (SELECT id FROM states WHERE name = 'California'),
    'San Francisco'
);
