USE company_db;

SELECT * FROM orders;

DROP TABLE orders;
CREATE TABLE orders (
    order_id INT,
    customer_id INT,
    order_date DATE
);
INSERT INTO orders (order_id, customer_id, order_date)
VALUES
(1, 101, '2025-01-01'),
(2, 101, '2025-01-15'),
(3, 101, '2025-03-10'),
(4, 102, '2025-01-05'),
(5, 102, '2025-01-20'),
(6, 102, '2025-04-25'),
(7, 103, '2025-02-10'),
(8, 103, '2025-02-12');

SELECT * FROM orders;

SELECT 
    customer_id,
    order_id,
    order_date,
    LAG(order_date) OVER (PARTITION BY customer_id ORDER BY order_date) AS previous_order_date,
    DATEDIFF(order_date, LAG(order_date) OVER (PARTITION BY customer_id ORDER BY order_date)) AS days_gap
FROM (
    SELECT 
        customer_id,
        order_id,
        order_date
    FROM orders
) AS t;



