
USE company_db;
DROP TABLE employee_performance;

CREATE TABLE employees_performance(
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_name VARCHAR(100),
    department VARCHAR(50),
    performance_score INT
);

INSERT INTO employees_performance (emp_name, department, performance_score) VALUES
('Alice', 'Sales', 85),
('Bob', 'Sales', 92),
('Charlie', 'Sales', 88),
('David', 'HR', 75),
('Eva', 'HR', 82),
('Frank', 'IT', 95),
('Grace', 'IT', 91),
('Hannah', 'IT', 95);

SELECT * FROM employees_performance;

SELECT 
    emp_id,
    emp_name,
    department,
    performance_score,
    DENSE_RANK() OVER (
        PARTITION BY department 
        ORDER BY performance_score DESC
    ) AS dept_rank
FROM employees_performance
ORDER BY department, dept_rank;


