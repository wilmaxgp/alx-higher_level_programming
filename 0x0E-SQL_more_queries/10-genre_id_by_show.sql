-- SQL script to list all cities contained in the database hbtn_0d_usa by ascending order
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id;
