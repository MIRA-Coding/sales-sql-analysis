SELECT c.name as customer_name, sum(p.price * o.qty) AS total_sales
from orders o
JOIN customers c ON c.id = o.customer_id 
join products p on o.product_id = p.id
group by c.name;
