-- SQL script to list all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost)
SELECT * FROM mysql.user WHERE user IN ('user_0d_1', 'user_0d_2');
