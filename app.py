import streamlit as st
from pymongo import MongoClient
import redis
from neo4j import GraphDatabase

# MongoDB Connection
def connect_mongodb():
    """Connect to MongoDB and return the collection."""
    client = MongoClient("mongodb.mongodb.net")  # MongoDB connection string
    db = client["RetailDB"]  # Replace with your database name
    collection = db["RetailTransactions"]  # Replace with your collection name
    return collection

# Redis Connection
def connect_redis():
    """Connect to Redis and return the client."""
    redis_client = redis.StrictRedis(
        host="",  # Redis host
        port=,  # Redis port
        password="",  # Redis password
        decode_responses=True  # Decode responses to strings
    )
    return redis_client

# Neo4j Connection
def connect_neo4j():
    """Connect to Neo4j and return the driver."""
    uri = ""  # Neo4j URI
    username = ""  # Neo4j username
    password = ""  # Neo4j password
    driver = GraphDatabase.driver(uri, auth=(username, password))
    return driver

# Streamlit App
st.title("Retail Data Dashboard")

# MongoDB Section
st.header("MongoDB: Retail Transactions")
collection = connect_mongodb()

# Fetch and display MongoDB data
st.subheader("Sample MongoDB Data")
mongo_sample = collection.find().limit(5)
for record in mongo_sample:
    st.json(record)

# Redis Section
st.header("Redis: Transaction Statuses")
redis_client = connect_redis()

# Fetch and display Redis data
st.subheader("Sample Redis Data")
try:
    sample_keys = redis_client.keys("transaction:*")
    for key in sample_keys[:5]:  # Display only the first 5 keys
        value = redis_client.get(key)
        st.write(f"Key: {key}, Value: {value}")
except Exception as e:
    st.error(f"Error fetching Redis data: {e}")
