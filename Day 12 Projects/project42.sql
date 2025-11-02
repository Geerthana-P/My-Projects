USE company_db;

SELECT * FROM orders;

WITH ordered_orders AS (
    SELECT 
        customer_id,
        order_date,
        ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date) AS order_num,
        LAG(order_date) OVER (PARTITION BY customer_id ORDER BY order_date) AS prev_order_date
    FROM orders
)
SELECT 
    customer_id,
    order_date,
    prev_order_date,
    DATEDIFF(order_date, prev_order_date) AS days_between_orders
FROM ordered_orders
WHERE order_num <= 2;   -- only first two orders

SELECT 
    customer_id, 
    order_date,
    MAX(order_date) OVER (PARTITION BY customer_id) AS last_order_date
FROM orders;
