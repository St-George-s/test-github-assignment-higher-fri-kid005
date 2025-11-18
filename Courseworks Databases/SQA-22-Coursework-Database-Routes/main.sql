-- QUESTION 2B:
-- SELECT p.forename, p.surname, p.plannerNo, COUNT(w.walkID) AS 'Total participants'
-- FROM Planner p 
-- JOIN Route r ON r.plannerNo = p.plannerNo
-- JOIN Walk w ON w.routeID = r.routeID
-- GROUP BY p.plannerNo 
-- ORDER BY COUNT(w.walkID) DESC;

-- QUESTION 2C:
-- SELECT wa.walkerNo, wa.forename, wa.surname, wa.telNo
-- FROM Walker wa
-- JOIN Walk w ON wa.walkerNo = w.walkerNo
-- JOIN Route r ON w.routeID = r.routeID
-- WHERE r.distance = (
--     SELECT MAX(distance)
--     FROM Route
-- )
-- GROUP BY wa.walkerNo;

-- QUESTION 2D:
-- SELECT r.routeID, r.woodName, r.description
-- FROM Route r 
-- WHERE r.footwear LIKE "%shoe%";

SELECT *
FROM Route;