# Write your MySQL query statement below
# After group by we always use having 

select name,sum(amount) as balance from users u join transactions t on u.account=t.account
group by t.account having balance>9000
