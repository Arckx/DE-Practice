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


