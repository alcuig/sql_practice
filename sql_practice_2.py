CREATE DATABASE sql_practice_2;

CREATE TABLE eu_chocolate_sales(
    sale_id varchar(50),
    product_code varchar(50),
    customer_id varchar(50),
    amount_purchased integer
);

INSERT INTO eu_chocolate_sales(
    sale_id,
    product_code,
    customer_id ,
    amount_purchased
) VALUES 
    ('S1', 'P1', 'C1', 2),
    ('S2', 'P4', 'C2', 1),
    ('S3', 'P3', 'C3', 1),
    ('S4', 'P2', 'C4', 1),
    ('S5', 'P2', 'C4', 7),
    ('S6', 'P1', 'C5', 1),
    ('S7', 'P3', 'C6', 2),
    ('S8', 'P4', 'C7', 1),
    ('S9', 'P4', 'C8', 3),
    ('S10', 'P4', 'C9', 6),
    ('S11', 'P1', 'C10',1),
    ('S12', 'P2', 'C11',1),
    ('S13', 'P1', 'C12', 2),
    ('S14', 'P3', 'C13', 1),
    ('S15', 'P2', 'C4', 5);

CREATE TABLE europe_chocolate_products(
    product_code varchar(50),
    product_name varchar(50),
    product_price integer
);

INSERT INTO chocolate_products(
    product_code,
    product_name,
    product_price
) VALUES ('P1','chocolate_delice_milk',5),
('P2','chocolate_rabbit_dark',2),
('P3','chocolate_rabbit_white',2),
('P4','chocolate_seashell_box',6), 
('P5', 'chocolate_easter_egg_milk', 14), 
('P6', 'chocolate_santa_white', 3);

CREATE TABLE chocolate_customers(
    customer_id varchar(50), 
    customer_age integer,
    customer_country varchar(50)
);

INSERT INTO chocolate_customers(
    customer_id, 
    customer_age,
    customer_country
) VALUES ('C1', 20, 'Italy'),
    ('C2', 22, 'France'), 
    ('C3', 49, 'Spain'), 
    ('C4', 87, 'Italy'), 
    ('C5', 34, 'France'),
    ('C6', 45, 'France'),
    ('C7', 56, 'United Kingdom'), 
    ('C8', 64, 'Russia'), 
    ('C9', 51, 'Spain'), 
    ('C10', 39, 'Spain'), 
    ('C11', 31, 'United Kingdom'),
    ('C12', 29, 'France'),
    ('C13', 18, 'France'), 
    ('C14', 40, 'Vietnam'), 
    ('C15', 20, 'Philippines'), 
    ('C16', 25, 'Vietnam'), 
    ('C17', 67, 'Vietnam');

#INNER JOIN 
#To examine which was most popular with customers.

SELECT eu_chocolate_sales.amount_purchased, chocolate_products.product_name, chocolate_products.product_price
FROM eu_chocolate_sales INNER JOIN chocolate_products
ON eu_chocolate_sales.product_code = chocolate_products.product_code;

#RESULT
product_code | amount_purchased |      product_name      | product_price 
--------------+------------------+------------------------+---------------
 P1           |                2 | chocolate_delice_milk  |             5
 P1           |                1 | chocolate_delice_milk  |             5
 P1           |                1 | chocolate_delice_milk  |             5
 P1           |                2 | chocolate_delice_milk  |             5
 P2           |                5 | chocolate_rabbit_dark  |             2
 P2           |                1 | chocolate_rabbit_dark  |             2
 P2           |                7 | chocolate_rabbit_dark  |             2
 P2           |                1 | chocolate_rabbit_dark  |             2
 P3           |                1 | chocolate_rabbit_white |             2
 P3           |                2 | chocolate_rabbit_white |             2
 P3           |                1 | chocolate_rabbit_white |             2
 P4           |                6 | chocolate_seashell_box |             6
 P4           |                3 | chocolate_seashell_box |             6
 P4           |                1 | chocolate_seashell_box |             6
 P4           |                1 | chocolate_seashell_box |             6



#LEFT JOIN 
#To find out which of the customers in customer database purchased products in Europe, and where they
#  were based.
#QUERY
SELECT eu_chocolate_sales.amount_purchased, chocolate_customers.customer_country
FROM chocolate_customers LEFT JOIN eu_chocolate_sales
ON eu_chocolate_sales.customer_id = chocolate_customers.customer_id; 
 
#RESULT
 amount_purchased | customer_country 
------------------+------------------
                2 | Italy
                1 | France
                1 | Spain
                5 | Italy
                7 | Italy
                1 | Italy
                1 | France
                2 | France
                1 | United Kingdom
                3 | Russia
                6 | Spain
                1 | Spain
                1 | United Kingdom
                2 | France
                1 | France
                  | Vietnam
                  | Philippines
                  | Vietnam
                  | Vietnam

