use dummy

CREATE TABLE worker (
    id INT,
    name VARCHAR(50),
    department VARCHAR(50),
    salary INT
);

INSERT INTO worker VALUES
(1, 'Ahmed', 'IT', 60000),
(2, 'Sara', 'IT', 75000),
(3, 'Ali', 'IT', 75000),
(4, 'Usman', 'HR', 50000),
(5, 'Hina', 'HR', 65000),
(6, 'Zara', 'HR', 70000),
(7, 'Bilal', 'Finance', 80000),
(8, 'Ayesha', 'Finance', 90000),
(9, 'Hamza', 'Finance', 85000);


CREATE TABLE sales (
    id INT,
    sale_date DATE,
    amount INT
);

INSERT INTO sales VALUES
(1, '2024-01-01', 100),
(2, '2024-01-02', 200),
(3, '2024-01-03', 150),
(4, '2024-01-04', 300),
(5, '2024-01-05', 250);

CREATE TABLE shipments (
    id INT,
    order_date DATE,
    amount INT
);

INSERT INTO shipments VALUES
(1, '2024-02-01', 500),
(2, '2024-02-02', 700),
(3, '2024-02-03', 650),
(4, '2024-02-04', 800),
(5, '2024-02-05', 750);

--Problem: Given a table employees(id, name, department, salary), rank employees within each department based on salary (highest first).
SELECT
    name,
    department,
    RANK() OVER(PARTITION BY department ORDER BY salary DESC) as dept_rank
FROM worker

--Problem: Return employees who have the second highest salary in each department.
SELECT * FROM (SELECT
    name,
    department,
    DENSE_RANK() OVER(PARTITION BY department ORDER BY salary DESC) as dept_rank
FROM worker) as sub
WHERE dept_rank = 2

--Problem: Given sales(date, amount), calculate a running total of sales ordered by date.
SELECT 
    sale_date,
    amount,
    SUM(amount) OVER(ORDER BY sale_date) as total_sales
FROM sales

--Problem: For table orders(id, order_date, amount), show each order along with the previous order’s amount.
SELECT
    *,
    LAG(amount) OVER(ORDER BY sale_date) as previous_amount
FROM sales

--Problem: Show each employee’s salary and how much it differs from the department average.
SELECT 
    *,
    salary - AVG(salary) OVER(PARTITION BY department) as salary_difference
FROM worker

--Problem: Create a stored procedure that takes a department name and returns all employees in that department.
CREATE PROCEDURE dept_employee 
@param1 varchar(50)
as
BEGIN
    SELECT *
    FROM worker
    WHERE department = @param1
END

EXEC dept_employee @param1 = 'Finance'

--Problem: Create a procedure to insert a new employee into employees.
CREATE PROCEDURE insert_employee
@param1 int,
@param2 varchar(60),
@param3 varchar(60),
@param4 int
as
BEGIN
    INSERT INTO worker  (id, name, department, salary)
    values
    (@param1, @param2, @param3, @param4)
END

EXEC insert_employee @param1=1, @param2= 'Sophia', @param3 = 'IT', @param4 = 95000

