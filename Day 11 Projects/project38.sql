
DROP TABLE orders;

-- Create the orders table
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE
);

-- Create the ratings table
CREATE TABLE ratings (
    rating_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    rating INT
);


-- Insert sample data into orders table
INSERT INTO orders (order_id, customer_id, order_date) VALUES
(1, 101, '2025-01-05'),
(2, 102, '2025-01-10'),
(3, 103, '2025-01-15'),
(4, 104, '2025-01-20'),
(5, 105, '2025-01-25');

-- Insert sample data into ratings table
INSERT INTO ratings (rating_id, customer_id, product_id, rating) VALUES
(1, 101, 201, 5),
(2, 103, 202, 4),
(3, 105, 203, 3);

SELECT * FROM orders;

SELECT * FROM ratings;

SELECT customer_id
FROM orders
WHERE customer_id NOT IN (SELECT customer_id FROM ratings);

SELECT o.customer_id
FROM orders o
LEFT JOIN ratings r ON o.customer_id = r.customer_id
WHERE r.customer_id IS NULL;



