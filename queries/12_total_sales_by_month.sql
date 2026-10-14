select strftime('%Y-%m', o.order_date) as months, 
    sum (p.price * o.qty) as month_revenue
from orders o
join products p on o.product_id = p.id
group by months;
