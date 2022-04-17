# Write your MySQL query statement below


# select id,visit_date,people from 

# (select id,visit_date,people, lag (id) OVER (Order BY id ) as prev_id, lag(id,2)  OVER (Order BY id ) as two_prev_id from stadium
# where people >= 100)temp where id - prev_id >=1 and id-two_prev_id>1


# select id,visit_date,people from 
#  (select id,visit_date,people,lead (id) OVER (Order BY id ) as next_id, lead(id,2) OVER (Order BY id ) as next2_id,
#  lag (id) OVER (Order BY id ) as prev_id, lag(id,2) OVER (Order BY id ) as prev2_id
#  from stadium  where people >= 100)temp where next_id-id =1 and next2_id - id =2 
#  or id - prev_id=1 and id-prev2_id=2
#  # select id,visit_date,people from 
#  # (select id,visit_date,people,ifnull(lead (id) OVER (Order BY id ),0) as next_id, ifnull (lead(id,2) OVER (Order BY id ),0) as next2_id,
#  # ifnull(lag (id) OVER (Order BY id ),0) as prev_id, ifnull(lag(id,2) OVER (Order BY id ),0) as prev2_id
#  # from stadium  where people >= 100) temp where next_id-id =1 and next2_id - id =2 
#  # or id - prev_id=1 and id-prev2_id=2
 
select distinct t1.*
from stadium t1, stadium t2, stadium t3
where t1.people >= 100 and t2.people >= 100 and t3.people >= 100
and
(
    (t1.id - t2.id = 1 and t1.id - t3.id = 2 and t2.id - t3.id =1)  -- t1, t2, t3
    or
    (t2.id - t1.id = 1 and t2.id - t3.id = 2 and t1.id - t3.id =1) -- t2, t1, t3
    or
    (t3.id - t2.id = 1 and t2.id - t1.id =1 and t3.id - t1.id = 2) -- t3, t2, t1
)
order by t1.id
;