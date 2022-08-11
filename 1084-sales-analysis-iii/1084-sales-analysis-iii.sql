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
 with cte as (
 select p.product_id,s.sale_date from product p join sales s 
on p.product_id=s.product_id where sale_date ),
 temp as (
select p.product_id,c.sale_date from product p  left join cte c on c.product_id=p.product_id where c.sale_date > "2019-03-31" or sale_date<"2018-12-31" or c.sale_date is null )
select p.product_id,p.product_name from product p where p.product_id not in (select product_id from temp)
 
 

# select p.product_id,s.sale_date from product p join sales s 
# on p.product_id=s.product_id where sale_date < "2019-01-01" or sale_date > "2019-03-31"
