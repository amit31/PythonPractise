# Write your MySQL query statement below


#select player_id,min(event_date) as first_login from activity group by player_id
select temp.player_id , temp.event_date as first_login from
(select player_id, event_date,dense_rank() Over (partition by player_id order by event_date)  as dr from activity ) temp
where temp.dr=1