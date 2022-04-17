# Write your MySQL query statement below

# select t.customer_number
# (select count(order_number) , customer_number  from orders 
# group by customer_number order by 2 desc )t


select t.customer_number from
(select count(order_number) , customer_number  from orders 
 group by customer_number order by 1 desc limit 1)t


