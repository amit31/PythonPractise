# Write your MySQL query statement below

select temp.id,temp.visit_date,temp.people from 
(select id,visit_date,people ,lead(id,1) over (order by id) as nextid , lead(id,2) over (order by id) as next2id,
lag(id,1) over (order by id ) as previd, lag(id,2)  over (order by id) as prev2id  from stadium where people >= 100) temp
where temp.next2id - temp.id =2 and temp.nextid -id =1 
or temp.nextid - temp.id =1 and temp.id - temp.previd=1 
or temp.id-temp.prev2id=2 and temp.id-temp.previd=1
