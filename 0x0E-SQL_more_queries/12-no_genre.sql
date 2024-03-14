-- SQL script to change the name California to Cali on the states table

SELECT tv_shows.title
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
GROUP BY tv_shows.title
HAVING COUNT(tv_show_genres.genre_id) = 0;
