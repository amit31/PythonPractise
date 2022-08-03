# Write your MySQL query statement below

# select t.customer_number
# (select count(order_number) , customer_number  from orders 
# group by customer_number order by 2 desc )t


select customer_number from 

(select count(order_number) as cnt ,customer_number from orders group by customer_number order by cnt desc limit 1) t

