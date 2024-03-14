SELECT CONCAT('Grants for ', user, '@', host) AS Privileges
FROM mysql.user
WHERE user = 'user_0d_1' AND host = 'localhost';

SHOW GRANTS FOR 'user_0d_1'@'localhost';
