-- Question 2c
SELECT forename, surname
FROM Customer  
JOIN Purchase ON Customer.customerID = Purchase.customerID
JOIN Movie ON Purchase.movieCode = Movie.movieCode
WHERE duration = (
    SELECT MIN(duration)
    FROM Movie 
);


-- Question 2d
SELECT forename, surname, SUM(price) AS "Total spent(£)"
FROM Customer  
JOIN Purchase ON Customer.customerID = Purchase.customerID
JOIN Movie ON Purchase.movieCode = Movie.movieCode
JOIN Genre ON Movie.genreID = Genre.genreID
WHERE genreName = 'Comedy'
GROUP BY Customer.customerID
ORDER BY SUM(price) DESC;


-- Question 2e
SELECT forename, surname, email
FROM customer, purchase, movie
WHERE customer.customerID = purchase.customerID
AND movie.movieCode = purchase.movieCode
AND released >= 1990
AND released<=1999
GROUP BY customer.customerID
ORDER BY forename;