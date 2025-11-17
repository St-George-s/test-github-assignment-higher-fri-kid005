-- QUESTION 2B:
SELECT p.forename, p.surname, p.plannerNo, COUNT(w.walkID) AS 'Total participants'
FROM Planner p 
JOIN Route r ON r.plannerNo = p.plannerNo
JOIN Walk w ON w.routeID = r.routeID
GROUP BY p.plannerNo 
ORDER BY COUNT(w.walkID) DESC;