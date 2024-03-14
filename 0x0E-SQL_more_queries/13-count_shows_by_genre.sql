
USE hbtn_0d_tvshows;

-- Add foreign key constraint to episodes table
ALTER TABLE episodes
ADD CONSTRAINT fk_episodes_show_id
FOREIGN KEY (show_id) REFERENCES shows(id);

-- Add foreign key constraint to ratings table
ALTER TABLE ratings
ADD CONSTRAINT fk_ratings_show_id
FOREIGN KEY (show_id) REFERENCES shows(id);
