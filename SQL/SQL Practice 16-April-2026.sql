use SalesDB

select * from Sales.Orders
select * from Sales.Customers

SELECT *
FROM 
	(SELECT FirstName, Country, Score
	  FROM Sales.Customers
	  WHERE Country = 'USA'
	) as usa_customers
WHERE usa_customers.score IS NULL

SELECT
	OrderID,
	OrderStatus,
	Quantity,
	Sales
FROM Sales.Orders
WHERE Sales > (
			SELECT AVG(Sales) as avg_sales
			FROM Sales.Orders
			)

SELECT
	OrderID,
	OrderStatus,
	Quantity,
	Sales
FROM Sales.Orders
WHERE Sales = (
			SELECT AVG(Sales) as avg_sales
			FROM Sales.Orders
			)


SELECT 
	CustomerID,
	OrderStatus,
	Quantity,
	Sales
FROM Sales.Orders

WITH SalesCustomers as (
SELECT *
FROM Sales.Customers
),
SalesOrders as (
SELECT *
FROM Sales.Orders
)
SELECT *
FROM SalesCustomers sc
INNER JOIN SalesOrders so
ON sc.CustomerID = so.CustomerID


