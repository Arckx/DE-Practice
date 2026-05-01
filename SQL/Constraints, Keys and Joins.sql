use company

CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    city VARCHAR(50),
    created_at DATE DEFAULT GETDATE()
);

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE NOT NULL,
    total_amount DECIMAL(10,2) CHECK (total_amount > 0),
    status VARCHAR(20) DEFAULT 'Pending',

    CONSTRAINT fk_customer
        FOREIGN KEY (customer_id)
        REFERENCES Customers(customer_id)
        ON DELETE CASCADE
);

INSERT INTO Customers (customer_id, first_name, last_name, email, city, created_at) VALUES
(1,'Ahmed','Khan','user1@gmail.com','Karachi','2025-01-01'),
(2,'Sara','Ali','user2@gmail.com','Lahore','2025-01-02'),
(3,'Bilal','Hussain','user3@gmail.com','Islamabad','2025-01-03'),
(4,'Ayesha','Malik','user4@gmail.com','Karachi','2025-01-04'),
(5,'Usman',NULL,'user5@gmail.com',NULL,'2025-01-05'),
(6,'Hina','Qureshi','user6@gmail.com','Islamabad','2025-01-06'),
(7,'Zain','Shah','user7@gmail.com','Karachi','2025-01-07'),
(8,'Fatima','Noor','user8@gmail.com',NULL,'2025-01-08'),
(9,'Omar','Farooq','user9@gmail.com','Islamabad','2025-01-09'),
(10,'Ali',NULL,'user10@gmail.com','Lahore','2025-01-10'),
(11,'Mariam','Akram','user11@gmail.com','Karachi','2025-01-11'),
(12,'Hassan','Iqbal','user12@gmail.com','Lahore','2025-01-12'),
(13,'Tariq','Naeem','user13@gmail.com','Islamabad','2025-01-13'),
(14,'Areeba','Khan','user14@gmail.com','Karachi','2025-01-14'),
(15,'Hamza',NULL,'user15@gmail.com','Lahore','2025-01-15'),
(16,'Nida','Yousaf','user16@gmail.com',NULL,'2025-01-16'),
(17,'Imran','Javed','user17@gmail.com','Karachi','2025-01-17'),
(18,'Sana','Rashid','user18@gmail.com','Lahore','2025-01-18'),
(19,'Saad','Mansoor','user19@gmail.com','Islamabad','2025-01-19'),
(20,'Kiran',NULL,'user20@gmail.com',NULL,'2025-01-20'),
(21,'Asad','Rehman','user21@gmail.com','Karachi','2025-01-21'),
(22,'Bushra','Tariq','user22@gmail.com','Lahore','2025-01-22'),
(23,'Danish','Mehmood','user23@gmail.com','Islamabad','2025-01-23'),
(24,'Laiba','Rauf','user24@gmail.com','Karachi','2025-01-24'),
(25,'Farhan',NULL,'user25@gmail.com','Lahore','2025-01-25'),
(26,'Zoya','Anwar','user26@gmail.com','Islamabad','2025-01-26'),
(27,'Arslan','Ashraf','user27@gmail.com','Karachi','2025-01-27'),
(28,'Iqra','Saleem','user28@gmail.com',NULL,'2025-01-28'),
(29,'Yasir','Latif','user29@gmail.com','Islamabad','2025-01-29'),
(30,'Noor',NULL,'user30@gmail.com','Karachi','2025-01-30'),
(31,'Fahad','Chaudhry','user31@gmail.com','Lahore','2025-02-01'),
(32,'Mehwish','Abbasi','user32@gmail.com','Islamabad','2025-02-02'),
(33,'Talha','Arif','user33@gmail.com','Karachi','2025-02-03'),
(34,'Hafsa','Sheikh','user34@gmail.com',NULL,'2025-02-04'),
(35,'Rizwan',NULL,'user35@gmail.com','Lahore','2025-02-05'),
(36,'Anum','Zafar','user36@gmail.com','Islamabad','2025-02-06'),
(37,'Adnan','Bhatti','user37@gmail.com','Karachi','2025-02-07'),
(38,'Eman','Waqar','user38@gmail.com','Lahore','2025-02-08'),
(39,'Shayan','Rafi','user39@gmail.com','Islamabad','2025-02-09'),
(40,'Aiman',NULL,'user40@gmail.com',NULL,'2025-02-10'),
(41,'Kamran','Asif','user41@gmail.com','Karachi','2025-02-11'),
(42,'Mahnoor','Kamal','user42@gmail.com','Lahore','2025-02-12'),
(43,'Waqas','Munir','user43@gmail.com','Islamabad','2025-02-13'),
(44,'Sadia','Khalid','user44@gmail.com','Karachi','2025-02-14'),
(45,'Junaid',NULL,'user45@gmail.com','Lahore','2025-02-15'),
(46,'Rimsha','Noman','user46@gmail.com','Islamabad','2025-02-16'),
(47,'Adeel','Sohail','user47@gmail.com','Karachi','2025-02-17'),
(48,'Hoor','Yasin','user48@gmail.com',NULL,'2025-02-18'),
(49,'Dua','Zaman','user49@gmail.com','Islamabad','2025-02-19'),
(50,'Umer',NULL,'user50@gmail.com','Karachi','2025-02-20'),
(51,'Zubair','Rana','user51@gmail.com','Lahore','2025-02-21'),
(52,'Alina','Faisal','user52@gmail.com','Islamabad','2025-02-22'),
(53,'Shahzaib','Mirza','user53@gmail.com','Karachi','2025-02-23'),
(54,'Minal','Irfan','user54@gmail.com','Lahore','2025-02-24'),
(55,'Haris',NULL,'user55@gmail.com','Islamabad','2025-02-25'),
(56,'Kinza','Aftab','user56@gmail.com','Karachi','2025-02-26'),
(57,'Rehan','Sabir','user57@gmail.com','Lahore','2025-02-27'),
(58,'Samiya','Arshad','user58@gmail.com','Islamabad','2025-02-28'),
(59,'Ahsan','Nawaz','user59@gmail.com','Karachi','2025-03-01'),
(60,'Sehrish',NULL,'user60@gmail.com',NULL,'2025-03-02'),
(61,'Mubashir','Qasim','user61@gmail.com','Lahore','2025-03-03'),
(62,'Rida','Usman','user62@gmail.com','Islamabad','2025-03-04'),
(63,'Zeeshan','Bilal','user63@gmail.com','Karachi','2025-03-05'),
(64,'Areej','Shahid','user64@gmail.com','Lahore','2025-03-06'),
(65,'Saif',NULL,'user65@gmail.com','Islamabad','2025-03-07'),
(66,'Huda','Aamir','user66@gmail.com','Karachi','2025-03-08'),
(67,'Murtaza','Hanif','user67@gmail.com','Lahore','2025-03-09'),
(68,'Sidra','Ilyas','user68@gmail.com','Islamabad','2025-03-10'),
(69,'Rayan','Bashir','user69@gmail.com','Karachi','2025-03-11'),
(70,'Anaya',NULL,'user70@gmail.com','Lahore','2025-03-12'),
(71,'Ibrahim','Zubair','user71@gmail.com','Islamabad','2025-03-13'),
(72,'Fiza','Sameer','user72@gmail.com','Karachi','2025-03-14'),
(73,'Sheryar','Faisal','user73@gmail.com','Lahore','2025-03-15'),
(74,'Hania','Shoukat','user74@gmail.com','Islamabad','2025-03-16'),
(75,'Zarar',NULL,'user75@gmail.com','Karachi','2025-03-17'),
(76,'Nawal','Khan','user76@gmail.com','Lahore','2025-03-18'),
(77,'Rameez','Afzal','user77@gmail.com','Islamabad','2025-03-19'),
(78,'Maha','Arif','user78@gmail.com','Karachi','2025-03-20'),
(79,'Huzaifa','Majid','user79@gmail.com','Lahore','2025-03-21'),
(80,'Aiza',NULL,'user80@gmail.com',NULL,'2025-03-22'),
(81,'Faizan','Rasheed','user81@gmail.com','Islamabad','2025-03-23'),
(82,'Tania','Shabbir','user82@gmail.com','Karachi','2025-03-24'),
(83,'Owais','Azhar','user83@gmail.com','Lahore','2025-03-25'),
(84,'Nimra','Imtiaz','user84@gmail.com','Islamabad','2025-03-26'),
(85,'Hashir',NULL,'user85@gmail.com','Karachi','2025-03-27'),
(86,'Hiba','Zahid','user86@gmail.com','Lahore','2025-03-28'),
(87,'Daniyal','Tufail','user87@gmail.com','Islamabad','2025-03-29'),
(88,'Momina','Haroon','user88@gmail.com','Karachi','2025-03-30'),
(89,'Rafay','Idrees','user89@gmail.com','Lahore','2025-03-31'),
(90,'Mehak',NULL,'user90@gmail.com','Islamabad','2025-04-01'),
(91,'Zainab','Junaid','user91@gmail.com','Karachi','2025-04-02'),
(92,'Yahya','Waseem','user92@gmail.com','Lahore','2025-04-03'),
(93,'Laiba','Furqan','user93@gmail.com','Islamabad','2025-04-04'),
(94,'Hamid','Rauf','user94@gmail.com','Karachi','2025-04-05'),
(95,'Sumbul',NULL,'user95@gmail.com','Lahore','2025-04-06'),
(96,'Talal','Yaqoob','user96@gmail.com','Islamabad','2025-04-07'),
(97,'Anas','Kamran','user97@gmail.com','Karachi','2025-04-08'),
(98,'Aleena','Rizvi','user98@gmail.com','Lahore','2025-04-09'),
(99,'Taimoor','Ejaz','user99@gmail.com','Islamabad','2025-04-10'),
(100,'Iqbal',NULL,'user100@gmail.com',NULL,'2025-04-11');

