-- SQL script to create the database hbtn_0d_usa and add the California state to the states table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

INSERT INTO states (name) VALUES ('California');
