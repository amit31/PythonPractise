# Write your MySQL query statement below

#select id 
#from
# (select id,recordDate,temperature, lag(temperature)  over (order by recordDate) as prev_date_temp
# from weather) #temp where temp.temperature > temp.prev_date_temp

# select id from (
# select id,recordDate,temperature, lag(temperature)  over (order by recordDate ) as next_date_temp ,
# lag(recordDate) over (order by recordDate) as prev_date 
# from weather )temp where temp.temperature > temp.prev_date
# and datediff(temp.recordDate,temp.prev_date)=1

# select id from
# (select id,recordDate,temperature, lag(temperature)  over (order by recordDate ) as next_date_temp ,
# lag(recordDate) over (order by recordDate) as prev_date 
# from weather)temp where datediff(temp.recordDate,temp.prev_date)=1 and temp.temperature>temp.next_date_temp

select id from
(select id,recordDate,temperature,lag(temperature) over (order by recordDate) as prev_date_temp,lag(recordDate) over (order by recordDate) as prev_date from weather ) temp where temp.temperature> temp.prev_date_temp and datediff(temp.recordDate,temp.prev_date)=1