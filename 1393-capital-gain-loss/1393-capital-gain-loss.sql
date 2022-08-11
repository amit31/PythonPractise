# Write your MySQL query statement below


# select s.stock_name,sum(s.PRICEN) as capital_gain_loss
# from (select stock_name,
# CASE 
# when operation = "SELL"  then PRICE else price*-1 
# END as PRICEN
# from stocks )s group by s.stock_name

with temp as (
select stock_name , case when operation = "BUY" then price*-1 else price end as price  from stocks )
select temp.stock_name,sum(temp.price) as capital_gain_loss  from temp group by stock_name