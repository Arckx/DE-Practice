use SalesDB

/* FInd the total sales for each product
Additonally provide details such as order id, order date */

SELECT
	OrderID,
	OrderDate,
	ProductID,
	SUM(Sales) 
		OVER
			(PARTITION BY ProductID) TotalSalesByProducts
FROM Sales.Orders


/* Problem 2 */
--Find the total sales across all orders
--Find the total sales for each product
--Find the total sales for each combination of product and order status
--Additionally provide details such as order id, order date

SELECT
	OrderID,
	OrderDate,
	ProductID,
	OrderStatus,
	Sales,
	SUM(Sales) OVER () TotalSales,
	SUM(Sales) OVER (PARTITION BY ProductID) SalesByProducts,
	SUM(Sales) OVER (PARTitiON BY ProductID, OrderStatus) SalesByProductAndStatus
FROM Sales.Orders


/* Problem 3 */

--Rank each order based on their sales from highest to lowest
--Additionally provide details such as order id, order date

SELECT
	OrderID,
	OrderDate,
	Sales,
	RANK() OVER (ORDER BY Sales DESC) RankSales
FROM Sales.Orders


--Using Window Function on ORDER BY Clause

SELECT
	OrderID,
	OrderDate,
	ProductID,
	SUM(Sales) 
		OVER
			(PARTITION BY ProductID) TotalSalesByProducts
FROM Sales.Orders
ORDER BY SUM(Sales) OVER (PARTITION BY OrderStatus)

--Using WIndow Function with GROUP BY
--Rank Customers based on their total sales

SELECT
	CustomerID,
	SUM(Sales) TotalSales,
	RANK() OVER (ORDER BY SUM(Sales) DESC) RankCustomers
FROM Sales.Orders
GROUP BY CustomerID