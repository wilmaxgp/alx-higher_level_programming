
USE hbtn_0d_tvshows;
SELECT * FROM episodes WHERE show_id = (SELECT id FROM shows WHERE name = 'Dexter') ORDER BY season, episode;
