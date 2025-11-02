CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50),
     location VARCHAR(50)
   );
INSERT INTO departments (dept_id, dept_name, location) VALUES 
   (1, 'HR', 'Chennai'),
   (2, 'IT', 'Bengaluru'),
   (3, 'FINANCE', 'Hyderabad'),
   (4, 'MARKETING', 'Mumbai'),
   (5, 'SALES', 'Delhi');
   
   SELECT * FROM departments;
   CREATE TABLE employee1 (  
   emp_id INT PRIMARY KEY, name VARCHAR(50), age INT, gender CHAR(1), salary DECIMAL (10,2), dept_id INT,
   hire_date DATE, FOREIGN KEY (dept_id) REFERENCES departments(dept_id));
   
INSERT INTO employee1 (emp_id, name, age, gender, salary, dept_id, hire_date) VALUES
(101, 'Arjun', 28, 'M', 45000, 2, '2020-05-10'),
(102, 'Priya', 31, 'F', 52000, 1, '2019-03-15'),
(103, 'Karthik', 26, 'M', 40000, 2, '2021-07-22'),
(104, 'Divya', 29, 'F', 60000, 3, '2018-11-12'),
(105, 'Sneha', 33, 'M', 70000, 4, '2017-01-05'),  
(106, 'Ramesh', 35, 'M', 58000, 5, '2018-06-23'), 
(107, 'Harini', 30, 'F', 49000, 2, '2020-09-19'), 
(108, 'Dinesh', 24, 'M', 35000, 1, '2022-01-10'), 
(109, 'Anjali', 27, 'F', 38000, 5, '2021-12-05'),
(110, 'Rajesh', 40, 'M', 80000, 3, '2015-02-18');

SELECT * FROM employee1;

SELECT *
FROM employee1
WHERE age = (SELECT MIN(age) FROM employee1);

SELECT e.name, d.dept_name
FROM employee1 e
JOIN departments d
ON e.dept_id = d.dept_id;



SELECT dept_id, COUNT(*) AS employee_count
FROM employee1
GROUP BY dept_id
ORDER BY employee_count DESC;

SELECT d.dept_name, COUNT(*) AS employee_count
FROM employee1 e
INNER JOIN departments d
ON e.dept_id = d.dept_id
GROUP BY d.dept_name
ORDER BY employee_count DESC;

SELECT *
FROM employee1
WHERE gender = 'F'
  AND salary > 45000;