#To see which products were and were not purchased in Europe. 
#QUERY
SELECT eu_chocolate_sales.amount_purchased, chocolate_products.product_name 
FROM chocolate_products LEFT JOIN eu_chocolate_sales
ON eu_chocolate_sales.product_code = chocolate_products.product_code;

#RESULT
amount_purchased |       product_name        
------------------+---------------------------
                2 | chocolate_delice_milk
                1 | chocolate_delice_milk
                1 | chocolate_delice_milk
                2 | chocolate_delice_milk
                5 | chocolate_rabbit_dark
                1 | chocolate_rabbit_dark
                7 | chocolate_rabbit_dark
                1 | chocolate_rabbit_dark
                1 | chocolate_rabbit_white
                2 | chocolate_rabbit_white
                1 | chocolate_rabbit_white
                6 | chocolate_seashell_box
                3 | chocolate_seashell_box
                1 | chocolate_seashell_box
                1 | chocolate_seashell_box
                  | chocolate_easter_egg_milk
                  | chocolate_santa_white

#RIGHT JOIN 

#OUTER JOIN 

#Display all information about sales and products.
#QUERY
SELECT *
FROM eu_chocolate_sales FULL JOIN chocolate_products
ON eu_chocolate_sales.product_code = chocolate_products.product_code;

#RESULT
 sale_id | product_code | customer_id | amount_purchased | product_code |       product_name        | product_price 
---------+--------------+-------------+------------------+--------------+---------------------------+---------------
 S13     | P1           | C12         |                2 | P1           | chocolate_delice_milk     |             5
 S11     | P1           | C10         |                1 | P1           | chocolate_delice_milk     |             5
 S6      | P1           | C5          |                1 | P1           | chocolate_delice_milk     |             5
 S1      | P1           | C1          |                2 | P1           | chocolate_delice_milk     |             5
 S15     | P2           | C4          |                5 | P2           | chocolate_rabbit_dark     |             2
 S12     | P2           | C11         |                1 | P2           | chocolate_rabbit_dark     |             2
 S5      | P2           | C4          |                7 | P2           | chocolate_rabbit_dark     |             2
 S4      | P2           | C4          |                1 | P2           | chocolate_rabbit_dark     |             2
 S14     | P3           | C13         |                1 | P3           | chocolate_rabbit_white    |             2
 S7      | P3           | C6          |                2 | P3           | chocolate_rabbit_white    |             2
 S3      | P3           | C3          |                1 | P3           | chocolate_rabbit_white    |             2
 S10     | P4           | C9          |                6 | P4           | chocolate_seashell_box    |             6
 S9      | P4           | C8          |                3 | P4           | chocolate_seashell_box    |             6
 S8      | P4           | C7          |                1 | P4           | chocolate_seashell_box    |             6
 S2      | P4           | C2          |                1 | P4           | chocolate_seashell_box    |             6
         |              |             |                  | P5           | chocolate_easter_egg_milk |            14
         |              |             |                  | P6           | chocolate_santa_white     |             3


#Display all information about customers and products. 
#QUERY
SELECT *
FROM eu_chocolate_sales FULL JOIN chocolate_customers
ON eu_chocolate_sales.customer_id = chocolate_customers.customer_id;

#RESULT
 sale_id | product_code | customer_id | amount_purchased | customer_id | customer_age | customer_country 
---------+--------------+-------------+------------------+-------------+--------------+------------------
 S1      | P1           | C1          |                2 | C1          |           20 | Italy
 S2      | P4           | C2          |                1 | C2          |           22 | France
 S3      | P3           | C3          |                1 | C3          |           49 | Spain
 S15     | P2           | C4          |                5 | C4          |           87 | Italy
 S5      | P2           | C4          |                7 | C4          |           87 | Italy
 S4      | P2           | C4          |                1 | C4          |           87 | Italy
 S6      | P1           | C5          |                1 | C5          |           34 | France
 S7      | P3           | C6          |                2 | C6          |           45 | France
 S8      | P4           | C7          |                1 | C7          |           56 | United Kingdom
 S9      | P4           | C8          |                3 | C8          |           64 | Russia
 S10     | P4           | C9          |                6 | C9          |           51 | Spain
 S11     | P1           | C10         |                1 | C10         |           39 | Spain
 S12     | P2           | C11         |                1 | C11         |           31 | United Kingdom
 S13     | P1           | C12         |                2 | C12         |           29 | France
 S14     | P3           | C13         |                1 | C13         |           18 | France
         |              |             |                  | C14         |           40 | Vietnam
         |              |             |                  | C15         |           20 | Philippines
         |              |             |                  | C16         |           25 | Vietnam
         |              |             |                  | C17         |           67 | Vietnam




