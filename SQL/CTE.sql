--Standalone CTE
use SalesDB
--Step1: Find the total Sales Per Customer

WITH CTE_TOTAL_SALES AS
(
	SELECT
		CustomerID,
		SUM(Sales) as TotalSales
	FROM Sales.Orders
	GROUP BY CustomerID
)

--Step2: Find the last order date for each customer (Standalone CTE)
, CTE_LAST_ORDER AS
(
	SELECT 
		CustomerID,
		MAX(OrderDate) AS Last_Order
	FROM Sales.Orders
	GROUP BY CustomerID
)

--Step3: Rank Cusomers based on Total Sales Per Customer (Nested CTE)
, CTE_Customer_Rank AS
(
	SELECT 
		CustomerID,
		TotalSales,
	RANK() OVER (ORDER BY TotalSales DESC) AS CustomerRank
	FROM CTE_TOTAL_SALES
)

--Main Query
SELECT 
	c.CustomerID,
	c.FirstName,
	c.LastName,
	cts.TotalSales,
	clo.Last_Order,
	ccr.CustomerRank
FROM Sales.Customers c
LEFT JOIN CTE_TOTAL_SALES cts
ON cts.CustomerID = c.CustomerID
LEFT JOIN CTE_LAST_ORDER clo
ON clo.CustomerID = c.CustomerID
LEFT JOIN CTE_Customer_Rank ccr
ON ccr.CustomerID = c.CustomerID


--Recursive CTE
--Generate a Sequence of Numbers from 1 to 20

WITH Series AS (
	--Anchor Query
	SELECT
		1 AS MyNumber
		UNION ALL
	--Recursive Query
	SELECT 
		MyNumber + 1
	FROM Series
	WHERE MyNumber < 20
)

--Main Query
SELECT *
FROM Series

--Task: Show the employee hierarchy by displaying each employee's level within the organization

WITH CTE_Emp_Hierarchy AS
(
    -- Anchor Query
    SELECT
        EmployeeID,
        FirstName,
        ManagerID,
        1 AS Level
    FROM Sales.Employees
    WHERE ManagerID IS NULL

    UNION ALL

    -- Recursive Query
    SELECT
        e.EmployeeID,
        e.FirstName,
        e.ManagerID,
        Level + 1
    FROM Sales.Employees AS e
    INNER JOIN CTE_Emp_Hierarchy ceh
        ON e.ManagerID = ceh.EmployeeID
)

-- Main Query
SELECT *
FROM CTE_Emp_Hierarchy