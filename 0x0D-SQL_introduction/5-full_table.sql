-- SQL script to print full description of table first_table from database hbtn_0c_0

SELECT CONCAT(TABLE_NAME, CREATE_TABLE) AS first_table
FROM information_schema.TABLES
WHERE TABLE_SCHEMA = 'hbtn_0c_0'
AND TABLE_NAME = 'first_table';
