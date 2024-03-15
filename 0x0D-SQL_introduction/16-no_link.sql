-- SQL script to list all records of table second_table from database hbtn_0c_0 where name is not NULL ordered by descending score

SELECT score, name FROM hbtn_0c_0.second_table WHERE name IS NOT NULL ORDER BY score DESC;
