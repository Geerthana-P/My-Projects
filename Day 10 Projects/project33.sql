CREATE DATABASE company_db;
USE company_db;
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100),
    salary DECIMAL(10,2)
);
INSERT INTO employees (id, name, department, salary) VALUES (1, 'Alice',
'Engineering', 70000);
INSERT INTO employees (id, name, department, salary) VALUES (2, 'Bob',
'Marketing', 60000);
SELECT * FROM employees;
UPDATE employees
SET salary = 75000
WHERE id = 1;
SELECT * FROM employees;

SET SQL_SAFE_UPDATES = 0;

DELETE FROM employees
WHERE name = 'Bob';
SELECT * FROM employees;



