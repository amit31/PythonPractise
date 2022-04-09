# Write your MySQL query statement below

select score, DENSE_RANK () over  (order by score desc) as 'rank' from scores 

#SELECT score, DENSE_RANK() OVER (ORDER BY score DESC) AS `rank` FROM Scores ORDER BY score DESC
