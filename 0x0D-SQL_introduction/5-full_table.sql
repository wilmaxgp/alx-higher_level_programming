-- SQL script to print full description of table first_table from database hbtn_0c_0

SET @db_name = 'hbtn_0c_0';
SET @table_name = 'first_table';
SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_KEY, COLUMN_DEFAULT, EXTRA, COLUMN_COMMENT
FROM information_schema.columns
WHERE table_schema = @db_name
AND table_name = @table_name;
