CREATE TABLE employee_performance (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    performance_score DECIMAL(5,2)
);
INSERT INTO employee_performance (emp_id, emp_name, performance_score) VALUES
(1, 'Alice', 85.5),
(2, 'Bob', 78.0),
(3, 'Charlie', 92.0),
(4, 'David', 88.5),
(5, 'Emma', 75.0);

SELECT * FROM employee_performance;

SELECT emp_name, performance_score
FROM employee_performance
WHERE performance_score > (
    SELECT AVG(performance_score)
    FROM employee_performance
);
