# How would you find Top 10 users in real time?
"""For a small system, I would use SQL with ORDER BY score DESC LIMIT 10 and add an index on score. 
For a real-time system where scores change frequently, I would use Redis Sorted Sets because they 
support efficient ranking and retrieval of top users. PostgreSQL would remain the source of truth 
while Redis would maintain the leaderboard. At very large scale, I would consider maintaining only 
the top K users using a Min Heap or distributed leaderboard architecture."""


# Give me a scenario where Redis caching should NOT be used?
"""
1. Frequently Changing Data (High Write Rate): 
Stock market prices updating every second.
Read directly from the database or use streaming systems like Kafka.

2. Banking / Payment Transactions
Always read critical financial data from the source of truth (database).

3. Rarely Accessed Data: Caching works best when data is read repeatedly.
"""

# Give me a scenario where Indexing is a drawback.
""" A scenario where indexing becomes a drawback is a table that has very frequent INSERT, 
UPDATE, or DELETE operations.
Indexes also consume additional storage and may be ineffective on low-cardinality 
columns such as status values like SUCCESS, FAILED, and PENDING.""" 


# How to make your python application secured mention list of security measures ?
"""
1. Authentication & Authorization
Strong Password Storage, JWT Security, Role-Based Access Control (RBAC)
2. API Security
Rate Limiting, Input Validation, Request Size Limits
3. Prevent SQL Injection
4. XSS Protection
5. CSRF Protection
6. HTTPS Everywhere
7. Secure Headers
8. Secrets Management
9. File Upload Security
10. Database Security
11. Logging & Monitoring
12. Secure Session Management
13. CORS Security
14. Dependency Security
15. Disable Debug Mode
16. API Permissions
17. Server Security
"""

# what are the 3 pillars of production grade project
"""
1. Reliability : This pillar ensures the system consistently performs its intended function 
without failing. A production-grade project must handle unexpected errors, invalid user inputs, 
and hardware or server failures gracefully.
Core Elements: High uptime, robust error handling, automated backups, and fault tolerance.
Implementation: Setting up comprehensive logging and monitoring (e.g., using tools like Datadog or Prometheus) to 
catch and resolve issues before users notice them.

2. Maintainability: As the project scales, the codebase or system must be easily understandable, 
testable, and modifiable by different teams.
Core Elements: Clear documentation, modular design, automated testing, and CI/CD pipelines.
Implementation: Writing unit and integration tests (using frameworks like Jest or pytest) and following 
established architecture patterns to prevent "technical debt".

3. Scalability: A production-grade project should be designed to grow. Whether facing an 
unexpected surge in users or processing larger datasets, the system should adapt without 
crashing or requiring a complete architectural rewrite.
Core Elements: Horizontal and vertical scaling, load balancing, and efficient resource allocation.
Implementation: Leveraging cloud infrastructure (such as AWS, Google Cloud, or Microsoft Azure) to 
dynamically adjust resources based on live traffic demands.

"""

# "The API receives the request and the server crashes before saving it to the database. What would you do?"
"""
The approach depends on the business requirement. For critical operations like payments or orders, 
I would first make the request idempotent using an idempotency key. Then I'd persist the request to a 
durable message queue like RabbitMQ, Kafka, or AWS SQS. A background worker would process the queue and 
write to the database. I'd also use retries with exponential backoff for transient failures, database 
transactions to prevent partial writes, and a dead-letter queue for messages that repeatedly fail. 
This combination minimizes data loss while preventing duplicate processing.
"""

# A database table receives a high volume of both read and write operations. How would you optimize query 
# performance? Would you use indexes? If so, how would you decide which columns to index?
"""
Indexes improve read performance because they allow PostgreSQL to locate rows using a B-tree instead 
of scanning the entire table. However, indexes introduce overhead on INSERT, UPDATE, and DELETE operations 
because every index must also be maintained. If a table has both high read and high write traffic, I wouldn't 
index every column. I would first analyze the query patterns using slow query logs and EXPLAIN ANALYZE, 
then create indexes only on columns that are frequently used in WHERE clauses, JOIN conditions, ORDER BY, 
or GROUP BY. For multi-column filters, I'd consider composite indexes with the correct column order. 
Beyond indexing, I'd optimize queries by selecting only needed columns, use pagination for large result sets, 
cache frequently accessed data in Redis, and if read traffic becomes very high, use read replicas. 
For very large tables, partitioning may also be appropriate.
"""

