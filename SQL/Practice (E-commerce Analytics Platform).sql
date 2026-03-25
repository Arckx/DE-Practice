--STEP 1: Create Schema (DDL)
CREATE DATABASE CommerceAnalytics
use CommerceAnalytics

CREATE TABLE Customers (
	customer_id INT PRIMARY KEY,
	name VARChAR(100),
	city VARCHAR(50),
	signup_date DATE
)

CREATE TABLE Products (
	product_id INT PRIMARY KEY,
	product_name VARCHAR(100),
	category VARCHAR(50),
	price DECIMAL(10,2)
)

CREATE TABLE Orders (
	order_id INT PRIMARY KEY,
	customer_id INT,
	order_date DATE,
	status VARCHAR(20),
	FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
)

CREATE TABLE Order_Items (
	order_item_id INT PRIMARY KEY,
	order_id INT,
	product_id INT,
	quantity INT,
	FOREIGN KEY (order_id) REFERENCES Orders(order_id),
	FOREIGN KEY (product_id) REFERENCES Products(product_id)
)

CREATE TABLE Payments (
	payment_id INT,
	order_id INT,
	payment_date DATE,
	amount DECIMAL(10,2),
	payment_method VARCHAR(20)
)

--STEP 2: Insert Data (DML)
INSERT INTO Customers VALUES
(1, 'Ahmed', 'Karachi', '2023-01-10'),
(2, 'Sara', 'Lahore', '2023-02-15'),
(3, 'Ali', 'Karachi', '2023-03-20'),
(4, 'John', 'Islamabad', '2023-04-25');

INSERT INTO Products VALUES
(101, 'Laptop', 'Electronics', 1000),
(102, 'Phone', 'Electronics', 500),
(103, 'Shoes', 'Fashion', 100),
(104, 'Watch', 'Fashion', 150);

INSERT INTO Orders VALUES
(1001, 1, '2023-06-01', 'Delivered'),
(1002, 1, '2023-06-05', 'Pending'),
(1003, 2, '2023-06-07', 'Delivered'),
(1004, 3, '2023-06-10', 'Delivered'),
(1005, 3, '2023-06-12', 'Cancelled');

INSERT INTO Order_Items VALUES
(1, 1001, 101, 1),
(2, 1001, 103, 2),
(3, 1002, 102, 1),
(4, 1003, 104, 3),
(5, 1004, 101, 1),
(6, 1004, 102, 2),
(7, 1005, 103, 1);

INSERT INTO Payments VALUES
(1, 1001, '2023-06-02', 1200, 'Card'),
(1, 1001, '2023-06-02', 1200, 'Card'),
(2, 1003, '2023-06-08', 450, 'Cash'),
(3, 1004, '2023-06-11', 2000, 'Card'),
(3, 1004, '2023-06-11', 2000, 'Card');


--STEP 3
--Task 1: Basic Exploration
--Get total number of customers, orders, and products
SELECT 
	COUNT(name) as TotalCustomers
FROM Customers

SELECT
	COUNT(order_id) as TotalOrders
FROM Orders

SELECT 
	COUNT(product_id) as TotalProducts
FROM Products

SELECT * FROM Orders

--Identify how many orders are in each status
SELECT
	status,
	COUNT(status) as TotalOrdersPresent
FROM Orders
GROUP BY status

--Task 2: Revenue Calculation
--Calculate total revenue per order
--Then total revenue per customer
SELECT * FROM Orders
SELECT * FROM Order_Items
SELECT * FROM Products

SELECT 
	*
FROM Orders o
LEFT JOIN Order_Items i
ON o.order_id = i.order_id
LEFT JOIN Products p
ON i.product_id = p.product_id

