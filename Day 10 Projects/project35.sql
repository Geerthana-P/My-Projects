-- Create table
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    stock INT,
    price DECIMAL(10,2)
);

-- Insert products
INSERT INTO products (product_id, product_name, stock, price)
VALUES 
(1, 'Laptop', 50, 1200.00),
(2, 'Mouse', 200, 25.00);

-- Check stock
SELECT * FROM products;

-- Sale: 5 Laptops sold
UPDATE products
SET stock = stock - 5
WHERE product_id = 1;

-- Check stock again
SELECT * FROM products;

-- Insert new product
INSERT INTO products (product_id, product_name, stock, price)
VALUES (3, 'Keyboard', 100, 50.00);

SELECT * FROM products;
