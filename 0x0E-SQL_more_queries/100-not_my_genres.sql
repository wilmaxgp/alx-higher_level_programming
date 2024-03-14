-- SQL script to display the number of cities in each state in descending order

SELECT tv_genres.name
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title != 'Dexter' OR tv_shows.title IS NULL
GROUP BY tv_genres.name
ORDER BY tv_genres.name ASC;
