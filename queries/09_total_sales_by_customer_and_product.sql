select c.name as customer_name, p.name as product_name, (p.price * o.qty) as total_sales
from customers c
join orders o on c.id = o.customer_id
join products p on o.product_id = p.id;
