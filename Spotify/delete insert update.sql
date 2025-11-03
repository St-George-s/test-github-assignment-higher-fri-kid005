-- DELETE FROM Tracks 
-- WHERE track_id = 5;

-- DELETE FROM Artists 
-- WHERE artist_id BETWEEN 20 AND 25;

-- INSERT INTO Genres (genre_id, genre_name) 
-- VALUES (21, 'Jazz');

-- INSERT INTO Tracks (track_id, track_name, artist_id, album_id, genre_id, duration_ms) 
-- VALUES (54, 'New Track', 4, 4, 1, 180000), 
--        (55, 'Another Track', 5, 5, 2, 200000);

-- UPDATE Albums 
-- SET release_year = 2021 
-- WHERE album_id = 3;

-- UPDATE Artists 
-- SET artist_name = 'New Artist Name' 
-- WHERE artist_id IN (1, 2, 3);

-- SELECT *
-- FROM Tracks;

-- DELETE FROM Albums 
-- WHERE release_year < 2019;

-- INSERT INTO Artists (artist_id, artist_name)
-- VALUES (34, 'Chappel Roan');

-- DELETE FROM Tracks
-- WHERE duration_ms < 120000;

-- INSERT INTO Albums (album_id, album_name, release_year)
-- VALUES (34, '1989 - Taylors Version', 2023);

-- SELECT *
-- FROM Genres;

-- UPDATE Tracks
-- SET genre_id = 4
-- WHERE track_id = 1;

