--Step 1: Write a Query
--For US Customers Find the total number of customers and the average score
use SalesDB

SELECT 
	COUNT(*) TotalCustomers,
	AVG(Score) AVgScore
FROM Sales.Customers
WHERE Country = 'USA'

--Step 2: Turning the query into a Stored Procedure

CREATE PROCEDURE GetCustomerSummary AS
BEGIN
SELECT 
	COUNT(*) TotalCustomers,
	AVG(Score) AVgScore
FROM Sales.Customers
WHERE Country = 'USA'
END

--Step 3: Execute the Stored Procedure

EXEC GetCustomerSummary


--Using Parameters in Stored Procedures

ALTER PROCEDURE GetCustomerSummary @Country NVARCHAR(50)
AS
BEGIN
SELECT 
	COUNT(*) TotalCustomers,
	AVG(Score) AVgScore
FROM Sales.Customers
WHERE Country = @Country
END

EXEC GetCustomerSummary @Country = 'Germany'

--Adding Default value to the stored procedure
ALTER PROCEDURE GetCustomerSummary @Country NVARCHAR(50) = 'USA'
AS
BEGIN
SELECT 
	COUNT(*) TotalCustomers,
	AVG(Score) AVgScore
FROM Sales.Customers
WHERE Country = @Country
END

EXEC GetCustomerSummary @Country = 'Germany'

--Multi Queries in Stored Procedures

ALTER PROCEDURE GetCustomerSummary @Country NVARCHAR(50) = 'USA'
AS
BEGIN
SELECT 
	COUNT(*) TotalCustomers,
	AVG(Score) AVgScore
FROM Sales.Customers
WHERE Country = @Country;
--Find the total No. of Orders and Total Sales
SELECT
	COUNT(OrderID) TotalOrders,
	SUM(Sales) TotalSales
FROM Sales.Orders o
JOIN Sales.Customers c
ON c.CustomerID = o.CustomerID
WHERE c.Country = @Country;
END

--Using Parameters in Stored Procedures
ALTER PROCEDURE GetCustomerSummary @Country NVARCHAR(50) = 'USA'
AS
BEGIN
SELECT 
	COUNT(*) TotalCustomers,
	AVG(Score) AVgScore
FROM Sales.Customers
WHERE Country = @Country;

SELECT
	COUNT(OrderID) TotalOrders,
	SUM(Sales) TotalSales
FROM Sales.Orders o
JOIN Sales.Customers c
ON c.CustomerID = o.CustomerID
WHERE c.Country = @Country;
END

--Using Variables in Stored Procedures
ALTER PROCEDURE GetCustomerSummary @Country NVARCHAR(50) = 'USA'
AS
BEGIN

DECLARE @TotalCustomers INT, @AvgScore FLOAT;

SELECT 
	@TotalCustomers = COUNT(*),
	@AvgScore = AVG(Score)
FROM Sales.Customers
WHERE Country = @Country;

PRINT 'Total Customers from ' + @Country + ':' + CAST(@TotalCustomers AS NVARCHAR);
PRINT 'Average Score from ' + @Country + ':' + CAST(@AvgScore AS NVARCHAR);

SELECT
	COUNT(OrderID) TotalOrders,
	SUM(Sales) TotalSales
FROM Sales.Orders o
JOIN Sales.Customers c
ON c.CustomerID = o.CustomerID
WHERE c.Country = @Country;
END

--Creating a Table for working with triggers
CREATE TABLE Sales.EmployeeLogs (
	LogID INT IDENTITY(1,1) PRIMARY KEY,
	EmployeeID INT,
	LogMessage VARCHAR(255),
	LogDate DATE
)
--Creating a Trigger for that Table
CREATE TRIGGER trg_AfterInsertEmployee ON Sales.Employees
AFTER INSERT
AS
BEGIN
	INSERT INTO Sales.EmployeeLogs (EmployeeID, LogMessage, LogDate)
	SELECT
		EmployeeID,
		'New Employee Added =' + CAST(EmployeeID AS VARCHAR),
		GETDATE()
	FROM INSERTED
END

INSERT INTO Sales.Employees
VALUES
(6, 'Maria', 'Doe', 'HR', '1988-01-12', 'F', 80000, 3)

SELECT * FROM Sales.EmployeeLogs