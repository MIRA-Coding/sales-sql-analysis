SELECT city, COUNT(*) AS customers_count
FROM customers
GROUP BY city;
