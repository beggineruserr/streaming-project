SELECT p.platform_name, AVG(s.rating) AS avg_rating
FROM shows s
JOIN platforms p ON s.platform_id = p.platform_id
GROUP BY p.platform_name
ORDER BY avg_rating DESC;


SELECT p.platform_name, s.release_year, AVG(s.rating) AS avg_rating
FROM shows s
JOIN platforms p ON s.platform_id = p.platform_id
GROUP BY p.platform_name, s.release_year
ORDER BY s.release_year ASC, avg_rating DESC;


SELECT p.platform_name, COUNT(*) AS total_shows
FROM shows s
JOIN platforms p ON s.platform_id = p.platform_id
GROUP BY p.platform_name
ORDER BY total_shows DESC;


SELECT s.title, p.platform_name, s.rating
FROM shows s
JOIN platforms p ON s.platform_id = p.platform_id
ORDER BY s.rating DESC
LIMIT 5;


SELECT p.platform_name
FROM shows s
JOIN platforms p ON s.platform_id = p.platform_id
GROUP BY p.platform_name
ORDER BY AVG(s.rating) DESC
LIMIT 1;



SELECT p.platform_name, s.release_year, COUNT(*) AS show_count
FROM shows s
JOIN platforms p ON s.platform_id = p.platform_id
GROUP BY p.platform_name, s.release_year
ORDER BY p.platform_name, show_count DESC;
