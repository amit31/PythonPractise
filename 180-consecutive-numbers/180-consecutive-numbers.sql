# Write your MySQL query statement below


# select num as  ConsecutiveNums from

# () 

# where count()

# SELECT DISTINCT num
# FROM
# (
# SELECT num,LEAD(num) OVER(ORDER BY id) AS lead, LAG(num) OVER (ORDER BY id) AS lag
# FROM logs
# )t
# WHERE num=lead and num=lag;

select distinct num as ConsecutiveNums  from
(SELECT num,LEAD(num,1) OVER(ORDER BY id) AS lead1, 
LEAD(num,2) OVER(ORDER BY id) AS lead2, 
LAG(num,1) OVER (ORDER BY id) AS lag1,
LAG(num,2) OVER (ORDER BY id) AS lag2 from logs)t1
where num =t1.lead1 and num=t1.lead2
OR num=t1.lag1 and num = t1.lag2
OR num=t1.lag1 and num=t1.lead1

# SELECT num,LEAD(num,1) OVER(ORDER BY id) AS lead1, 
# LEAD(num,2) OVER(ORDER BY id) AS lead2, 
# LAG(num,1) OVER (ORDER BY id) AS lag1,
# LAG(num,2) OVER (ORDER BY id) AS lag2 from logs