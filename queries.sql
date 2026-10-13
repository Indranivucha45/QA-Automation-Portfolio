-- 1. Create a Product Table
CREATE TABLE product (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    category VARCHAR(50),
    price DECIMAL(10, 2)
);

-- 2. Insert Sample Data
INSERT INTO product VALUES (1, 'Laptop', 'Electronics', 1200.00);
INSERT INTO product VALUES (2, 'Headphones', 'Electronics', 150.00);
INSERT INTO product VALUES (3, 'Desk Chair', 'Furniture', 250.00);

-- 3. Select Query (Filtering by Category)
SELECT product_name, price 
FROM product 
WHERE category = 'Electronics';
