# Write your MySQL query statement below

select name from SalesPerson s 
where sales_id NOT IN (select sales_id from company c join orders o on c.com_id=o.com_id and c.name ="RED")