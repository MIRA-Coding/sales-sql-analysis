select c.name, sum(p.price * o.qty) as total 
from orders o 
join customers c on o.customer_id = c.id
join products p on o.product_id = p.id
group by c.name
order by total desc
limit 1;
