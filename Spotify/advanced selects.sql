-- SELECT artist_name 
-- FROM Artists 
-- WHERE artist_name LIKE 'T%';

-- 'T%' starts with letter 'T'

-- SELECT album_name, release_year 
-- FROM Albums 
-- WHERE release_year >= 2015 
-- ORDER BY release_year ASC;

-- DESC means DESCENDING ORDER!!!
-- ASC means ASCENDING!!!

-- SELECT a.album_name AS Album, a.release_year Year 
-- FROM Albums a 
-- WHERE a.release_year > 2010 
-- ORDER BY a.release_year;

-- SELECT artist_name, LENGTH(artist_name) AS Name_Length 
-- FROM Artists 
-- WHERE artist_name LIKE '_a%';

-- SELECT track_name
-- FROM Tracks
-- WHERE track_name LIKE 'S%E'; 

-- SELECT album_name, 2025 - release_year
-- FROM Albums
-- WHERE release_year > 2010;

SELECT artist_name, LENGTH(artist_name)
FROM Artists
WHERE artist_name LIKE '_____';