CREATE database dummy
use dummy

CREATE TABLE customers (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    email VARCHAR(100)
);

CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    salary DECIMAL(10,2),
    department_id INT,
    manager_id INT
);

CREATE TABLE departments (
    id INT PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE orders (
    id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    amount DECIMAL(10,2)
);

CREATE TABLE products (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    price DECIMAL(10,2)
);

CREATE TABLE order_items (
    id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT
);

INSERT INTO customers VALUES
(1, 'Ali', 25, 'ali@email.com'),
(2, 'Sara', 30, 'sara@email.com'),
(3, 'Ahmed', 35, 'ahmed@email.com'),
(4, 'Ayesha', 28, 'ayesha@email.com'),
(5, 'Bilal', 40, 'bilal@email.com'),
(6, 'Zara', 30, 'sara@email.com'); -- duplicate email

INSERT INTO departments VALUES
(1, 'IT'),
(2, 'HR'),
(3, 'Finance');

INSERT INTO employees VALUES
(1, 'John', 50000, 1, NULL),
(2, 'Jane', 60000, 1, 1),
(3, 'Mark', 55000, 2, 1),
(4, 'Luke', 70000, 3, 1),
(5, 'Paul', 65000, 3, 4),
(6, 'Anna', 48000, 2, 3);

INSERT INTO orders VALUES
(1, 1, '2024-01-01', 200),
(2, 1, '2024-01-10', 300),
(3, 2, '2024-02-01', 150),
(4, 3, '2024-02-15', 400),
(5, 3, '2024-03-01', 100),
(6, 4, '2024-03-10', 250);

INSERT INTO products VALUES
(1, 'Laptop', 1000),
(2, 'Phone', 500),
(3, 'Tablet', 300),
(4, 'Headphones', 100);

INSERT INTO order_items VALUES
(1, 1, 1, 1),
(2, 1, 4, 2),
(3, 2, 2, 1),
(4, 3, 3, 1),
(5, 4, 1, 1),
(6, 5, 4, 3);

--Beginner Level
--Find all customers whose age is greater than the average age of all customers.

SELECT * FROM customers

SELECT name, age
FROM customers
WHERE age >
(SELECT AVG(age)
FROM customers)

--Find the employee(s) who have the highest salary.

SELECT * FROM employees

SELECT name, salary
FROM employees
WHERE salary > (
                SELECT AVG(salary)
                FROM employees
)

--Find orders where the order amount is greater than that customer’s average order amount.

SELECT * FROM orders

SELECT id, amount
FROM orders
WHERE amount > (SELECT AVG(amount) FROM orders)

--Using a CTE, count how many employees are in each department.

SELECT * FROM employees

WITH employee as (
SELECT * FROM employees)
SELECT department_id, count(department_id) as total_employees
FROM employee
GROUP BY department_id

--Intermediate Level
--Find the second highest salary from the employees table.

SELECT * from employees

SELECT name, salary
FROM employees
WHERE salary = (SELECT MAX(salary)
                FROM employees
                WHERE salary < (SELECT MAX(salary) FROM Employees)
                )

--Find customers who have never placed an order.
SELECT * FROM customers
SELECT * FROM orders

SELECT id 
FROM customers c
WHERE NOT EXISTS (SELECT customer_id from orders o WHERE c.id = o.customer_id)

--Calculate running total of sales ordered by date.
SELECT * FROM orders

WITH running_total_sales as (
    SELECT 
        order_date, 
        amount,
        SUM(amount) OVER(ORDER BY order_date) as total_amount
    FROM orders
)
SELECT * FROM running_total_sales

--Find the department with the highest average salary.
SELECT * FROM employees



WITH avg_salary as (
    SELECT department_id, AVG(salary) as dept_avg_salary
    FROM employees
    GROUP BY department_id
)
SELECT TOP 1
    department_id,
    dept_avg_salary
FROM avg_salary
ORDER BY dept_avg_salary DESC;

--Upper Intermediate
--Find employees whose salary is higher than the average salary of their department.
SELECT * FROM employees

