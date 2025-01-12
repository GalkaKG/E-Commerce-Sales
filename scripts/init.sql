-- -- Create the table to store the sales report data
-- CREATE TABLE amazon_sales_report (
--     index INT,
--     order_id VARCHAR(255),
--     date DATE,
--     status VARCHAR(50),
--     fulfilment VARCHAR(50),
--     sales_channel VARCHAR(50),
--     ship_service_level VARCHAR(50),
--     style VARCHAR(50),
--     sku VARCHAR(255),
--     category VARCHAR(100),
--     size VARCHAR(50),
--     asin VARCHAR(50),
--     courier_status VARCHAR(50),
--     qty INT,
--     currency VARCHAR(10),
--     amount NUMERIC(10, 2),
--     ship_city VARCHAR(100),
--     ship_state VARCHAR(100),
--     ship_postal_code VARCHAR(50),
--     ship_country VARCHAR(50),
--     promotion_ids TEXT,
--     b2b BOOLEAN,
--     fulfilled_by VARCHAR(50),
--     unnamed_22 VARCHAR(255)
-- );

-- -- -- Copy the CSV data into the table
-- -- COPY amazon_sales_report(index, order_id, date, status, fulfilment, sales_channel, ship_service_level, style, sku, category, size, asin, courier_status, qty, currency, amount, ship_city, ship_state, ship_postal_code, ship_country, promotion_ids, b2b, fulfilled_by, unnamed_22)
-- -- FROM '/docker-entrypoint-initdb.d/Amazon_Sale_Report.csv' DELIMITER ',' CSV HEADER;

-- Create the table to store the sales report data
CREATE TABLE amazon_sales_report (
    "index" INT,
    order_id VARCHAR(255),
    date DATE,
    status VARCHAR(50),
    fulfilment VARCHAR(50),
    sales_channel VARCHAR(50),
    ship_service_level VARCHAR(50),
    style VARCHAR(50),
    sku VARCHAR(255),
    category VARCHAR(100),
    size VARCHAR(50),
    asin VARCHAR(50),
    courier_status VARCHAR(50),
    qty INT,
    currency VARCHAR(10),
    amount NUMERIC(10, 2),
    ship_city VARCHAR(100),
    ship_state VARCHAR(100),
    ship_postal_code VARCHAR(50),
    ship_country VARCHAR(50),
    promotion_ids TEXT,
    b2b BOOLEAN,
    fulfilled_by VARCHAR(50),
    unnamed_22 VARCHAR(255)
);
