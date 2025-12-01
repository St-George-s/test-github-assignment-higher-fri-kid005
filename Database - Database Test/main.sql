DESCRIBE ALL TABLES;

-- 3.1:
-- SELECT e.episodeTitle, s.showName, e.maxViewers, e.episodeDate
-- FROM Episode e 
-- JOIN Show s ON e.showID = s.showID;

-- 3.2:
-- SELECT s.showName AS 'Show', e.episodeTitle AS 'Episode'
-- FROM Show s 
-- JOIN Episode e ON e.showID = s.showID
-- WHERE e.episodeDate LIKE '2024-12-__';

-- 3.3:
-- UPDATE Timeslot 
-- SET endTime = '19:30'
-- WHERE showID = 2 AND airDate = '2024-12-24';