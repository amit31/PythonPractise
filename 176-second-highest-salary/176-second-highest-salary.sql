# Write your MySQL query statement below

select IFNULL(
(select (salary) as SecondHighestSalary from employee where salary Not In ( Select max(salary) from employee) order by salary desc limit 1),NULL) as SecondHighestSalary

# select IFNULL(

# (select SecondHighestSalary from
# (select distinct(salary) as SecondHighestSalary , dense_rank() Over ( ORDER BY salary desc) as denserank  from employee)temp
# where temp.denserank = 2 ),NULL) as SecondHighestSalary