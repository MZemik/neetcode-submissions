-- Write your query below
SELECT name
FROM sales_person
WHERE sales_id NOT IN (SELECT sales_id 
                        FROM orders
                        LEFT JOIN company
                        USING(com_id)
                        WHERE name = 'CRIMSON');