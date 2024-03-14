
USE hbtn_0d_tvshows;
SELECT shows.name, MAX(season) AS latest_season, MAX(episode) AS latest_episode
FROM shows
JOIN episodes ON shows.id = episodes.show_id
GROUP BY shows.name;
