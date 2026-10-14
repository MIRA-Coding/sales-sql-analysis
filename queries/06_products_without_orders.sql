select p.name 
from products p
left join orders o on o.product_id = p.id
where o.id is null;
