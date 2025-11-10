CREATE DATABASE IF NOT EXISTS EcommerceInventory;
USE EcommerceInventory;

DROP TABLE IF EXISTS Stock;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Suppliers;

CREATE TABLE Suppliers (
    supplier_id INT AUTO_INCREMENT PRIMARY KEY,
    supplier_name VARCHAR(100) NOT NULL,
    contact_email VARCHAR(100),
    phone_number VARCHAR(15)
);

CREATE TABLE Products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    price DECIMAL(10,2),
    supplier_id INT,
    FOREIGN KEY (supplier_id) REFERENCES Suppliers(supplier_id)
);

CREATE TABLE Stock (
    stock_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    quantity INT,
    last_updated DATE,
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

INSERT INTO Suppliers (supplier_name, contact_email, phone_number) VALUES
('TechSource Pvt Ltd', 'contact@techsource.com', '9876543210'),
('HomeEssentials Co', 'support@homeessentials.com', '9988776655'),
('GadgetWorld', 'sales@gadgetworld.com', '9123456789'),
('KitchenPlus', 'help@kitchenplus.com', '9871204567'),
('MegaMart Supplies', 'info@megamart.com', '9012345678');

INSERT INTO Products (product_name, category, price, supplier_id) VALUES
('Wireless Mouse', 'Electronics', 599.00, 1),
('Bluetooth Speaker', 'Electronics', 1299.00, 3),
('Stainless Steel Pan', 'Kitchenware', 850.00, 4),
('LED Table Lamp', 'Home Decor', 699.00, 2),
('Smart Watch', 'Electronics', 2499.00, 3),
('Cotton Bedsheet', 'Home Decor', 999.00, 5),
('USB-C Cable', 'Electronics', 299.00, 1),
('Electric Kettle', 'Appliances', 1199.00, 4),
('Notebook Pack', 'Stationery', 199.00, 5),
('Wall Clock', 'Home Decor', 749.00, 2);

INSERT INTO Stock (product_id, quantity, last_updated) VALUES
(1, 25, '2025-11-10'),
(2, 8, '2025-11-10'),
(3, 15, '2025-11-09'),
(4, 5, '2025-11-08'),
(5, 50, '2025-11-07'),
(6, 9, '2025-11-06'),
(7, 40, '2025-11-05'),
(8, 3, '2025-11-04'),
(9, 18, '2025-11-03'),
(10, 6, '2025-11-02');



SELECT 
    p.product_id,
    p.product_name,
    p.category,
    s.quantity AS stock_quantity,
    sup.supplier_name
FROM Products p
JOIN Stock s ON p.product_id = s.product_id
JOIN Suppliers sup ON p.supplier_id = sup.supplier_id
WHERE s.quantity < 10;