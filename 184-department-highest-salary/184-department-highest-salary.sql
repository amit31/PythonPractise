# Write your MySQL query statement below



# select temp.name as Department,temp.employeename as Employee ,temp.salary as Salary  from
# (select d.name,e.name as employeename,salary,dense_rank()  over ( partition by d.name order by salary desc ) as dr from employee e join department d on e.departmentId=d.id) temp where temp.dr=1


select temp.name as Department,temp.employeename as Employee,salary
from
(select e.name as employeename,d.name ,salary , dense_rank () over ( partition by departmentID order by salary desc) as dr from employee e join department d on e.departmentId=d.id) temp where temp.dr=1