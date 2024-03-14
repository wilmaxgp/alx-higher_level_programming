
USE hbtn_0d_tvshows;
SELECT shows.name, COALESCE(genres.name, 'Unknown') AS genre_name
FROM shows
LEFT JOIN genres ON shows.genre_id = genres.id
ORDER BY shows.id ASC;
