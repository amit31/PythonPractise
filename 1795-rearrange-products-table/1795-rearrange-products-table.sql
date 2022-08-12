# Write your MySQL query statement below

select temp.product_id,temp.store,temp.price
from 
(select product_id,
case when store1 is not null then 'store1' end as store,
case when store1 is not null then store1 end as price 
from products
union 
select product_id,
case when store2 is not null then 'store2' end as store,
case when store2 is not null then store2  end as price 
from products
union
select product_id,
case when store3 is not null then 'store3' end as store,
case when store3 is not null then store3 end as price 
from products order by product_id ) temp where temp.store is not null
