use company

--Relational Schema
CREATE SCHEMA sales

CREATE TABLE sales.Customers (
	customer_id INT PRIMARY KEY,
	name VARCHAR(100),
	email VARCHAR(100),
	created_at DATE
)

CREATE TABLE sales.Products (
	product_id INT PRIMARY KEY,
	product_name VARCHAR(100),
	price DECIMAL(10,2)
)
