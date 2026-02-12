# Given a table with columns id, ip_address, status, and datetime.
# Write an SQL query to return, for the date 04-08-2025, each distinct ip_address along 
# with the count of times it was online (status = TRUE) and offline (status = FALSE).
"""
SELECT
    ip_address,
    COUNT(*) FILTER (WHERE status = TRUE)  AS online_count,
    COUNT(*) FILTER (WHERE status = FALSE) AS offline_count
FROM logs
WHERE DATE(datetime) = '2025-08-04'
GROUP BY ip_address;
"""

# Find Duplicate Email or Removing duplicate emails
"""
SELECT 
    email,
    COUNT(*) AS cnt
FROM Customer
GROUP BY email
HAVING COUNT(*) > 1;
""" 

# Find nth highest salary  
"""
SELECT DISTINCT Salary
FROM Employee
ORDER BY Salary DESC
LIMIT 1 OFFSET (n-1);
"""

# Find nth highest salary without order by
"""
SELECT e1.salary
FROM Employee e1
WHERE 3 = (
    SELECT COUNT(DISTINCT e2.salary)
    FROM Employee e2
    WHERE e2.salary >= e1.salary
);
"""