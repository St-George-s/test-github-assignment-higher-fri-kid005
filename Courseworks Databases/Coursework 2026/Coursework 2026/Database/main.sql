-- Question 2c
SELECT c.forename, c.surname
FROM Customer c 
JOIN Purchase p ON c.customerID = p.customerID
JOIN Movie m ON p.movieCode = m.movieCode
WHERE m.duration = (
    SELECT MIN(duration)
    FROM Movie m
);


-- Question 2d
SELECT c.forename, c.surname, SUM(m.price) AS "Total spent(£)"
FROM Customer c 
JOIN Purchase p ON c.customerID = p.customerID
JOIN Movie m ON p.movieCode = m.movieCode
JOIN Genre g ON m.genreID = m.genreID
WHERE g.genreName = 'Comedy'
GROUP BY c.customerID
ORDER BY SUM(m.price) DESC;


-- Question 2e
-- SELECT forename, surname, email
-- FROM customer, purchase, movie
-- WHERE customer.customerID = purchase.customerID
-- AND movie.movieCode = purchase.movieCode
-- AND released = 1990;