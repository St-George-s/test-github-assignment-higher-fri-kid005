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
SELECT s.initial, s.surname, t.teamName, E.city, E.eventDate
FROM Event e
JOIN Race ra ON e.eventID = ra.eventID
JOIN Result res ON res.raceNumber = ra.raceNumber
JOIN Swimmer s ON res.swimmerID = s.swimmerID
JOIN Team t ON t.teamRef = s.teamRef
WHERE res.raceTime = (
    SELECT MIN(res.raceTime)
    FROM Result
    WHERE res.lane = 1 or 8
);