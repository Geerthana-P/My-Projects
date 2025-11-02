CREATE TABLE sales (
    order_id INT PRIMARY KEY,
    product VARCHAR(100),
    quantity INT,
    price DECIMAL(10,2),
    region VARCHAR(50)
);

INSERT INTO sales (order_id, product, quantity, price, region) VALUES
(1, 'Laptop', 10, 1200.00, 'East'),
(2, 'Monitor', 6, 300.00, 'East'),
(3, 'Mouse', 15, 25.00, 'West'),
(4, 'Keyboard', 8, 50.00, 'North'),
(5, 'Laptop', 5, 1150.00, 'South');

SELECT * FROM sales;
SELECT SUM(quantity * price) AS total_revenue
FROM sales;
SELECT *
FROM sales
WHERE region = 'East' AND quantity > 5
ORDER BY price DESC;
SELECT product, AVG(price) FROM sales GROUP BY product;

