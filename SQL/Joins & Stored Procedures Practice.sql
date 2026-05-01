use SalesDB

Select * from Sales.Customers
SELECT * FROM Sales.Products
SELECT * FROM Sales.Employees
SELECT * FROM Sales.Orders

--Task: Show each customer’s full name and total number of orders.
SELECT
	CONCAT_WS(' ', c.FirstName, c.LastName) as FullName,
	COUNT(o.OrderID) as total_orders
FROM Sales.Customers c
LEFT JOIN Sales.Orders o
ON c.CustomerID = o.CustomerID
GROUP BY CONCAT_WS(' ', c.FirstName, c.LastName)

--Task: Find total sales handled by each employee.
SELECT
	CONCAT_WS(' ', e.FirstName, e.LastName) as FullName,
	SUM(o.Sales) as total_sales
FROM Sales.Employees e
LEFT JOIN Sales.Orders o
ON e.EmployeeID = o.SalesPersonID
GROUP BY CONCAT_WS(' ', e.FirstName, e.LastName)

--Task: Create a procedure that returns all orders for a given CustomerID.
CREATE PROCEDURE customer_orders
@CustomerID int
as
BEGIN
	SELECT
		CustomerID,
		SUM(Quantity) as total_orders
	FROM Sales.Orders
	WHERE CustomerID = @CustomerID
	GROUP BY CustomerID
END

EXEC customer_orders @CustomerID=2

--Task: Return total sales grouped by month.
CREATE PROCEDURE month_sales as
BEGIN
	SELECT 
		MONTH(OrderDate) as month,
		SUM(Sales) as total_sales
	FROM Sales.Orders
	GROUP BY MONTH(OrderDate)
END

EXEC month_sales

