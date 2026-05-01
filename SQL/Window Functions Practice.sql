use SalesDB

SELECT * FROM Sales.Orders

--Using Where and Group By
SELECT
	ProductID,
	OrderStatus,
	SUM(Sales) as TotalSales
FROM Sales.Orders
Where OrderStatus = 'Shipped'
GROUP BY ProductID, OrderStatus


--Using Group By and Having
SELECT
	ProductID,
	OrderStatus,
	SUM(Sales) as TotalSales
FROM Sales.Orders
GROUP BY ProductID, OrderStatus
HAVING OrderStatus = 'Delivered'


--Using Window Function to Find Total Sales of Each ProductID
SELECT
	ProductID,
	OrderDate,
	SUM(Sales) OVER (PARTITION BY ProductID) as TotalSales
FROM Sales.Orders

--Using Window Function to RANK Total Sales
SELECT
	ProductID,
	OrderDate,
	Sales,
	SUM(Sales) OVER (PARTITION BY ProductID) as TotalSales,
	RANK() OVER (ORDER BY ProductID DESC) as RankSales
FROM Sales.Orders

--Using Window Function to DENSE_RANK Total Sales
SELECT
	ProductID,
	OrderDate,
	Sales,
	SUM(Sales) OVER (PARTITION BY ProductID) as TotalSales,
	DENSE_RANK() OVER (ORDER BY ProductID DESC) as RankSales
FROM Sales.Orders

----Using Window Function to ROW_NUMBER Total Sales
SELECT
	ProductID,
	OrderDate,
	Sales,
	SUM(Sales) OVER (PARTITION BY ProductID) as TotalSales,
	ROW_NUMBER() OVER (ORDER BY ProductID DESC) as RankSales
FROM Sales.Orders

--Using Aggregate Functions in Window Functions
SELECT
	ProductID,
	OrderDate,
	AVG(Sales) OVER (PARTITION BY ProductID) as AvgSales,
	DENSE_RANK() OVER (ORDER BY ProductID ASC) as RankSales
FROM Sales.Orders