--DDL problems

use company

CREATE TABLE Departments (
	dept_id INT PRIMARY KEY,
	dept_name VARCHAR(50)
)

CREATE TABLE Employees (
	emp_id INT PRIMARY KEY,
	emp_name VARCHAR(50),
	salary INT,
	dept_id INT,
	joining_date DATE,
	FOREIGN KEY (dept_id) REFERENCES Departments(dept_id)
)

INSERT INTO Departments VALUES
(1, 'HR'),
(2, 'IT'),
(3, 'Finance')

INSERT INTO Employees VALUES
(101, 'Ali', 50000, 2, '2022-01-10'),
(102, 'Sara', 60000, 2, '2021-06-15'),
(103, 'Ahmed', 45000, 1, '2023-03-01'),
(104, 'Zara', 70000, 3, '2020-09-20'),
(105, 'Usman', 40000, 1, '2024-01-05');

UPDATE Employees
SET email = LOWER(full_name) + '@company.com'
WHERE email IS NULL;


SELECT * FROM Employees
SELECT * FROM Staff

--Add a column email of type VARCHAR(100)
ALTER TABLE Employees
ADD email VARCHAR(100)

--Add a column status with default value 'Active'
ALTER TABLE Employees
ADD status VARCHAR(15) DEFAULT 'Active'

--Change salary column data type from INT to DECIMAL(10,2)
ALTER TABLE Employees
ALTER COLUMN salary DECIMAL(10, 2)

EXEC sp_rename
'employees.emp_name',
'full_name',
'COLUMN'

--Drop the column joining_date
ALTER TABLE Employees
DROP COLUMN joining_date

--Rename the table Employees to Staff
EXEC sp_rename
'Staff',
'Employees'


--Add a UNIQUE constraint on email
ALTER TABLE Staff
ADD CONSTRAINT emp_email UNIQUE (email)

--Drop the UNIQUE constraint from email
ALTER TABLE Staff
DROP CONSTRAINT emp_email 

--Truncate the table
TRUNCATE TABLE Staff

--Drop the table completely
DROP TABLE Staff

--DML Problems
SELECT * FROM Employees
--Insert a new employee record
INSERT INTO Employees
(emp_id, full_name, salary, dept_id, email, status)
VALUES
(106, 'Aliyan', '80000', 3, 'aliyan@gmail.com', 'Active')

--Insert multiple employee records in a single statement

--Update salary of employee with emp_id = 3 to 48,000
UPDATE Employees
SET salary = 48000
WHERE emp_id = 103

--Update department to 'Admin' where department is 'HR'
UPDATE Departments
SET dept_name = 'Admin'
WHERE dept_name = 'HR'

SELECT * FROM Departments
--Increase salary by 10% for all IT employees
UPDATE Employees
SET salary = salary + salary*0.1
WHERE dept_id = 2

--Delete employee with emp_id = 4
DELETE Employees
WHERE emp_id = 104

--Delete employees whose salary is below 45,000
DELETE Employees
WHERE salary < 45000

--Set department to 'Unassigned' where department is NULL
UPDATE Departments
SET dept_name = 'Unassigned'
WHERE dept_name is NULL

--Delete all records without dropping the table
DELETE Employees

--Insert a record but omit the salary column (use default value)
