
USE hbtn_0d_tvshows;
SELECT rating FROM ratings WHERE show_id = (SELECT id FROM shows WHERE name = 'Dexter');
