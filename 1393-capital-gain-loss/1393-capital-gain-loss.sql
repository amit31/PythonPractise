# Write your MySQL query statement below


select s.stock_name,sum(s.PRICEN) as capital_gain_loss

from

(select stock_name,
CASE 
when operation = "SELL"  then PRICE else price*-1 END as PRICEN
from stocks )s group by s.stock_name