INSERT INTO Orders (order_id, customer_id, order_date, total_amount, status) VALUES
(21,21,'2025-05-21',1350.00,'Pending'),
(22,22,'2025-05-22',2890.50,'Completed'),
(23,23,'2025-05-23',760.75,'Cancelled'),
(24,24,'2025-05-24',4500.00,'Completed'),
(25,25,'2025-05-25',980.00,NULL),
(26,26,'2025-05-26',3100.40,'Pending'),
(27,27,'2025-05-27',2750.00,'Completed'),
(28,28,'2025-05-28',640.00,'Cancelled'),
(29,29,'2025-05-29',8900.00,'Completed'),
(30,30,'2025-05-30',1200.00,NULL),
(31,31,'2025-05-31',2100.00,'Pending'),
(32,32,'2025-06-01',3300.00,'Completed'),
(33,33,'2025-06-02',1450.00,'Cancelled'),
(34,34,'2025-06-03',780.00,'Completed'),
(35,35,'2025-06-04',920.00,NULL),
(36,36,'2025-06-05',5000.00,'Pending'),
(37,37,'2025-06-06',6150.00,'Completed'),
(38,38,'2025-06-07',880.00,'Cancelled'),
(39,39,'2025-06-08',1340.00,'Completed'),
(40,40,'2025-06-09',760.00,NULL),
(41,41,'2025-06-10',210.00,'Pending'),
(42,42,'2025-06-11',320.00,'Completed'),
(43,43,'2025-06-12',430.00,'Cancelled'),
(44,44,'2025-06-13',540.00,'Completed'),
(45,45,'2025-06-14',650.00,NULL),
(46,46,'2025-06-15',7600.00,'Pending'),
(47,47,'2025-06-16',8700.00,'Completed'),
(48,48,'2025-06-17',980.00,'Cancelled'),
(49,49,'2025-06-18',1090.00,'Completed'),
(50,50,'2025-06-19',2100.00,NULL),
(51,51,'2025-06-20',3200.00,'Pending'),
(52,52,'2025-06-21',4300.00,'Completed'),
(53,53,'2025-06-22',5400.00,'Cancelled'),
(54,54,'2025-06-23',6500.00,'Completed'),
(55,55,'2025-06-24',7600.00,NULL),
(56,56,'2025-06-25',870.00,'Pending'),
(57,57,'2025-06-26',980.00,'Completed'),
(58,58,'2025-06-27',1090.00,'Cancelled'),
(59,59,'2025-06-28',1200.00,'Completed'),
(60,60,'2025-06-29',1300.00,NULL),
(61,61,'2025-06-30',1400.00,'Pending'),
(62,62,'2025-07-01',1500.00,'Completed'),
(63,63,'2025-07-02',1600.00,'Cancelled'),
(64,64,'2025-07-03',1700.00,'Completed'),
(65,65,'2025-07-04',1800.00,NULL),
(66,66,'2025-07-05',1900.00,'Pending'),
(67,67,'2025-07-06',2000.00,'Completed'),
(68,68,'2025-07-07',2100.00,'Cancelled'),
(69,69,'2025-07-08',2200.00,'Completed'),
(70,70,'2025-07-09',2300.00,NULL),
(71,71,'2025-07-10',2400.00,'Pending'),
(72,72,'2025-07-11',2500.00,'Completed'),
(73,73,'2025-07-12',2600.00,'Cancelled'),
(74,74,'2025-07-13',2700.00,'Completed'),
(75,75,'2025-07-14',2800.00,NULL),
(76,76,'2025-07-15',2900.00,'Pending'),
(77,77,'2025-07-16',3000.00,'Completed'),
(78,78,'2025-07-17',3100.00,'Cancelled'),
(79,79,'2025-07-18',3200.00,'Completed'),
(80,80,'2025-07-19',3300.00,NULL),
(81,81,'2025-07-20',3400.00,'Pending'),
(82,82,'2025-07-21',3500.00,'Completed'),
(83,83,'2025-07-22',3600.00,'Cancelled'),
(84,84,'2025-07-23',3700.00,'Completed'),
(85,85,'2025-07-24',3800.00,NULL),
(86,86,'2025-07-25',3900.00,'Pending'),
(87,87,'2025-07-26',4000.00,'Completed'),
(88,88,'2025-07-27',4100.00,'Cancelled'),
(89,89,'2025-07-28',4200.00,'Completed'),
(90,90,'2025-07-29',4300.00,NULL),
(91,91,'2025-07-30',4400.00,'Pending'),
(92,92,'2025-07-31',4500.00,'Completed'),
(93,93,'2025-08-01',4600.00,'Cancelled'),
(94,94,'2025-08-02',4700.00,'Completed'),
(95,95,'2025-08-03',4800.00,NULL),
(96,96,'2025-08-04',4900.00,'Pending'),
(97,97,'2025-08-05',5000.00,'Completed'),
(98,98,'2025-08-06',5100.00,'Cancelled'),
(99,99,'2025-08-07',5200.00,'Completed'),
(100,100,'2025-08-08',5300.00,'Pending');


SELECT * FROM Customers

SELECT * FROM Orders


--Joins

--INNER Join
SELECT * 
FROM customers as c
INNER JOIN orders as o
ON c.customer_id = o.customer_id

--LEFT Join
SELECT * 
FROM customers as c
LEFT JOIN orders as o
ON c.customer_id = o.customer_id

--LEFT OUTER Join
SELECT * 
FROM customers as c
LEFT OUTER JOIN orders as o
ON c.customer_id = o.customer_id

--RIGHT Join
SELECT * 
FROM customers as c
RIGHT JOIN orders as o
ON c.customer_id = o.customer_id

--FULL Join
SELECT * 
FROM customers as c
FULL JOIN orders as o
ON c.customer_id = o.customer_id

