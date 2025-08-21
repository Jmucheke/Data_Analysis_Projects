-- DROP DATABASE IF EXISTS ecommerce;
CREATE DATABASE ecommerce;

USE ecommerce;

DROP TABLE IF EXISTS customers;
CREATE TABLE customers (
	customer_id INT PRIMARY KEY,
	name VARCHAR(100),
    email VARCHAR(100),
    country VARCHAR(50)
);

INSERT INTO customers VALUES
(1, 'Alice Johnson', 'alice@example.com', 'USA'),
(2, 'Bob Smith', 'bob@example.com', 'UK'),
(3, 'Charlie Lee', 'charlie@example.com', 'Canada'),
(4, 'Diana Prince', 'diana@example.com', 'USA'),
(5, 'Ethan Brown', 'ethan@example.com', 'Australia');


DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10, 2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

INSERT INTO orders VALUES
(1001, 1, '2025-01-10', 250.50),
(1002, 2, '2025-02-15', 110.00),
(1003, 1, '2025-03-05', 75.00),
(1004, 3, '2025-04-20', 305.25),
(1005, 4, '2025-05-18', 500.00),
(1006, 5, '2025-06-22', 0.00); 


DROP TABLE IF EXISTS suppliers;
CREATE TABLE suppliers (
    supplier_id INT PRIMARY KEY,
    supplier_name VARCHAR(100),
    country VARCHAR(50)
);

INSERT INTO suppliers VALUES
(201, 'TechCorp', 'USA'),
(202, 'Peripherals Inc.', 'Germany'),
(203, 'FurniHouse', 'Sweden');


DROP TABLE IF EXISTS categories;
CREATE TABLE categories (
    category_id INT PRIMARY KEY,
    category_name VARCHAR(100)
);

INSERT INTO categories VALUES
(1, 'Electronics'),
(2, 'Accessories'),
(3, 'Furniture');

DROP TABLE IF EXISTS products;
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category_id INT,
    supplier_id INT,
    price DECIMAL(10, 2),
    stock INT,
    FOREIGN KEY (category_id) REFERENCES categories(category_id),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);

INSERT INTO products VALUES
(101, 'Laptop', 1, 201, 75.00, 20),
(102, 'Mouse', 2, 202, 50.50, 100),
(103, 'Keyboard', 2, 202, 110.00, 50),
(104, 'Monitor', 1, 201, 100.00, 30),
(105, 'Desk', 3, 203, 100.00, 10),
(106, 'Chair', 3, 203, 85.00, 0); -- out of stock

DROP TABLE IF EXISTS order_items;
CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    price DECIMAL(10, 2),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

INSERT INTO order_items VALUES
(1, 1001, 101, 2, 100.00),
(2, 1001, 102, 1, 50.50),
(3, 1002, 103, 1, 110.00),
(4, 1003, 101, 1, 75.00),
(5, 1004, 104, 3, 100.00),
(6, 1005, 105, 5, 100.00);

