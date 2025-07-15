CREATE TABLE platforms (
    platform_id SERIAL PRIMARY KEY,
    platform_name VARCHAR(50) UNIQUE
);

CREATE TABLE genres (
    genre_id SERIAL PRIMARY KEY,
    genre_name VARCHAR(50) UNIQUE
);

CREATE TABLE shows (
    show_id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    platform_id INTEGER REFERENCES platforms(platform_id),
    genre_id INTEGER REFERENCES genres(genre_id),
    rating NUMERIC,
    release_year INT
);

-- pushing changes again