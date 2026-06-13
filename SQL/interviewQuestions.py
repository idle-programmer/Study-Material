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

# Emp with highest salary of each department
"""
SELECT e.id, e.name, d.name AS dept_name, e.salary
FROM employees e
JOIN department d ON e.dept_id = d.id
WHERE e.salary = (
    SELECT MAX(e2.salary)
    FROM employees e2
    WHERE e2.dept_id = e.dept_id
);
"""

# CREATE TABLE products ( product_id INT PRIMARY KEY,
# product_name VARCHAR(100), category VARCHAR(50), 
# price DECIMAL(10,2), stock_quantity INT ); 
# SQL: Write a query to list all categories 
# which have more than 5 unique products.
"""
SELECT category, COUNT(product_id) AS product_count
FROM products
GROUP BY category
HAVING COUNT(product_id) > 5;
"""

# Diff betw "IN" and "BETWEEN"
"""IN is used to filter rows based on a list of specific values, while BETWEEN is used 
to filter rows within a range.Also, BETWEEN is inclusive of both boundary values."""

# View in DBMS
"""A View is a virtual table based on a SQL query. It is mainly used for security, simplifying 
complex queries, data abstraction, and reusability because it presents data from one or more tables 
without storing the data itself. """


# Diff between postgres and mysql
"""
| Feature                     | PostgreSQL (Postgres)                                         | MySQL                                                             |
| --------------------------- | ------------------------------------------------------------- | ----------------------------------------------------------------- |
| **Database Type**           | Object-Relational Database Management System (ORDBMS)         | Relational Database Management System (RDBMS)                     |
| **Connection Model**        | Process-per-connection (separate OS process)                  | Thread-per-connection (separate thread)                           |
| **Transactional DDL**       | ✅ Supported (Roll back a schema change)                      | ❌ Not supported (Schema changes auto-commit)                     |
| **JSON Support**            | Native JSON & JSONB (binary JSON with indexing)               | JSON supported, but less powerful than JSONB                      |
| **Materialized Views**      | ✅ Supported                                                  | ❌ Not supported natively                                         |
| **Best Use Cases**          | Enterprise applications, FinTech, Analytics, Complex Systems  | Web applications, CMS, E-commerce, Read-heavy workloads           |


PostgreSQL provides powerful schema support, which makes implementing multi-tenant SaaS applications easier. 
Each tenant can have its own schema within the same database, providing better data isolation compared to 
storing all tenants in shared tables with a tenant_id column.
"""