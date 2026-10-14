select count(*) as total_orders,
    sum(qty) as total_quantity
from orders;
