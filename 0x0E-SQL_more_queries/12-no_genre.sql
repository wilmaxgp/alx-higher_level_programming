
USE hbtn_0d_tvshows;
SELECT genres.name AS genre_name, COUNT(shows.id) AS number_of_shows
FROM genres
LEFT JOIN shows ON genres.id = shows.genre_id
GROUP BY genres.id
ORDER BY number_of_shows DESC, genres.id ASC;
