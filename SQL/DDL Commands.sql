create database company;

use company;

CREATE TABLE persons (
	id INT NOT NULL,
	person_name VARCHAR(50) NOT NULL,
	birth_date DATE,
	phone VARCHAR(15) NOT NULL,
	CONSTRAINT pk_persons PRIMARY KEY (id)
)

INSERT INTO persons
(id, person_name, birth_date, mobile_number)
VALUES
(1,  'Ahmed Khan',     '1995-03-12', '03011234567'),
(2,  'Sara Ali',       '1998-07-25', '03021234567'),
(3,  'Usman Raza',     '1992-11-08', '03031234567'),
(4,  'Ayesha Malik',   '1996-01-19', '03041234567'),
(5,  'Bilal Hussain',  '1990-09-03', '03051234567'),
(6,  'Hina Shah',      '1997-05-14', '03061234567'),
(7,  'Fahad Iqbal',    '1993-12-22', '03071234567'),
(8,  'Zara Naeem',     '1999-08-30', '03081234567'),
(9,  'Hamza Sheikh',   '1994-02-17', '03091234567'),
(10, 'Nida Farooq',    '1991-06-05', '03101234567'),
(11, 'Ali Javed',      '1989-10-11', '03111234567'),
(12, 'Maryam Siddiqi','1996-04-27', '03121234567'),
(13, 'Imran Akhtar',   '1992-01-09', '03131234567'),
(14, 'Sana Qureshi',   '1998-09-18', '03141234567'),
(15, 'Adnan Latif',    '1987-12-01', '03151234567');

SELECT * FROM persons

ALTER TABLE persons
ADD email VARCHAR(50)

ALTER TABLE persons
DROP COLUMN email

EXEC sp_rename
'persons.phone',
'mobile_number',
'COLUMN';

ALTER TABLE persons
ALTER COLUMN person_name CHAR(50) NOT NULL;

ALTER TABLE persons
ADD email VARCHAR(50) NULL

ALTER TABLE persons
ALTER COLUMN email INT

DROP DATABASE companies

DROP TABLE person

ALTER TABLE persons
DROP COLUMN email

TRUNCATE TABLE persons

--Create a Table
CREATE TABLE patient (
	id INT PRIMARY KEY,
	patient_name VARCHAR(50) NOT NULL,
	dept VARCHAR(50) NOT NULL,
	phone INT NOT NULL
)

--Add a New Column
ALTER TABLE patient
ADD email VARCHAR(50)

--Modify a Column's Data Type
ALTER TABLE patient
ALTER COLUMN email VARCHAR(50)

--Drop a Column
ALTER TABLE patient
DROP COLUMN email

ALTER TABLE patient
ADD age INT NOT NULL

--Add a Unique Constraint
ALTER TABLE patient
ADD CONSTRAINT pt_name UNIQUE (patient_name)

--Drop a Table
DROP TABLE patient

--Truncate a Table
TRUNCATE TABLE patient

--Set a Default Value
ALTER TABLE patient
ADD fees INT NOT NULL

ALTER TABLE patient
ADD DEFAULT fees


SELECT * from patient

--DML

--INSERT Command (2nd method)
--This method is used to copydata from one table to another
INSERT INTO table_name (column 1, column 2) --Select data from target table
SELECT columns FROM table_name --Select data from source table

--UPDATE Command
UPDATE table_name
SET column_name = 'something'
WHERE condition

--DELETE Command
DELETE FROM table_name --only using delete command will empty the table
WHERE condition 

--DELETE vs TRUNCATE
--DELETE would take time to empty the table due to background checks
--Truncate empties the table without any checks