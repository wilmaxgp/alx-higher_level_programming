
USE hbtn_0d_tvshows;
SELECT shows.name, COUNT(DISTINCT season) AS num_seasons
FROM shows
JOIN episodes ON shows.id = episodes.show_id
GROUP BY shows.name;
