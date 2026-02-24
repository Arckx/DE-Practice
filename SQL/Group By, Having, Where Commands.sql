use company

select * from orders
SELECT * FROM persons

--Aggregate Functions

SELECT COUNT(*) 
FROM orders

SELECT SUM(total_amount) 
FROM orders

SELECT AVG(total_amount) 
FROM orders

SELECT MIN(total_amount) 
FROM orders

SELECT MAX(total_amount) 
FROM orders

--Using GROUP BY Command

SELECT COUNT(status) as count_status, status, SUM(total_amount) as sum_amt
FROM orders
GROUP BY status

use SalesDB
SELECT * FROM Sales.Orders