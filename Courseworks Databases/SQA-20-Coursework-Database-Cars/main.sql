-- QUESTION 1Bi

-- SELECT g.garageName, SUM(j.cost) AS "Total sales"
-- FROM Garage g 
-- JOIN Job j ON j.garageID = g.garageID
-- WHERE j.dateOut = "19-Jan-20"
-- GROUP BY g.garageID;


-- QUESTION 1Bii

-- SELECT MAX(j.dateOut - j.dateIn) AS "Number of days", j.regNo, g.garageName
-- FROM Job j 
-- JOIN Garage g ON g.garageID = j.garageID; 


-- QUESTION 1C

SELECT forename, surname, AVG(cost) AS "Average Job Cost"
FROM Customer, Car, Job
WHERE Customer.customerID = Car.customerID AND Car.regNo = Job.regNo
GROUP BY forename, surname, Customer.customerID
ORDER BY AVG(cost) DESC;