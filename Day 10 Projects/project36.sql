CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    customer_name VARCHAR(100),
    amount DECIMAL(10,2)
);
INSERT INTO orders (order_id, customer_id, customer_name, amount) VALUES
(1, 101, 'Alice', 1200.00),
(2, 102, 'Bob', 600.00),
(3, 101, 'Alice', 800.00),
(4, 103, 'Carol', 1500.00),
(5, 104, 'Dave', 700.00),
(6, 105, 'Eve', 900.00),
(7, 102, 'Bob', 400.00),
(8, 103, 'Carol', 500.00);

SELECT * FROM orders;

SELECT customer_id, customer_name, SUM(amount) AS total_spending
FROM orders
GROUP BY customer_id, customer_name
ORDER BY total_spending DESC
LIMIT 5;
