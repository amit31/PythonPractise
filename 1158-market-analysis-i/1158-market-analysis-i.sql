# Write your MySQL query statement below


#where filters the rows when used with order_date
#and will give result with left join even when condition fails

with temp as (
select user_id as buyer_id,join_date,count(order_date) as orders_in_2019
from users u join orders o 
on u.user_id=o.buyer_id where o.order_date > '2018-12-31' group by user_id,join_date )

select u.user_id as buyer_id,u.join_date,ifnull(t.orders_in_2019,0) as orders_in_2019  from users u left join temp t on u.user_id=t.buyer_id