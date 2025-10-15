/*Selecting top 10 most popular car brands and their best selling models*/

CREATE TEMP TABLE model_sales AS
SELECT 
    make,
    model,
    COUNT(*) AS model_sales
FROM vehicle_sales
GROUP BY make, model;

CREATE TEMP TABLE brand_sales AS
SELECT 
    make,
    COUNT(*) AS total_sales
FROM vehicle_sales
GROUP BY make;

CREATE TEMP TABLE best_model AS
SELECT 
    make,
    MAX(model_sales) AS best_model_sales
FROM model_sales
GROUP BY make;

SELECT 
    b.make,
    bs.total_sales,
    m.model AS best_model,
    b.best_model_sales
FROM best_model b
JOIN model_sales m ON b.make = m.make AND b.best_model_sales = m.model_sales
JOIN brand_sales bs ON b.make = bs.make
ORDER BY bs.total_sales DESC
LIMIT 10;

/*Selecting the number of cars sold in each month*/
SELECT
    SUBSTR(saledate, 4, 2) AS Month,
    SUBSTR(saledate, 7, 4) AS Year,
    SUM(CASE WHEN make='Ford'        THEN 1 ELSE 0 END) AS Ford,
    SUM(CASE WHEN make='Chevrolet'   THEN 1 ELSE 0 END) AS Chevrolet,
    SUM(CASE WHEN make='Nissan'      THEN 1 ELSE 0 END) AS Nissan,
    SUM(CASE WHEN make='Toyota'      THEN 1 ELSE 0 END) AS Toyota,
    SUM(CASE WHEN make='Dodge'       THEN 1 ELSE 0 END) AS Dodge,
    SUM(CASE WHEN make='Honda'       THEN 1 ELSE 0 END) AS Honda,
    SUM(CASE WHEN make='Hyundai'     THEN 1 ELSE 0 END) AS Hyundai,
    SUM(CASE WHEN make='BMW'         THEN 1 ELSE 0 END) AS BMW,
    SUM(CASE WHEN make='Kia'         THEN 1 ELSE 0 END) AS Kia
FROM vehicle_sales
WHERE SUBSTR(saledate, 7, 4)='2015'
GROUP BY month
ORDER BY month;

/*Top 10 brands in 2014*/
SELECT 
    make,
    COUNT(*) AS total_sales
FROM vehicle_sales
WHERE SUBSTR(saledate, 7, 4) = '2014'
GROUP BY make
ORDER BY total_sales DESC
LIMIT 10;

/*Top 10 brands in 2015*/
SELECT 
    make,
    COUNT(*) AS total_sales
FROM vehicle_sales
WHERE SUBSTR(saledate, 7, 4) = '2015'
GROUP BY make
ORDER BY total_sales DESC
LIMIT 10;

/*Most expensive brands and models*/
SELECT 
    make,
    model,
    ROUND(AVG(sellingprice), 0) AS avg_price,
    ROUND(AVG(mmr), 0) AS avg_market_value,
    ROUND(AVG(sellingprice - mmr), 0) AS avg_margin
FROM vehicle_sales
GROUP BY make
ORDER BY avg_price DESC
LIMIT 20;

/*Biggest price difference between mmr and selling price*/
SELECT
    make,
    model,
    sellingprice,
    mmr,
    (sellingprice - mmr) AS price_difference
FROM vehicle_sales
ORDER BY price_difference DESC
LIMIT 10;

/*Most popular color for each brand*/
WITH color_rank AS (
    SELECT 
        make,
        color,
        COUNT(*) AS color_sales,
        RANK() OVER (PARTITION BY make ORDER BY COUNT(*) DESC) AS rnk
    FROM vehicle_sales
    GROUP BY make, color
)
SELECT make, color, color_sales
FROM color_rank
WHERE rnk = 1
ORDER BY color_sales DESC;