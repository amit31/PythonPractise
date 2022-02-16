# Write your MySQL query statement below
select e.name as Employee from employee e join employee p
on e.managerid=p.id and e.salary>p.salary