DROP TABLE student;

CREATE TABLE student(
    student_id INT PRIMARY KEY,
    first_name VARCHAR(25) NOT NULL,
    last_name VARCHAR(25) NOT NULL,
    email VARCHAR(100),
    gpa VARCHAR(6) CONSTRAINT check_gpa CHECK (gpa >= 0.00 AND gpa <= 4.00) NOT NULL,
    enrollment_date DATE);

INSERT INTO student (student_id, first_name, last_name, email, gpa, enrollment_date) VALUES
(201, 'Maya', 'Patel', 'maya.patel@cs.example.edu', 3.92, '2020-08-24');

INSERT INTO student (student_id, first_name, last_name, email, gpa, enrollment_date) VALUES
(202, 'Ethan', 'Li', 'ethan.li@cs.example.edu', 3.40, '2021-01-11');

INSERT INTO student (student_id, first_name, last_name, email, gpa, enrollment_date) VALUES
(203, 'Priya', 'Nair', 'priya.nair@cs.example.edu', 3.78, '2019-09-03');

INSERT INTO student (student_id, first_name, last_name, email, gpa, enrollment_date) VALUES
(204, 'Lucas', 'Kim', 'lucas.kim@cs.example.edu', 2.95, '2022-06-01');

INSERT INTO student (student_id, first_name, last_name, email, gpa, enrollment_date) VALUES
(205, 'Sofia', 'Nguyen', 'sofia.nguyen@cs.example.edu', 3.60, '2021-08-30');

--q3
--SELECT * FROM student WHERE gpa > 3.50;

--q4
--SELECT * FROM student WHERE enrollment_date < '2021-01-01';

--q5
--SELECT * FROM student WHERE last_name LIKE '%Li';	

--q6
--SELECT COUNT(*) FROM student;

--q7
-- SELECT * FROM student WHERE email LIKE '%cs.example.edu%';