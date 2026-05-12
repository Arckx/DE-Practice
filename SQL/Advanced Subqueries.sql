exec sp_databases
use SalesDB

SELECT * FROM Sales.Customers
SELECT * FROM Sales.Employees
SELECT * FROM Sales.Orders
SELECT * FROM Sales.OrdersArchive
SELECT * FROM Sales.Products


INSERT INTO Sales.Orders
(ProductID, CustomerID, SalesPersonID, OrderDate, ShipDate, OrderStatus, ShipAddress, BillAddress, Quantity, Sales, CreationTime)
SELECT
	ProductID, CustomerID, SalesPersonID, OrderDate, ShipDate, OrderStatus, ShipAddress, BillAddress, Quantity, Sales, CreationTime
FROM Sales.OrdersArchive
WHERE OrderStatus = 'Shipped'