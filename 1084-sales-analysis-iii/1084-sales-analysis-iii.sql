# Write your MySQL query statement below


# select p.product_id,product_name from product p
# join sales s on p.product_id=s.product_id
# and s.sale_date between "2019-01-01" and "2019-03-31"

select product_id,product_name from product 
where product_id not in 
(select product_id from sales where sale_date >"2019-03-31" or sale_date <"2018-12-31" )