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