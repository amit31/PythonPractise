# Write your MySQL query statement below

select name , ifnull(sum(distance),0) as travelled_distance from users u left join rides r
on u.id=r.user_id group by name order by travelled_distance  desc,name