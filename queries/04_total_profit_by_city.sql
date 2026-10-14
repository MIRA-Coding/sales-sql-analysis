select c.city, sum(p.price * o.qty) as profit_of_city
from orders o
join products p on o.product_id = p.id
join customers c on o.customer_id = c.id
group by c.city;
