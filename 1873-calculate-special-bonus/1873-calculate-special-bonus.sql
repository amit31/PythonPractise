# Write your MySQL query statement below


select employee_id,
CASE 
     when SUBSTRING(name,1,1) NOT IN ( 'M','m') and employee_id%2 !=0 THEN SALARY 
     ELSE 0 
END as bonus
from employees

#select LEFT(name,1) from employees