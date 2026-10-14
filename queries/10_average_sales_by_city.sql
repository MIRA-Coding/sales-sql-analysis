select c.city, avg(p.price * o.qty) as city_avg_price
from customers c
join orders o on c.id = o.customer_id
join products p on o.product_id = p.id
group by c.city;
