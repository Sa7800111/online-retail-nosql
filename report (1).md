README.md: Retail Data Integration Using MongoDB, Redis, and Neo4j
Project: Unified Retail Data Management System Using NoSQL Databases

Team Member : Sangeeth sajeev menon

Use Case: Retail Data Management and Analysis
This project will be developed for an integrated system that stores, caches, and analyzes the relationships in retail data. It will efficiently manage transactional data, reduce latency in queries, and draw inferences about customer behavior and relationships between products.
 
 How Each Database Type is Used:
 1. MongoDB
Purpose: Primary database for storing raw transactional data in a document-oriented format.
Why MongoDB?
Flexible schema for semi-structured data like transactions.
Data Structure:
Each document represents a transaction with fields such as:
InvoiceNo: Unique identifier for each transaction.
CustomerID: Identifier for the customer.
StockCode: Product code.
Description: Product description.
Quantity: Quantity purchased.
UnitPrice: Price per unit.
InvoiceDate: Date and time of the transaction.
Country: Customer's location

2. Redis
Purpose: To cache frequently accessed data, such as transaction statuses, for quicker retrieval.
Why Redis?
Optimized for low-latency data access.
Data Structure:
Key-value pairs:
Key: transaction:<InvoiceNo>:status
Value: Transaction status, such as large-transaction, small-transaction.
Sample Queries:
python
Copy code
# Insert data into Redis
redis_client.set(f"transaction:{record['InvoiceNo']}:status", status_value)

# Fetch data from Redis
redis_client.get(f"transaction:{InvoiceNo}:status")

3. Neo4j
Objective: To store and query the complex relationship between customers, transactions, and products.
Why Neo4j?
Graph-based data model to outline patterns and relationships.
Data Structure:
Nodes:
Customer: For Customers
Transaction: For Transactions
Product: For Products
Relationships:
MADE: The relationship between Customer and Transaction
INCLUDES: The relationship between Transaction and Product
Sample Query:
cypher
Copy code
MATCH (c:Customer)-[:MADE]->(t:Transaction)-[:INCLUDES]->(p:Product)
RETURN c.id AS CustomerID, t.id AS TransactionID, p.description AS ProductDescription

System Requirements:
Initial Dataset: online_retail_subset_cleaned.csv
Fields include InvoiceNo, StockCode, CustomerID, etc.
Insert Queries:
MongoDB:
python
Copy code
collection.insert_many(data_dict)
Redis:
python
Copy code
redis_client.set(f"transaction:{record['InvoiceNo']}:status", status_value)
Neo4j:
cypher
Copy code
MERGE (c:Customer {id: $CustomerID})
MERGE (t:Transaction {id: $InvoiceNo})
MERGE (p:Product {id: $StockCode})
MERGE (c)-[:MADE]->(t)
MERGE (t)-[:INCLUDES]->(p)

Streamlit Dashboard :
A user-friendly dashboard built using Streamlit allows users to:

View sample transactional data stored in MongoDB.
Retrieve transaction statuses cached in Redis.
Analyze customer, transaction, and product relationships in Neo4j.

Tools and Technologies
Programming Language: Python
Libraries: streamlit, pymongo, redis, neo4j
Databases:
MongoDB: Cloud-hosted on MongoDB Atlas.
Redis: Hosted on redis-14372.c327.europe-west1-2.gce.redns.redis-cloud.com.
Neo4j: Cloud-hosted on Neo4j AuraDB.

Summary
This project demonstrates the integration of three NoSQL databases to manage, cache, and analyze retail data:

MongoDB for flexible document storage.
Redis for high-performance caching.
Neo4j for managing complex relationships.
By combining the strengths of these databases, the system provides a robust, scalable solution for retail data management.

github
https://github.com/Sa7800111/online-retail-nosql
# Insert data into MongoDB
collection.insert_many(data_dict)

# Insert data into Redis
redis_client.set(f"transaction:{record['InvoiceNo']}:status", status_value)

# Insert data into Neo4j
MERGE (c:Customer {id: $CustomerID})
MERGE (t:Transaction {id: $InvoiceNo})
MERGE (p:Product {id: $StockCode})
MERGE (c)-[:MADE]->(t)
MERGE (t)-[:INCLUDES]->(p)

# Fetch data from Redis
redis_client.get(f"transaction:{InvoiceNo}:status")

# Fetch data from Neo4j
MATCH (c:Customer)-[:MADE]->(t:Transaction)-[:INCLUDES]->(p:Product)
RETURN c.id AS CustomerID, t.id AS TransactionID, p.description AS ProductDescription
