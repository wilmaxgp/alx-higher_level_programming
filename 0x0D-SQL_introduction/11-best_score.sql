-- SQL script to list all records with a score >= 10 from table second_table of database hbtn_0c_0 ordered by score (top first)

SELECT score, name FROM hbtn_0c_0.second_table WHERE score >= 10 ORDER BY score DESC;
