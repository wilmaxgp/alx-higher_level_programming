-- SQL script to create table second_table in database hbtn_0c_0 and insert multiple rows

CREATE TABLE IF NOT EXISTS hbtn_0c_0.second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

INSERT INTO hbtn_0c_0.second_table (id, name, score) VALUES (1, 'John', 10);
INSERT INTO hbtn_0c_0.second_table (id, name, score) VALUES (2, 'Alex', 3);
INSERT INTO hbtn_0c_0.second_table (id, name, score) VALUES (3, 'Bob', 14);
INSERT INTO hbtn_0c_0.second_table (id, name, score) VALUES (4, 'George', 8);
