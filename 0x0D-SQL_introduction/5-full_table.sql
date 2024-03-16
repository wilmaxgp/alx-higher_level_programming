-- SQL script to print full description of table first_table from database hbtn_0c_0

SELECT CONCAT(
    TABLE_NAME, 
    'CREATE TABLE ',
    '`', 
    TABLE_NAME, 
    '` (',
    GROUP_CONCAT(
        CONCAT(
            '`', COLUMN_NAME, '` ',
            COLUMN_TYPE,
            IF(IS_NULLABLE = 'NO', ' NOT NULL', ''),
            IF(COLUMN_DEFAULT IS NOT NULL, CONCAT(' DEFAULT ', QUOTE(COLUMN_DEFAULT)), ''),
            IF(COLUMN_KEY = 'PRI', ' PRIMARY KEY', ''),
            IF(EXTRA = 'auto_increment', ' AUTO_INCREMENT', '')
        )
        ORDER BY ORDINAL_POSITION
        SEPARATOR ',\n  '
    ),
    ') ENGINE=', ENGINE,
    ' DEFAULT CHARSET=', CHARACTER_SET_NAME, 
    ' COLLATE=', COLLATION_NAME
) AS full_description
FROM information_schema.TABLES
WHERE TABLE_SCHEMA = 'hbtn_0c_0'
AND TABLE_NAME = 'first_table';
