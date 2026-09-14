CREATE TABLE customers (
    customer_id VARCHAR(20) PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL,
    state CHAR(2),
    created_date DATE,
    processed_at DATETIME
);
CREATE TABLE orders (
    order_id VARCHAR(20) PRIMARY KEY,
    customer_id VARCHAR(20) NOT NULL,
    order_date DATE NOT NULL,
    amount DECIMAL(12,2) NOT NULL,
    status VARCHAR(30),
    processed_at DATETIME,
    CONSTRAINT FK_orders_customers
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);
