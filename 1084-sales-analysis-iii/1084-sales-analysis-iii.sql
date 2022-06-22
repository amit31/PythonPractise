# Write your MySQL query statement below



# select product_id,product_name from product 
# where product_id not in 
# (select product_id from sales where sale_date >"2019-03-31" or sale_date <"2018-12-31" )


# with temp as 
# (select p.product_id from product p left join sales s 
# on p.product_id=s.product_id
#  where sale_date >"2019-03-31" or sale_date <"2018-12-31" ) 
# select product_id,product_name from temp where 

# select product_id,product_name from product 
# where product_id not in 

with temp as 
(select p.product_id,p.product_name,s.sale_date  from product p left join sales s 
on p.product_id=s.product_id) 
select product_id,product_name from product 
where product_id not in (
select temp.product_id from temp 
where temp.sale_date >"2019-03-31" or temp.sale_date <"2018-12-31" or temp.sale_date is null)