# Write your MySQL query statement below

select Email as email  from person group by email having count(email)>1