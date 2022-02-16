# Write your MySQL query statement below

select d.name as Department,e.name as Employee,e.salary as Salary
from Employee e join Department d on e.departmentid=d.id
WHERE
    (e.DepartmentId , Salary) IN
    (   SELECT
            DepartmentId, MAX(Salary)
        FROM
            Employee
        GROUP BY DepartmentId
    )

