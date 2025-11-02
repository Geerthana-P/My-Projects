DROP TABLE PRODUCTS;
DROP TABLE sales;
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    category VARCHAR(50)
);

CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    product_id INT,
    quantity INT,
    price DECIMAL(10,2),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

INSERT INTO products (product_id, product_name, category) VALUES
(1, 'Laptop', 'Electronics'),
(2, 'Headphones', 'Electronics'),
(3, 'Shirt', 'Clothing'),
(4, 'Book', 'Stationery');

INSERT INTO sales (sale_id, product_id, quantity, price) VALUES
(1, 1, 5, 70000),
(2, 2, 10, 2000),
(3, 3, 20, 1000),
(4, 4, 15, 500),
(5, 1, 2, 70000);


SELECT * FROM products;
SELECT * FROM sales;

SELECT 
    p.category,
    SUM(s.quantity * s.price) AS total_revenue
FROM sales s
JOIN products p ON s.product_id = p.product_id
GROUP BY p.category;



