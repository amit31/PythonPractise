# Write your MySQL query statement below


# select ad1.actor_id,ad1.director_id   from actordirector ad1 join actordirector ad2 
# on ad1.timestamp=ad2.timestamp+1 and ad1.actor_id=ad2.actor_id and ad1.director_id=ad2.director_id
# join actordirector ad3
# on ad1.timestamp=ad3.timestamp+2 and ad1.actor_id=ad3.actor_id and ad1.director_id=ad3.director_id


# with acd as (

#     select * from actordirector order by timestamp
# ) 
#  select ad1.actor_id,ad1.director_id,ad1.timestamp  from acd ad1 #join  acd ad2
# # on ad1.timestamp=ad2.timestamp+1 and ad1.actor_id=ad2.actor_id and ad1.director_id=ad2.director_id
# # join acd ad3
# # on ad1.timestamp=ad3.timestamp+2 and ad1.actor_id=ad3.actor_id and ad1.director_id=ad3.director_id


select actor_id, director_id
from ActorDirector
group by actor_id, director_id
having count(timestamp) > 2
