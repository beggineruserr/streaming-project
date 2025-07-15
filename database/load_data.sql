DROP TABLE IF EXISTS temp_shows;

CREATE TABLE temp_shows (
    title VARCHAR(100),
    platform VARCHAR(50),
    rating NUMERIC,
    release_year INT
);

\COPY temp_shows(title, platform, rating, release_year)
FROM '/Users/jonathanlopez/streaming-project/data/shows_clean.csv'
DELIMITER ','
CSV HEADER;

INSERT INTO shows (title, platform_id, rating, release_year)
SELECT ts.title, p.platform_id, ts.rating, ts.release_year
FROM temp_shows ts
JOIN platforms p ON ts.platform = p.platform_name;