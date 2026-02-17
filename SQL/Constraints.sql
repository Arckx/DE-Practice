create database retail_db

use retail_db

CREATE TABLE orders (
	order_id int,
	order_item_id int,
	order_date date,
	customer_id int,
	order_status varchar(20),
	product_id int,
	quantity int,
	product_price float,
	total_price float
)

--Creating CHECK COnstraint
ALTER Table orders
ADD CONSTRAINT CHK_OrderStatus CHECK (order_status in ('CLOSED', 
'PENDING_PAYMENT',
'COMPLETE',
'PROCESSING',
'ON_HOLD',
'SUSPECTED_FRAUD',
'PENDING'))

EXEC sp_helpconstraint  'orders'

--Deleting a Constraint
ALTER TABLE orders
DROP CONSTRAINT CHK_OrderStatus

--Creating NOT NULL Constraint
CREATE TABLE colleges (
	college_id INT NOT NULL,
	college_code VARCHAR(20) NOT NULL,
	college_name VARCHAR(50)
)

--Creating UNIQUE Constraint
CREATE TABLE colleges (
	college_id INT NOT NULL UNIQUE,
	college_code VARCHAR(20) UNIQUE,
	college_name VARCHAR(50)
)

--Creating Primary Key Constraint
CREATE TABLE colleges (
	college_id INT PRIMARY KEY,
	college_code VARCHAR(20) NOT NULL,
	college_name VARCHAR(50)
)

--Creating Foreign Key Constraint
CREATE TABLE orders (
	order_id INT PRIMARY KEY,
	customer_id INT REFERENCES Table_Name(column_name)
)

--Creating Default Constraint
CREATE TABLE colleges (
	college_id INT PRIMARY KEY,
	college_code VARCHAR(20),
	college_country VARCHAR(20) DEFAULT 'US'
)

--Creating INDEX Constraint
CREATE TABLE colleges (
	college_id INT PRIMARY KEY,
	college_code VARCHAR(20) NOT NULL,
	college_name VARCHAR(50)
)

CREATE INDEX college_index
ON colleges(college_code)

-- create unique index
CREATE UNIQUE INDEX college_index
ON Colleges(college_code);