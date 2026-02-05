SELECT * 
FROM Tracks 
WHERE album_id IN (
  SELECT album_id 
  FROM Albums 
  WHERE release_year > 2018
 );

--  SELECT T.track_name, A.album_name 
--  FROM Tracks T, Albums A
--  WHERE T.album_id = A.album_id
--    AND A.release_year > 2018;

-- SELECT T.track_name, A.album_name 
-- FROM Tracks T 
-- JOIN Albums A ON T.album_id = A.album_id 
-- WHERE A.release_year > 2020;

-- SELECT A.artist_name, COUNT(T.track_id) AS "Total Tracks"
-- FROM Artists A 
-- JOIN Tracks T ON A.artist_id = T.artist_id 
-- GROUP BY A.artist_name;

-- SELECT * 
-- FROM Tracks 
-- WHERE album_id IN (
--   SELECT album_id 
--   FROM Albums 
--   WHERE release_year < 2020
--  );

-- SELECT T.track_name
-- FROM Tracks T
-- JOIN Artists A ON A.artist_id = T.artist_id
-- WHERE A.artist_name = 'Lizzo';

-- SELECT T.track_name, G.genre_name
-- FROM Tracks T 
-- JOIN Genres G ON G.genre_id = T.track_id;

-- SELECT G.genre_name AS Genre, COUNT(T.track_id) AS "Total Tracks"
-- FROM Tracks T
-- JOIN Albums A ON A.album_id = T.track_id
-- JOIN Genres G ON G.genre_id = T.track_id
-- WHERE A.release_year = 2019;