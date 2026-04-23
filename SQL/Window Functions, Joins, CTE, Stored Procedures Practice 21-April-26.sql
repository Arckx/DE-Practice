EXEC sp_databases;
use SalesDB

SELECT * FROM Sales.Products
SELECT * FROM Sales.Orders

--Joining two tables and using Window Function RANK for Sales
SELECT 
	o.OrderID,
	p.Product,
	p.Category,
	o.OrderStatus,
	o.Quantity,
	o.Sales,
	RANK() OVER(ORDER BY o.Sales DESC) as ranked_sales
FROM Sales.Products p
INNER JOIN Sales.Orders o
ON p.ProductID = o.ProductID

--1. For each category, rank products from highest to lowest price.
SELECT
	Product,
	Category,
	Price,
	RANK() OVER(PARTITION BY Category ORDER BY Price DESC) as ranked_products
FROM Sales.Products

--2. Identify the product in each category with the highest total sales.

WITH total_sales as (
	SELECT
		p.Product as product,
		p.Category as category,
		SUM(o.Sales) as total_sales,
		ROW_NUMBER() OVER(PARTITION BY category ORDER BY SUM(o.Sales) DESC) as highest_sales
	FROM Sales.Products p
	JOIN Sales.Orders o
	ON p.ProductID = o.ProductID
	GROUP BY p.Product, p.Category
)
SELECT 
		product,
		category
FROM total_sales
WHERE highest_sales = 1

--3. Calculate cumulative sales over time based on OrderDate.
SELECT 
	OrderDate,
	SUM(Sales) OVER(ORDER BY OrderDate) as cumulative_sales
FROM Sales.Orders

--4. Find customers who placed multiple orders.

SELECT * FROM Sales.Orders
WITH multiple_orders as (
SELECT 
	CustomerID,
	COUNT(*) AS total_orders
FROM Sales.Orders
GROUP BY CustomerID
)
SELECT *
FROM multiple_orders
WHERE total_orders > 1

--List products that do not appear in the Orders table.
SELECT * FROM Sales.Products
SELECT * FROM Sales.Orders

SELECT
	p.Product,
	o.*
FROM Sales.Products p
LEFT JOIN Sales.Orders o
ON o.ProductID = p.ProductID
WHERE o.OrderID is NULL

--Calculate the average sales amount per customer.
SELECT
	o.CustomerID,
	AVG(o.Quantity * p.Price) as avg_sales
FROM Sales.Products p
INNER JOIN Sales.Orders o
ON p.ProductID = o.ProductID
GROUP BY CustomerID

--Detect duplicate orders where ProductID and OrderDate are the same.

WITH duplicate_product_orders as 
(SELECT 
	ProductID, 
	OrderDate,
	COUNT(*) OVER(PARTITION BY ProductID, OrderDate) as multiple_orders
FROM Sales.Orders)
SELECT *
FROM duplicate_product_orders
WHERE multiple_orders > 1

