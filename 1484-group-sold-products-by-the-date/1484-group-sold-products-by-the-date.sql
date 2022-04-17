# Write your MySQL query statement below

select sell_date,count( distinct product ) as num_sold,GROUP_CONCAT(distinct product order by product) as products from activities
group by sell_date

#STRING_AGG(Mail,',')  WITHIN GROUP ( ORDER BY FirstName ASC)  AS
#GROUP_CONCAT(al.AlbumName ORDER BY al.AlbumName DESC)