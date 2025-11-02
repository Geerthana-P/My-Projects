USE company_db;

DROP TABLE employees;

CREATE TABLE employees (  
   emp_id INT PRIMARY KEY, name VARCHAR(50), salary DECIMAL (10,2), dept_id INT);
   
   INSERT INTO employees (emp_id, name, salary, dept_id) VALUES
(101, 'Arjun', 45000, 2),
(102, 'Priya', 52000, 1),
(103, 'Karthik', 40000, 2),
(104, 'Divya', 60000, 3),
(105, 'Sneha', 70000, 4);

SELECT * FROM departments;
SELECT e.name, d.dept_name
FROM employees e
INNER JOIN departments d ON e.dept_id = d.dept_id;

SELECT d.dept_name, e.name
FROM departments d
LEFT JOIN employees e ON d.dept_id = e.dept_id;

SELECT d.dept_name, AVG(e.salary) AS avg_salary
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
GROUP BY d.dept_name;
