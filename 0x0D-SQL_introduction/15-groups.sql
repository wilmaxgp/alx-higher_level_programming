-- SQL script to list the number of records with the same score in table second_table of database hbtn_0c_0 sorted by the number of records (descending)

SELECT score, COUNT(*) AS number FROM hbtn_0c_0.second_table GROUP BY score ORDER BY number DESC;
