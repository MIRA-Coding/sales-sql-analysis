SELECT p.category, COUNT(o.id) AS orders_count
FROM products p
LEFT JOIN orders o ON o.product_id = p.id
GROUP BY p.category;
