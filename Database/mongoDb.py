# What is MongoDB?
"MongoDB is a NoSQL document database that stores data as BSON documents instead of rows and tables."

# Why MongoDB instead of PostgreSQL?
"""
Data structure changes frequently
Large volumes of logs/events
Complex joins aren't required
High write throughput is needed

Examples:
Webhook audit logs, Analytics, Activity tracking, Notification history"""

# What is BSON?
"MongoDB stores data in BSON (Binary JSON)."

# What is ObjectId?
"""
Every document gets:
{
  "_id": ObjectId("...")
}

ObjectId contains:
Timestamp, Machine identifier, Process id, Counter

It is unique and indexed automatically."""

# What is a Collection?
"""Equivalent of a table.
PostgreSQL → Table
MongoDB → Collection"""

# What is a Document?
"""Equivalent of a row. Every json obj is a document."""

# What are Indexes in MongoDB?
"Exactly like PostgreSQL indexes."

# What is Aggregation?
"""
Equivalent of: GROUP BY, SUM,COUNT,AVG

Example:
Count webhooks by event:
db.webhooks.aggregate([
{
 "$group":{
   "_id":"$event",
   "count":{"$sum":1}
 }
}
])"""

# What is Sharding?
"""MongoDB's horizontal scaling.
Use:
Shard 1
Shard 2
Shard 3
Data distributed automatically. Useful when data becomes TBs in size."""

# What is Replica Set?
"""High Availability.
Primary
Secondary
Secondary

Writes go to Primary.
If Primary fails: Mongo elects another Primary."""

# Difference Between Sharding and Replication?
"""
Replication: Same data copied
Purpose: High Availability.

Sharding: Data split
Purpose: Scale storage and throughput."""

# What is Embedding?
"Store child document inside parent."

# What is Referencing?
"Equivalent of foreign key."

# Embedding vs Referencing?
"""
Embedding:
{
 event,
 performers[]
}

Pros: Fast reads, One query

Referencing:
{
 performer_id
}

Pros:Less duplication"""

# What is MongoDB TTL?
"""Auto-delete documents. (eg: Delete webhook logs after 90 days.)
syntax:

db.webhooks.createIndex(
{
   "created_at":1
},
{
   expireAfterSeconds:7776000
}
)
"""
# What is Schema Validation?
"""MongoDB is schema flexible. But we can enforce rules. 
Example:
{
  required:[
      "payment_id",
      "event"
  ]
}"""

# What are MongoDB limitations?
"""
No true joins like PostgreSQL
Multi-document transactions are slower
Complex reporting is harder
Data duplication is common
"""

