USE company_db;
DROP TABLE sales;

CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    region VARCHAR(50),
    amount DECIMAL(10,2)
);

INSERT INTO sales (sale_id, region, amount) VALUES
(1,'North', 25000.00),
(2,'South', 18000.00),
(3,'East', 15000.00),
(4,'West', 12000.00),
(5,'North', 30000.00),
(6,'South', 22000.00),
(7,'East', 10000.00),
(8,'West', 15000.00),
(9,'North', 20000.00),
(10,'South', 25000.00);

SELECT * FROM sales;

SELECT 
    region, 
    SUM(amount) AS total_sales
FROM sales
GROUP BY region;

SELECT *,
 RANK() OVER (ORDER BY total_sales DESC) AS sales_rank
FROM (
 SELECT region, SUM(amount) AS total_sales
 FROM sales
 GROUP BY region
) AS regional_sales;


