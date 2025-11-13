-- DESCRIBE ALL TABLES;

-- QUESTION 2C:
-- SELECT s.initial, s.surname, s.swimCategory, t.teamName, COUNT(r.position) AS "Races Won"
-- FROM Swimmer S
-- JOIN Result r ON s.swimmerID = r.swimmerID
-- JOIN Team t ON t.teamRef = s.teamRef
-- WHERE r.position = 1
-- GROUP BY s.swimmerID
-- ORDER BY s.initial ASC;

-- QUESTION 2D:
-- SELECT s.initial, s.surname, t.teamName, E.city, E.eventDate
-- FROM Event e
-- JOIN Race ra ON e.eventID = ra.eventID
-- JOIN Result res ON res.raceNumber = ra.raceNumber
-- JOIN Swimmer s ON res.swimmerID = s.swimmerID
-- JOIN Team t ON t.teamRef = s.teamRef
-- WHERE res.raceTime = (
--     SELECT MIN(raceTime)
--     FROM Result
--     WHERE lane = 1 or lane = 8
-- );

-- QUESTION 2E:
-- SELECT teamName, COUNT(position) AS [Total medals won]
-- FROM Result R, Swimmer S, Team T
-- WHERE R.swimmerID = S.swimmerID AND S.teamRef = T.teamRef AND position <4
-- GROUP BY teamName
-- ORDER BY COUNT(position) DESC;
