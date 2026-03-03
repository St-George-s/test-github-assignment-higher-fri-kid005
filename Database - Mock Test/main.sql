-- QUESTION 3.1:
-- SELECT e.eventName as "Event Name", 
-- s.name as "Shop Name",
-- e.maxAttendees as "Max Attendees", 
-- e.eventDate as "Event Date"
-- FROM Event e 
-- JOIN Shop s ON s.shopID = e.shopID;

-- QUESTION 3.2:
-- SELECT s.name as "Shop Name", e.eventName as "Event Name"
-- FROM Shop s
-- JOIN Event e ON e.shopID = s.shopID
-- WHERE e.eventDate = "2024-12-25";

-- QUESTION 3.3:
-- UPDATE OpeningTime
-- SET closeTime = "19:00"
-- WHERE shopID = 2;

-- QUESTION 4.1:
-- SELECT s.name AS "Shop Name", COUNT(b.bookingID) AS "Total Bookings"
-- FROM Shop s 
-- JOIN event e ON e.shopID = s.shopID
-- JOIN Booking b ON b.eventID = e.eventID
-- GROUP BY s.name;   