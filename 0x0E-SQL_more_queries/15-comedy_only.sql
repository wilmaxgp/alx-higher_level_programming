
USE hbtn_0d_tvshows;
SELECT genres.name
FROM shows
JOIN genres ON shows.genre_id = genres.id
WHERE shows.name = 'Dexter';
