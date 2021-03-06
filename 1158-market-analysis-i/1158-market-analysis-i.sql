# Write your MySQL query statement below


#where filters the rows when used with order_date
#and will give result with left join even when condition fails

select user_id as buyer_id,join_date,count(o.order_date) as orders_in_2019 from  users u 
left join orders o on u.user_id=o.buyer_id
and o.order_date 
between "2019-01-01" and "2019-12-31" 
group by user_id,join_date