use SalesDB

EXEC sp_tables

SELECT * FROM Sales.Employees
SELECT * FROM Sales.Customers
SELECT * FROM Sales.Orders
SELECT * FROM Sales.Products

--Using SubQuery and Window Function in Select command
SELECT 
	OrderID,
	ProductID,
	Quantity,
	SUM(Quantity) OVER(Partition By ProductID) as No_of_Orders
FROM Sales.Orders
WHERE OrderStatus = 'Delivered'

--Joining 5 Tables Sales.Orders, Sales.Employees, Sales.Orders, Sales.Products
SELECT *
FROM 
	Sales.Orders as so
FULL JOIN Sales.Products as sp ON so.ProductID = sp.ProductID
FULL JOIN Sales.Customers as sc ON so.CustomerID = sc.CustomerID


--Using SubQuery in From command
SELECT 
	so.ProductID,
	sp.Price,
	SUM(Quantity) as TotalQuantity,
	SUM(Sales) as TotalSales
FROM Sales.Orders as so
		FULL JOIN Sales.Products as sp ON so.ProductID = sp.ProductID
		FULL JOIN Sales.Customers as sc ON so.CustomerID = sc.CustomerID
	
GROUP BY so.ProductID, sp.Price