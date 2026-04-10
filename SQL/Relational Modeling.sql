use company

--Step 1: Tables (Relational Design)
-- students → stores student data
-- courses → stores course data
-- enrollments → connects students and courses

--Step 2: SQL Implementation
CREATE TABLE students (
	student_id INT PRIMARY KEY,
	name VARCHAR(100),
	email VARCHAR(100) UNIQUE
)

CREATE TABLE courses (
	course_id INT PRIMARY KEY,
	title VARCHAR(100)
)

CREATE TABLE enrollments (
	enrollment_id INT PRIMARY KEY,
	student_id INT,
	course_id INT,
	enrollemnt_date DATE,
	FOREIGN KEY (student_id) REFERENCES students(student_id),
	FOREIGN KEY (course_id) REFERENCES courses(course_id)
)

--Step 3: Insert Sample Data
INSERT INTO students VALUES (1, 'Ahmed', 'ahmed@email.com');
INSERT INTO students VALUES (2, 'Ali', 'ali@email.com');

INSERT INTO courses VALUES (101, 'SQL Basics');
INSERT INTO courses VALUES (102, 'Data Engineering');

INSERT INTO enrollments VALUES (1, 1, 101, '2026-04-01');
INSERT INTO enrollments VALUES (2, 1, 102, '2026-04-02');
INSERT INTO enrollments VALUES (3, 2, 101, '2026-04-03');

--Step 4: Query
SELECT s.name, c.title
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
JOIN courses c ON e.course_id = c.course_id;

