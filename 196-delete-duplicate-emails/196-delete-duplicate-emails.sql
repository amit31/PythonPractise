# Write your MySQL query statement below
 delete p1
FROM Person p1,
    Person p2
WHERE
    p1.Email = p2.Email
and p1.id>p2.id