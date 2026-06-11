-- QUESTION 1Bi
SELECT c.forename, c.surname, (b.adultTicket*5.50)+(b.childTicket*2.0)+(b.concessionTicket*1.5) AS "Tax (£)"
FROM Customer c 
JOIN Booking b ON c.customerID = b.customerID
WHERE c.customerID = "GR01932"
AND b.flightID = "QH182";


-- QUESTION 1Bii
SELECT c.forename, c.surname
FROM Customer c 
JOIN Booking b ON c.customerID = b.customerID
WHERE childTicket = (
    SELECT MAX(childTicket)
    FROM Booking b 
);