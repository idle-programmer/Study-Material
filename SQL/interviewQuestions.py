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
