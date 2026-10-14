select p.category, sum(p.price * o.qty) as category_revenue
from customers c
join orders o on c.id = o.customer_id
join products p on o.product_id = p.id
group by p.category;
