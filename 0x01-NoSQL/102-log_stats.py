#!/usr/bin/env python3
"""
Module for analyzing Nginx logs stored in MongoDB with IP statistics
"""
from pymongo import MongoClient


def log_stats():
    """
    Analyzes Nginx logs in the 'logs.nginx' collection and prints statistics.

    Outputs:
        - Total number of logs
        - Count of logs for each HTTP method (GET, POST, PUT, PATCH, DELETE)
        - Count of logs with method=GET and path=/status
        - Top 10 most frequent IP addresses
    """
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    # Total number of logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Count logs for each HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Count logs with method=GET and path=/status
    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")

    # Get top 10 IPs
    pipeline = [
        {
            "$group": {
                "_id": "$ip",
                "count": {"$sum": 1}
            }
        },
        {
            "$sort": {
                "count": -1
            }
        },
        {
            "$limit": 10
        }
    ]
    top_ips = list(collection.aggregate(pipeline))
    print("IPs:")
    for ip_data in top_ips:
        print(f"\t{ip_data['_id']}: {ip_data['count']}")


if __name__ == "__main__":
    log_stats()
