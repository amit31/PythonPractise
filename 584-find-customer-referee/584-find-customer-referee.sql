# Write your MySQL query statement below

select c.name from customer c  join customer d
on c.id=d.id where c.referee_id is NULL or c.referee_id!=2